from flask import Flask, request
from paste.translogger import TransLogger
from waitress import serve
import subprocess
from ml import get_room_details
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
    print(request.form.keys())
    
    if "files" not in request.files:
        return "No image uploaded.", 400
    # print(request.files["files"])
    # # image = request.files["files"]
    pid = request.form['name']
    print(type(request.form))
    os.makedirs('app/static/'+pid,exist_ok=True)
    # # image.save('/app/static/test.jpeg')
    data = request.form.to_dict() 
    print(data)
    image_url = []
    for file in request.files.getlist("files"):
        print(file)
        filename = file.filename
        file.save('app/static/'+pid+'/'+filename)
        image_url.append(f'https://raw.githubusercontent.com/prashant3167/fastrestbai/main/static/{pid}/{filename}')
    create_url(pid)
    for i in image_url:
        r_type,r_feature =get_room_details(i)
        print(r_type,r_feature)

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
