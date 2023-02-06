from PIL import Image
import numpy as np

class FlipImage(object):
    '''
        Flips the image.
    '''

    def __init__(self, flip_type='horizontal'):
        '''
            Arguments:
            flip_type: 'horizontal' or 'vertical' Default: 'horizontal'
        '''
        self.flip_type = flip_type

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''
        
        # if isinstance(image) == np.ndarray:
        #     image = Image.fromarray(np.uint8(image))
            
        image=image.transpose(Image.FLIP_LEFT_RIGHT if self.flip_type == 'horizontal' else Image.FLIP_TOP_BOTTOM)
        
        return image
