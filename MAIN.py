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
   
pathName = 'D:\\GGST_DATA\\BATTLE_DATA_FRAMES\\SOL_KY\\ROUND_THREE_WIN\\FIGHT_ONE\\'

files_in_directory = os.listdir(pathName)

#results = [None]*3
#old_result_one = [None]*3
#old_result_two = [None]*3
#old_result_three = [None]*3

neutral = 'NEUTRAL'
all_neutral = [neutral] * 10
results = [neutral] * 3
old_result_one = all_neutral
old_result_two = all_neutral

for fileName in files_in_directory:

    full_path = os.path.join(pathName, fileName)
    image = cv2.imread(pathName + fileName)

    # Store current results
    #results[0] = builder.row_one_position_one_input(image)
    #results[1] = builder.row_two_position_one_input(image)
    #results[2] = builder.row_three_position_one_input(image)
#
    #print('FULL SET BELOW')
    #print(f'New Result 1: {results[1]}')
    #print(f'Old Result 1: {old_result_one}')
    #print(f'New Result 2: {results[2]}')
    #print(f'Old Result 2: {old_result_two}')
#
    #if old_result_one == results[1] and old_result_two == results[2]:
    #    output = results[0]
    #else:
    #    output = all_neutral
#
    #print(f'OUTPUT IS: {output}')
    ## Set old results with current ones
    #old_result_one = results[0]
    #old_result_two = results[1]


    test, _ = builder.get_input(image)

    print(test)
    #print(bool_list)
   
    new_size = (1280, 720)
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