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


            
pathName = 'D:\\GGST_DATA\\BATTLE_DATA_FRAMES\\SOL_KY\\ROUNDT_THREE_WIN\\FIGHT_ONE\\'

files_in_directory = os.listdir(pathName)

for fileName in files_in_directory:

    full_path = os.path.join(pathName, fileName)
    image = cv2.imread(pathName + fileName)

    returned = builder.position_one_input(image)
    print(returned)

    action = action.create_action_array(returned)
    print(action)

    new_size = (1280, 720)
    resized_image = cv2.resize(image, new_size)
    cv2.imshow('debug_image', resized_image)

    key = cv2.waitKey(0) & 0xFF
    if key == ord('q'):
        break

cv2.destroyAllWindows()





#cv2.imshow('TEST', first_position)

#end_time = time.time()
#elapsed_time_ms = (end_time - start_time) * 1000
#print(f'Elapsed time for this loop: {elapsed_time_ms}ms')
#THIS IS FOR DEBUG - LEAVE IT


#new_size = (1280, 720)
#resized_image = cv2.resize(sourceImage, new_size)
#cv2.imshow('debug_image', resized_image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#THIS IS FOR DEBUG - LEAVE IT