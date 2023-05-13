from flask import Flask, request
from paste.translogger import TransLogger
from waitress import serve
import subprocess
import json
from ml import get_room_details, get_advert_title, get_advert_desc, get_mentioned_feature
# from flask_cors import CORS

import os

app = Flask(__name__)
# CORS(app)

def create_url(pid):
    subprocess.run(["git", "-C","app", "add", "."]) 
    subprocess.run(["git", "-C","app", "commit", "-a", "-m", f"""\"{pid} images\""""])
    subprocess.run(["git", "-C","app", "push"]) 


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
        image_url.append(f'https://raw.githubusercontent.com/prashant3167/fastrestbai/main/static/{pid}/{filename}')
    create_url(pid)
    detected_room = []
    detected_feautres = []
    for i in image_url:
        t0,t1 =get_room_details(i)
        detected_room.append(t0)
        detected_feautres.extend(t1)

    detected_feautres = set(detected_feautres) + set(detected_room)
    mentioned_features = set(get_mentioned_feature(data))
    desc = get_advert_desc(mentioned_features)
    title = get_advert_title(mentioned_features)

    prepare_response = dict()
    prepare_response['property_id'] = pid
    prepare_response['title'] = title
    prepare_response['description'] = desc
    prepare_response['mentioned_features'] = mentioned_features
    prepare_response['detected_feautres'] = detected_feautres
    prepare_response['image_url'] = image_url

    print(prepare_response)

    with open('app/static/'+pid+'/' + pid + '.json', "w") as fp:
        json.dump(prepare_response, fp, indent=4)

    return {"hbc": request.files.getlist("upload")}

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
