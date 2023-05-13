from flask import Flask, request
from paste.translogger import TransLogger
from waitress import serve
# from flask_cors import CORS

import os

app = Flask(__name__)
# CORS(app)


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
    for file in request.files.getlist("files"):
        print(file)
        filename = file.filename
        file.save('app/static/'+pid+'/'+filename)

    # image.save('/app/'+image.filename)
    # You can save the image to a directory or perform any other processing here.
    # For simplicity, let's just return the name of the uploaded image.
    # return "Image uploaded: " + image.filename
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
