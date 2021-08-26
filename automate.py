import pyautogui as gui
import numpy as np
import time
import cv2

def auto_canny(image, sigma=0.33):
	# compute the median of the single channel pixel intensities
	v = np.median(image)
	# apply automatic Canny edge detection using the computed median
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper)
	# return the edged image
	return edged

def Resize(image,w):
	
	height,width =  image.shape
	aspect_ratio = height/width
	new_height = int(w*aspect_ratio)
	resized_img = cv2.resize(image,(w,new_height))
	return (resized_img,new_height)


# Read the original image
img = cv2.imread(r"C:\Users\Joydip Dutta\Desktop\imgs\img1.jpg") 
# Convert to graycsale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blur the image for better edge detection
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 
# Apply Canny Edge Algo using optimal threshholds
edge = auto_canny(img_blur)
# Resize the edged image
w = 800
edge,h = Resize(edge,w)

#automate Ms paint
gui.keyDown('win')
gui.press('r')
gui.keyUp('win')
time.sleep(2)
gui.write('MsPaint')
gui.press('enter')
time.sleep(2)

gui.click(808,87)    		 # coordinates of fill icon
gui.click(268,70)    		 # coordinates of background colour location
gui.click(237,221) 	 		 # coordinates on a random location on the canvas for filling	
gui.click(242,104)	 		 # coordinates for selecting the eraser tool
gui.click(638,94)	 		 # coordinates for size dropdown tool
gui.moveTo(639,125)  		 # coordinates of eraser size
gui.click(button='right')
gui.click(628,128,clicks=2)  # coordinates of lowest eraser size 
gui.move(8,164)
         
# relative coordinates for the image to be drawn in the canvas         
x0,y0 = 237,221          

# Threshhold value for considering edges
thresh = 104

#list for appending white pixel coordinates in the edged image for clicking 
coord=[]

for i in range(h):
	for j in range(w):
		if edge[i][j] >= thresh:
			coord.append((j,i))

# Clicking on desired edge coordinates to get the sketch
for cord in coord:
	gui.click(cord[0]+x0,cord[1]+y0)



