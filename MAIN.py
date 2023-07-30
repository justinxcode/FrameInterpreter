import os
import cv2
import time

from InputBuilder import InputBuilder
start_time = time.time()

currentResolution = 1440
builder = InputBuilder(currentResolution)


#sourcePath = 'D:\\GGST_DATA\\RIPPER_REFERENCE_DATA\\ICON_REFERENCE_FRAMES\\'
sourcePath = 'D:\\GGST_DATA\\RIPPER_REFERENCE_DATA\\TEST_FRAMES\\'
sourceName = 'ALL_TEN.png'


sourceImage = cv2.imread(sourcePath + sourceName)

returned = builder.position_one_input(sourceImage)

end_time = time.time()


#print(returned)


elapsed_time_ms = (end_time - start_time) * 1000
print(f'Elapsed time for this loop: {elapsed_time_ms}ms')


new_size = (1280, 720)
resized_image = cv2.resize(sourceImage, new_size)
cv2.imshow('debug_image', resized_image)
cv2.waitKey(0)
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