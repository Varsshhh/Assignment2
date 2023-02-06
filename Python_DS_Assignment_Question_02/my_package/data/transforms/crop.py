#Imports
import random
from PIL import Image
import numpy as np

class CropImage(object):  
    '''
        Performs either random cropping or center cropping.
    '''

    def __init__(self, shape, crop_type='center'):
        '''
            Arguments:
            shape: output shape of the crop (h, w)
            crop_type: center crop or random crop. Default: center
        ''' 
        self.shape = shape
        self.crop_type = crop_type

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''
        # if isinstance(image) == np.ndarray:
        #     image = Image.fromarray(np.uint8(image))
        
        iw, ih = image.size
        h, w = self.shape
        
        if self.crop_type == 'center':
            left = (iw - w) // 2
            top = (ih - h) // 2
            right = (iw + w) // 2
            bottom = (ih + h) // 2
        elif self.crop_type == 'random':
            left = random.randint(0, iw - w)
            top = random.randint(0, ih - h)
            right = left + w
            bottom = top + h
        else:
            raise ValueError("Invalid crop type")
        
        image = image.crop((left, top, right, bottom))
        
        return image
