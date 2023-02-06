from PIL import Image
import numpy as np

class RotateImage(object):
    '''
        Rotates the image about the centre of the image.
    '''

    def __init__(self, degrees):
        '''
            Arguments:
            degrees: rotation degree.
        '''
        self.degrees = degrees

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (PIL image)
        '''
        # if isinstance(image) == np.ndarray:
        #     image = Image.fromarray(np.uint8(image))
        
        image = image.rotate(self.degrees, resample=Image.BICUBIC, expand=True)
        return image
    
        # image = Image.fromarray(np.uint8(image))
        # return np.array(image.rotate(self.degrees, resample=Image.BICUBIC, expand=True))
