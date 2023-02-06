from PIL import Image
import numpy as np


class RescaleImage(object):
    '''
        Rescales the image to a given size.
    '''

    def __init__(self, output_size):
        '''
            Arguments:
            output_size (tuple or int): Desired output size. If tuple, output is
            matched to output_size. If int, smaller of image edges is matched
            to output_size keeping aspect ratio the same.
        '''
        assert isinstance(output_size, (int, tuple))
        self.output_size = output_size

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (PIL image)
            Note: You do not need to resize the bounding boxes. ONLY RESIZE THE IMAGE.
        '''
        
        # if isinstance(image) == np.ndarray:
        #     image = Image.fromarray(np.uint8(image))
 
        old_size = image.size

        if isinstance(self.output_size, int):
            ratio = float(self.output_size) / min(old_size)
            new_size = tuple([int(x * ratio) for x in old_size])
        else:
            new_size = self.output_size

        image = image.resize(new_size, Image.ANTIALIAS)

        return image
