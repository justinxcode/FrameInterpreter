import cv2

filePath = 'D:\\GGST_DATA\\TEMP\\VIDEOS\\'
fileName = 'chipp1_input.avi'
videoPath =  filePath + fileName

frame_count = 0

# Open the video file
cap = cv2.VideoCapture(videoPath)

# Check if video opened successfully
if not cap.isOpened(): 
    print("Error opening video file")

# Read until video is completed
while(cap.isOpened()):
    
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret:

        # Save the resulting frame to png file
        cv2.imwrite(f'D:\\GGST_DATA\\TEMP\\FRAMES\\{frame_count}.png', frame)
        frame_count += 1  # increment frame count

    # Break the loop if no frame is received
    else: 
        break

# After the loop release the cap object
cap.release()
print('Video has finish!')
