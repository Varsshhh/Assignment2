#Imports
from PIL import Image, ImageFilter
import numpy as np

class BlurImage(object):
    '''
        Applies Gaussian Blur on the image.
    '''

    def __init__(self, radius):
        '''
            Arguments:
            radius (int): radius to blur
        '''
        self.radius = radius

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL Image)

            Returns:
            image (numpy array or PIL Image)
        '''
        # if isinstance(image) == np.ndarray:
        #     image = Image.fromarray(np.uint8(image))
         
        image = image.filter(ImageFilter.GaussianBlur(self.radius))

        
        return image
