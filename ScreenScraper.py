import os
import cv2
from IconFinder import IconPositions

pos = IconPositions()

pathName = 'D:\\GGST_DATA\\RIPPER_REFERENCE_DATA\\UNSORTED\\'

# STILL NEED
# FAULTLESS_DEFENSE_FADE.png
# ROMAN_CANCEL_FADE.png

# use listdir to get all files in the directory
files_in_directory = os.listdir(pathName)

# iterate over each file in the directory
for fileName in files_in_directory:
    # join the directory path and file name
    full_path = os.path.join(pathName, fileName)
    # check if it is a file, not a directory
    if os.path.isfile(full_path):
        # check if the file is a .jpg file
        if fileName.endswith('.png'):
            # print the file name
            image = cv2.imread(pathName + fileName)
            sourceROI = pos.position_one_output(image)
            cv2.imwrite('D:\\GGST_DATA\\RIPPER_REFERENCE_DATA\\ICONS\\' + fileName, sourceROI)

print('All icons ripped!')




#cv2.imwrite('D:\\GGST_DATA\\RIPPER_REFERENCE_DATA\\ICONS\\' + imageName, sourceROI)

#cv2.imshow('ICON', sourceROI)
#cv2.waitKey(0)
#cv2.destroyAllWindows()