import cv2
import time
from IconFinder import IconPositions
from IconMatch import IconMatch
start_time = time.time()

pos = IconPositions()
match = IconMatch()
currentResolution = 1440

#sourcePath = 'D:\\GGST_DATA\\RIPPER_REFERENCE_DATA\\ICON_REFERENCE_FRAMES\\'
sourcePath = 'D:\\GGST_DATA\\RIPPER_REFERENCE_DATA\\TEST_FRAMES\\'
sourceName = 'MANY.png'
sourceImage = cv2.imread(sourcePath + sourceName)


sourceROI = pos.position_seven_output(sourceImage)
match.find_match(sourceROI, currentResolution)

#position nine coordinate - 0 - best value - 
#position ten coordinate - 0 - best value - 


end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f'Elapsed time for this loop: {elapsed_time_ms}ms')
#THIS IS FOR DEBUG - LEAVE IT

debug_image = sourceROI
new_width = debug_image.shape[1] * 20
new_height = debug_image.shape[0] * 20
new_size = (new_width, new_height)
resized_image = cv2.resize(debug_image, new_size)
cv2.imshow(f'debug_image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#THIS IS FOR DEBUG - LEAVE IT