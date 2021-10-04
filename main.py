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


app = Flask(__name__)


@app.route("/")
def hello_world():
 return "<p>Hello, World!</p>"

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000)
