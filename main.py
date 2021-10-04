# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import urllib.request
import ssl

import cv2
import urllib.request

import requests
from PIL import Image

from flask import Flask, request, abort


def dhash(image, hashSize=8):
	# resize the input image, adding a single column (width) so we
	# can compute the horizontal gradient
	resized = cv2.resize(image, (hashSize + 1, hashSize))

	# compute the (relative) horizontal gradient between adjacent
	# column pixels
	diff = resized[:, 1:] > resized[:, :-1]

	# convert the difference image to a hash
	return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])

app = Flask(__name__)

@app.route("/")
def home():
    return 'home'
@app.route('/hashi', methods=['GET', 'POST'])
def hashing():
    imageName = request.args.get('image')
    urlImage = 'https://dwjz5q0kg4677.cloudfront.net/'+imageName
    request_response = requests.head(urlImage)
    status_code = request_response.status_code
    website_is_up = status_code == 200
    if website_is_up == False:
        abort(404)
    print("websitete is ippp", website_is_up)
    ssl._create_default_https_context = ssl._create_unverified_context
    print(urlImage)
    urllib.request.urlretrieve(
        urlImage,
        "gfg")
    image = cv2.imread("gfg")

    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.waitKey(0)

    imageHash = dhash(image)

    return str(imageHash)
if __name__ == "__main__":
    app.run(debug=True)