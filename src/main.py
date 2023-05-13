from flask import Flask, request

app = Flask(__name__)

@app.route('/upload/', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return 'No image uploaded.', 400

    image = request.files['image']
    # You can save the image to a directory or perform any other processing here.
    # For simplicity, let's just return the name of the uploaded image.
    return 'Image uploaded: ' + image.filename


@app.route('/tets/', methods=['GET'])
def test():
    # if 'image' not in request.files:
    #     return 'No image uploaded.', 400

    # image = request.files['image']
    # # You can save the image to a directory or perform any other processing here.
    # # For simplicity, let's just return the name of the uploaded image.
    return 'Image uploaded:'


if __name__ == '__main__':
    app.run(port=8000)