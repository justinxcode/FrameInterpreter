import os
import shutil
from natsort import natsorted

filePath = 'D:\\GGST_DATA\\TEMP\\FRAMES'

outputFolder_INPUT = 'D:\\GGST_DATA\\TEMP\\FRAMES_REORDERED_INPUT'
outputFolder_NO_INPUT = 'D:\\GGST_DATA\\TEMP\\FRAMES_REORDERED_NO_INPUT'

files = os.listdir(filePath)

filesSorted = natsorted(files)

frame_count = 0

# iterate over the files
for i, filename in enumerate(filesSorted):

    original_file = os.path.join(filePath, filename)
    
    new_file = os.path.join(outputFolder_NO_INPUT, f'{frame_count}.png')  

    shutil.copy2(original_file, new_file)
    frame_count += 1

print('File renamer has finish!')

