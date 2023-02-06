#Imports
from my_package.model import ImageCaptioningModel
from my_package.data import Dataset, Download
from my_package.data.transforms import FlipImage, RescaleImage, BlurImage, CropImage, RotateImage
import numpy as np
from PIL import Image
import os


def experiment(annotation_file, captioner, transforms, outputs):
    '''
        Function to perform the desired experiments
        Arguments:
        annotation_file: Path to annotation file
        captioner: The image captioner
        transforms: List of transforms to be applied to the image
        outputs: Path to the directory where the plots are to be stored
    '''
     #Create the instances of the dataset and download
    dataset = Dataset(annotation_file,transforms)
    downloader = Download()
    
    print("\n\n--------------------------------------ANALYSIS TASK-1 ---------------------------------------------")
    
    # Enumerate over the data items
    for i,tup in enumerate(dataset):
        image_name,captions,image_url=tup
        current_image_path=outputs+'/'+str(i)+".jpg"
        # Download images to ./data/imgs   
        downloader(image_url,current_image_path)

        # Print the image names and their captions
        print(f"\nFILE NAME: {image_name}")
        print("Generated Captions: ")
        for i,caption in enumerate(captions):
            print("\t\t",end=" ")
            print(i+1,'-',caption["caption"],sep="")
        print()
    
    print("\n-----All the images are downloaded into path './data/imgs' and captions are displayed successfully-----\n")
                
    myimage=Image.open(outputs+'/'+"3.jpg")
    
    print("\n--------------------------------------ANALYSIS TASK-2 ---------------------------------------------\n")    


    transformed_images_path = "Python_DS_Assignment_Question_02/data/transformed-imgs"

    if not os.path.exists(transformed_images_path):
        os.makedirs(transformed_images_path)
        print("--> Successfully created Sub-dir path to store the tranformed imgs")
    else:
        print("--> Sub-dir path already exists\n--> Creation of new Sub-dir omitted")    
    
    for i,transform in enumerate(transforms):
        if transform is not None:
            transformed_image=transform(myimage)
            transformed_image_path=transformed_images_path+'/'+"transform-"+chr(97+i)+".jpg"
            transformed_image.save(transformed_image_path)
            prediction=captioner(transformed_image_path,num_captions=3)
            print("\nFILE NAME: transform-"+chr(i+97)+".jpg")
            print("Generated captions: ")
            for i,cap in enumerate(prediction):
                print("\t\t",end=" ")
                print(i+1,'-',cap,sep="")  
              
        else:
            newly_saved_og_image_path=transformed_images_path+'/'+"transform-"+chr(97+i)+".jpg"
            myimage.save(newly_saved_og_image_path)
            prediction=captioner(newly_saved_og_image_path,num_captions=3)
            print("\nFILE NAME: transform-"+chr(i+97)+".jpg")
            print("Generated captions: ")
            for i,cap in enumerate(prediction):
                print("\t\t",end=" ")
                print(i+1,'-',cap,sep="")  
    
    print("\n---All the transformed images are downloaded into path './data/transformed-imgs' and the generated captions are displayed successfully---\n")
    
    print("\n----------------------------------------END OF MAIN------------------------------------------------")
    
    #Create the instances of the dataset, download


    #Print image names and their captions from annotation file using dataset object


    #Download images to ./data/imgs/ folder using download object


    #Transform the required image (roll number mod 10) and save it seperately


    #Get the predictions from the captioner for the above saved transformed image  


def main():
    # Load the image captioning model
    captioner = ImageCaptioningModel()
    
    # Load the annotation file
    annotation_file = 'Python_DS_Assignment_Question_02/data/annotations.jsonl'

    # Specify the path to the outputs directory
    outputs ='Python_DS_Assignment_Question_02/data/imgs'
        
    # Specify the transforms to be applied to the image
    transforms = [None,FlipImage(),BlurImage(10),RescaleImage((1280,1080)),RescaleImage((320,270)),RotateImage(90),RotateImage(315)]
                
    # Analysis Tasks
    experiment(annotation_file,captioner, transforms, outputs)            

if __name__ == '__main__':
    main()
