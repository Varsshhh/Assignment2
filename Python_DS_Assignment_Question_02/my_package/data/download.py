from io import BytesIO
from PIL import Image
import requests

class Download(object):
    '''
        A class for helping in dowloading the required images from the given url to the specified path
    '''
    def __call__(self, url, path):
        response = requests.get(url,timeout=10)
        image = Image.open(BytesIO(response.content))
        image.save(path)

