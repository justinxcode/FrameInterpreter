import os
import cv2
import numpy as np


class IconMatch:
    def __init__(self):
            # Reference path
            self.referencePath_720p = ''
            self.referencePath_1080p = ''
            self.referencePath_1440p = 'icons\\1440p\\'
            self.referencePath_2160p = ''

    def mse_score(self, image_one, image_two):
        # Compute the mean squared error between two images
        mse_score = np.sum((image_one.astype("float") - image_two.astype("float")) ** 2)
        mse_score /= float(image_one.shape[0] * image_one.shape[1])
        return mse_score
    
    def define_reference(self, referenceResolution):
        try:
            if(referenceResolution == 720):
                referencePath = self.referencePath_720p
            elif(referenceResolution == 1080):
                referencePath = self.referencePath_1080p
            elif(referenceResolution == 1440):
                referencePath = self.referencePath_1440p
            elif(referenceResolution == 2160):
                referencePath = self.referencePath_2160p
            else:
                raise ValueError(f"Unsupported Resolution: {referenceResolution}")
        

            # Get the list of reference files names
            referenceFiles = os.listdir(referencePath)

            # Get the count of reference files
            referenceFileCount = len(referenceFiles)

            if referenceFileCount != 32:
                raise ValueError(f"Incorrect number of reference files: {referenceFileCount} / 32")

        except ValueError as e:
            print(f"An error occurred in define_reference: {str(e)}")
            raise

        return {referenceFile: cv2.imread(referencePath + referenceFile) for referenceFile in referenceFiles}.items()
    
    def find_match(self, frame, referenceResolution):

        match_found = False
        closest_match_name = None
        closest_match_score = float('inf')

        referenceImages = self.define_reference(referenceResolution)

        for referenceName, referenceImage in referenceImages:
 
            #Call mse score to compare images
            mse_score = self.mse_score(frame, referenceImage)
            #print(f"MSE with {referenceName} with score {mse_score:.2f}!")

            if mse_score < 2000:  # Adjust this threshold according to your requirement
                print(f"Match found with {referenceName} with score {mse_score:.2f}!")
                match_found = True
                break
            elif mse_score < closest_match_score:
                closest_match_score = round(mse_score, 2)
                closest_match_name = referenceName

        if not match_found:
            if closest_match_score <= 10000.00:
                print(f"Closest match found with {closest_match_name} with score {closest_match_score}!")
            else:
                print("Probably Neutral?")
            
