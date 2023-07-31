import numpy as np

class IconMatch:
    def __init__(self):
            self.mse_threshold = float(7000)

    def mse_score(self, image_one, image_two):

        mse_score = np.sum((image_one.astype('float') - image_two.astype('float')) ** 2)

        mse_score /= float(image_one.shape[0] * image_one.shape[1])

        return mse_score
    
    def find_match(self, frame, referenceImages):

        lowest_mse_score = float('inf')

        for referenceName, referenceImage in referenceImages:
 
            mse_score = self.mse_score(frame, referenceImage)

            if mse_score < lowest_mse_score and mse_score < self.mse_threshold:
                lowest_mse_score = mse_score
                lowest_input_name = referenceName

        if lowest_mse_score >= self.mse_threshold:
            return 'NEUTRAL'
        
        #print(f"MSE with {lowest_input_name} with score {lowest_mse_score:.2f}!")
        return lowest_input_name
            
