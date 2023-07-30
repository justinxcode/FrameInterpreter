import os
import cv2
from IconFinder import IconPositions

pos = IconPositions()

pathName = 'D:\\GGST_DATA\\RIPPER_REFERENCE_DATA\\ICON_REFERENCE_FRAMES\\'

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
            if fileName == 'FAULTLESS_DEFENSE_FADE.png':
                sourceROI = pos.position_two_output(image)
            else:
                sourceROI = pos.position_one_output(image)

            cv2.imwrite('D:\\GGST_DATA\\RIPPER_REFERENCE_DATA\\ICONS\\' + fileName, sourceROI)

print('All icons ripped!')