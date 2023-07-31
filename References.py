import os
import cv2

class References:
    def __init__(self):
            # Reference paths
            self.referencePath_720p = '' #TODO
            self.referencePath_1080p = '' #TODO
            self.referencePath_1440p = 'icons\\1440p\\'
            self.referencePath_2160p = '' #TODO
            self.referenceResolution = 1440
            self.directionsFileNames = ["UP.png"
                                        , "UP_FADE.png"
                                        , "LEFT.png"
                                        , "LEFT_FADE.png"
                                        , "DOWN.png"
                                        , "DOWN_FADE.png"
                                        , "RIGHT.png"
                                        , "RIGHT_FADE.png"
                                        , "UP_LEFT.png"
                                        , "UP_LEFT_FADE.png"
                                        , "UP_RIGHT.png"
                                        , "UP_RIGHT_FADE.png"
                                        , "DOWN_LEFT.png"
                                        , "DOWN_LEFT_FADE.png"
                                        , "DOWN_RIGHT.png"
                                        , "DOWN_RIGHT_FADE.png"
                                        ]

    def get_reference_path(self):
        try:
            if(self.referenceResolution == 720):
                referencePath = self.referencePath_720p
            elif(self.referenceResolution == 1080):
                referencePath = self.referencePath_1080p
            elif(self.referenceResolution == 1440):
                referencePath = self.referencePath_1440p
            elif(self.referenceResolution == 2160):
                referencePath = self.referencePath_2160p
            else:
                raise ValueError(f"Unsupported Resolution: {self.referenceResolution}")

        except ValueError as e:
            print(f"An error occurred in define_reference: {str(e)}")
            raise

        return referencePath

    def get_all_references(self):

        referencePath = self.get_reference_path()

        referenceFileNames = os.listdir(referencePath)

        dictionary = {}

        for referenceFileName in referenceFileNames:
            input_name, _ = os.path.splitext(referenceFileName)
            dictionary[input_name] = cv2.imread(referencePath + referenceFileName)

        return dictionary

    def get_button_references(self):

        referencePath = self.get_reference_path()

        referenceFileNames = os.listdir(referencePath)

        buttons_only = [x for x in referenceFileNames if x not in self.directionsFileNames]

        dictionary = {}

        for referenceFileName in buttons_only:
            input_name, _ = os.path.splitext(referenceFileName)
            dictionary[input_name] = cv2.imread(referencePath + referenceFileName)

        return dictionary
    
    def get_direction_references(self):

        referencePath = self.get_reference_path()

        referenceFileNames = os.listdir(referencePath)

        directions_only = [x for x in referenceFileNames if x in self.directionsFileNames]

        dictionary = {}

        for referenceFileName in directions_only:
            input_name, _ = os.path.splitext(referenceFileName)
            dictionary[input_name] = cv2.imread(referencePath + referenceFileName)

        return dictionary
    