import os
import cv2
import time

from InputBuilder import InputBuilder
from ActionBuilder import ActionBuilder

start_time = time.time()

builder = InputBuilder()
action = ActionBuilder()

#sourcePath = 'D:\\GGST_DATA\\RIPPER_REFERENCE_DATA\\ICON_REFERENCE_FRAMES\\'
#sourcePath = 'D:\\GGST_DATA\\RIPPER_REFERENCE_DATA\\TEST_FRAMES\\'
#sourceName = 'ALL_TEN.png'
#sourceImage = cv2.imread(sourcePath + sourceName)
   
<<<<<<< HEAD
pathName = 'D:\\GGST_DATA\\BATTLE_DATA_FRAMES\\SOL_KY\\ROUND_THREE_WIN\\FIGHT_ONE\\'
=======
pathName = 'C:\\Users\\Justin\\Pictures\\GGST_EXAMPLE_BATTLE\\'
>>>>>>> d580bbda570ed641d270cdf4203ec8ac3f82388c

files_in_directory = os.listdir(pathName)

for fileName in files_in_directory:

    full_path = os.path.join(pathName, fileName)
    image = cv2.imread(pathName + fileName)

    test, bool_list = builder.get_input(image)

    print(test)
<<<<<<< HEAD
    #print(bool_list)
   
    new_size = (1280, 720)
=======
    print(bool_list)
   
    new_size = (960, 540)
>>>>>>> d580bbda570ed641d270cdf4203ec8ac3f82388c
    resized_image = cv2.resize(image, new_size)
    cv2.imshow('debug_image', resized_image)

    key = cv2.waitKey(0) & 0xFF
    if key == ord('q'):
        break

cv2.destroyAllWindows()





#THIS IS FOR DEBUG - LEAVE IT

#end_time = time.time()
#elapsed_time_ms = (end_time - start_time) * 1000
#print(f'Elapsed time for this loop: {elapsed_time_ms}ms')
#new_size = (1280, 720)
#resized_image = cv2.resize(sourceImage, new_size)
#cv2.imshow('debug_image', resized_image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#THIS IS FOR DEBUG - LEAVE IT