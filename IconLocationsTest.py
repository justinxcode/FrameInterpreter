import cv2
from InputBuilder import InputBuilder
from IconFinder import IconPositions

builder = InputBuilder()
pos = IconPositions()

sourcePath = 'D:\\GGST_DATA\\RIPPER_REFERENCE_DATA\\TEST_FRAMES\\ALL_TEN.png'
sourceImage = cv2.imread(sourcePath)

#row_one = builder.row_one_position_one_input(sourceImage)
#print(f'Row one data: {row_one}')
#row_two = builder.row_two_position_one_input(sourceImage)
#print(f'Row two data: {row_two}')
#row_three = builder.row_three_position_one_input(sourceImage)
#print(f'Row two data: {row_three}')

row_four = builder.row_four_position_one_input(sourceImage)
print(f'Row two data: {row_four}')



debug_image = pos.row_four_position_one_output(sourceImage)






new_width = debug_image.shape[1] * 20
new_height = debug_image.shape[0] * 20
new_size = (new_width, new_height)
resized_image = cv2.resize(debug_image, new_size)
cv2.imshow('debug_image', resized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()