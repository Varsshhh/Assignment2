import os
import jsonlines
from PIL import Image
import numpy as np

class Dataset(object):
    '''
        A class for the dataset that will return data items as per the given index
    '''

    def __init__(self, annotation_file, transforms=None):
        '''
            Arguments:
            annotation_file: path to the annotation file
            transforms: list of transforms (class instances)
            For instance, [<class 'RandomCrop'>, <class 'Rotate'>]
        '''
        self.annotation_file = annotation_file
        self.transforms = transforms
        self.annotations = []
        with jsonlines.open(self.annotation_file,mode='r') as reader:
            for obj in reader:
                self.annotations.append(obj)

    def __len__(self):
        '''
            return the number of data points in the dataset
        '''
        return len(self.annotations)

    def __getitem__(self, index):
        '''
            return the data items for the index as an object
        '''
        obj = self.annotations[index]
        image_name = obj['file_name']
        captions = obj['captions']
        image_url=obj['url']
        return image_name, captions,image_url

    def __transformitem__(self, path):
        '''
            return transformed PIL Image object for the image in the given path
        '''
        if not os.path.exists(path):
            raise FileNotFoundError(f"File not found: {path}")
        image = Image.open(path)
        if self.transforms:
            for transform in self.transforms:
                image = transform(image)
        return image
