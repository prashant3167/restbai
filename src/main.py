from flask import Flask, request
from paste.translogger import TransLogger
from waitress import serve

app = Flask(__name__)


@app.route("/upload/", methods=["POST"])
def upload():
    if "image" not in request.files:
        return "No image uploaded.", 400

    # image = request.files["image"]
    for file in request.files.getlist("upload"):
        print(file)
        filename = file.filename
        destination = "/".join(['/app/static', filename])
        print("Accept incoming file:", filename)
        print(destination)
        file.save(destination)

    # image.save('/app/'+image.filename)
    # You can save the image to a directory or perform any other processing here.
    # For simplicity, let's just return the name of the uploaded image.
    # return "Image uploaded: " + image.filename


@app.route("/tets/", methods=["GET"])
def test():
    # if 'image' not in request.files:
    #     return 'No image uploaded.', 400

    # image = request.files['image']
    # # You can save the image to a directory or perform any other processing here.
    # # For simplicity, let's just return the name of the uploaded image.
    return {"hbc": "Image uploaded:"}


if __name__ == "__main__":
    # app.run(port=8000)
    serve(TransLogger(app), host="0.0.0.0", port=8000, threads=10)
