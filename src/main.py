from flask import Flask, request
from paste.translogger import TransLogger
from waitress import serve
import subprocess
from string import whitespace
import json
from ml import get_room_details, get_advert_title, get_advert_desc, get_mentioned_feature
from flask_cors import CORS
from cloudinary.uploader import upload as upload_cloud
from cloudinary.utils import cloudinary_url
import cloudinary
import logging
# logging.getLogger('')
logger = logging.getLogger()
cloudinary.config(
  cloud_name = "dytf3ytro",
  api_key = "946492928211747",
  api_secret = "NnzYE9b2fmqQ5tAdsB__VDMRjxw",
  secure = True
)


import os

app = Flask(__name__)
CORS(app)

def create_url(pid):
    subprocess.run(["git", "-C","/static_files","config", "--global","user.email", "\"you@example.com\""])
    subprocess.run(["git", "-C","/static_files","config", "--global","user.name", "\"you@example.com\""])
    subprocess.run(["git", "-C","/static_files", "add", "."]) 
    subprocess.run(["git", "-C","/static_files", "commit", "-a", "-m", f"""\"{pid} images\""""])
    subprocess.run(["git", "-C","/static_files", "push"])

@app.route("/upload", methods=["POST"])
def upload():
    print("request.form.keys")
    print(request.form.keys())
    
    if "files" not in request.files:
        return "No image uploaded.", 400
    # print(request.files["files"])
    # # image = request.files["files"]
    pid = request.form['name']
    print("request.form")
    print(type(request.form))
    os.makedirs('app/static/'+pid,exist_ok=True)
    # # image.save('/app/static/test.jpeg')
    data = request.form.to_dict()
    print("request.form.to_dict")
    print(data)
    image_url = []
    
    for file in request.files.getlist("files"):
        print(file)
        filename = file.filename
        file.save('app/static/'+pid+'/'+filename)
        url_data = upload_cloud('app/static/'+pid+'/'+filename)

        image_url.append(url_data['url'])
    # create_url(pid)
    detected_room = []
    detected_feautres = []
    prepare_response = dict()
    prepare_response['images'] = []
    for i in image_url:
        t0,t1 =get_room_details(i)
        detected_room.append(t0)
        detected_feautres.extend(t1)
        prepare_response['images'].append({'url':i,'type':t0})

    detected_feautres = list(set(detected_feautres) | set(detected_room))
    mentioned_features = list(set(get_mentioned_feature(data)))
    red_zone  = list(set(mentioned_features)-set(detected_feautres))
    green_zone  = list(set(mentioned_features).intersection(set(detected_feautres)))
    yellow_zone = list(set(detected_feautres)-set(mentioned_features))
    desc = get_advert_desc(mentioned_features)
    
    title = get_advert_title(mentioned_features)

    prepare_response['property_id'] = pid
    prepare_response['title'] = title.strip(' "\'\t\r\n')
    prepare_response['description'] = desc.strip(' "\'\t\r\n')
    prepare_response['mentioned_features'] = mentioned_features
    prepare_response['detected_feautres'] = detected_feautres
    prepare_response['green'] = green_zone
    prepare_response['yellow'] = yellow_zone
    prepare_response['red'] = red_zone

    print(prepare_response)
    with open('app/static/'+pid+'/' + pid + '.json', "w") as fp:
        json.dump(prepare_response, fp, indent=4)

    return {"hbc": request.files.getlist("upload")}

@app.route('/advert/<pid>', methods=['GET'])
def get_advert(pid):
    logger.debug('app/static/' + pid + '/' + pid + '.json')
    with open('app/static/' + pid + '/' + pid + '.json', "r") as f:
        response = json.load(f)
    return response

@app.route("/tets/", methods=["GET"])
def test():
    # if 'image' not in request.files:
    #     return 'No image uploaded.', 400

    # image = request.files['image']
    # # You can save the image to a directory or perform any other processing here.
    # # For simplicity, let's just return the name of the uploaded image.
    return {"hbc": "Image uploaded:"}


if __name__ == "__main__":
    # app.run(port=8000,debug=True)
    serve(TransLogger(app), host="0.0.0.0", port=8000, threads=10)
