import numpy as np
import cv2 
#For windows users import this:
from PIL import ImageGrab

#Four character code object for video writer
code = cv2.VideoWriter_fourcc(*'XVID')
#Video writer object
out = cv2.VideoWriter("Output.mkv",code,5.0,(1366,786))

while True:
	#Capture the computer Screen
	img = ImageGrab.grab()
	#Convert image to numpy array
	img_np = np.array(img)
	#Convert image from BGR to RGB
	frame = cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)
	#Show image on OpenCV frame
	cv2.imshow("screen",frame)
	#Write fame to video writer
	out.write(frame)

	if cv2.waitKey(1)==27:
		break


out.release()
cv2.destroyAllWindow()