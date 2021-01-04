# ----------------------------------------- IMPORTANT INFORTMATION -------------------------------------------------------
# In these practice problems, questions will be commented out by default. When you work on a problem, uncomment the relevant code
# by selecting the lines and pressing CTRL + / (Windows) or CMD + / (Mac). 
# For example, for problem 0, we select from PROBLEM 0 START to PROBLEM 0 END
# Try it below


# # ---------- PROBLEM 0 START ----------
# print('hello world!')
# # ---------- PROBLEM 0 END ----------


# When you are finished with the problem, run it to make sure the output matches what you expect. Then, re-comment that problem 
# by using the same method and move on to the next problem! 


# ---------------------------------------- PROBLEM 1 START ----------------------------------------
# Start off by importing the OpenCV library.
# ---------- SOLUTION GOES HERE ----------
import cv2
# ----------------------------------------
# Now, let's load an image into Python. Use dog.jpg that is included in this folder. You can search up "cv2.imread" for reference. 
# Use the variable img to store it.
# To make sure you've loaded the image correctly, the code below it shows the image in your variable in a new window. The window closes when you press anything in your keyboard. 
img = 0


cv2.imshow("window", img)
cv2.waitKey()
cv2.destroyAllWindows()
# ---------------------------------------- PROBLEM 1 END ----------------------------------------


# ---------------------------------------- PROBLEM 2 START ----------------------------------------
# With the same image you've loaded in, convert it into grayscale and store it in the below variable. 
# Reference: cv2.cvtColor
gray_img = 0

# ---------------------------------------- PROBLEM 2 END ----------------------------------------


# ---------------------------------------- PROBLEM 3 START ----------------------------------------
# Now, let's perform a Gaussian blur. This smooths out any noise or other weird stuff in the image.
# Doing this helps the computer not get caught up on random dark or light pixels. 
# Reference: cv2.GaussianBlur
blur = cv2.GaussianBlur(gray_img, (3, 3), 0)

# ---------------------------------------- PROBLEM 3 END ----------------------------------------


# ---------------------------------------- PROBLEM 4 START ----------------------------------------
# Next we'll execute edge detection on the image. This one is really cool, so make sure to look at the result of this step!
# Reference: cv2.Canny()
edge = cv2.Canny(blur, 100, 200)

cv2.imshow("window", edge)
cv2.waitKey()
cv2.destroyAllWindows()

# We're almost done with the pipeline! Here's a freebie, no need to change this code! Be sure to read up on the "cv2.morphologyEx()" method.
import numpy as np
kernel = np.ones((3, 3))
morph = cv2.morphologyEx(edge, cv2.MORPH_CLOSE, kernel, iterations=1)

cv2.imshow("window", morph)
cv2.waitKey()
cv2.destroyAllWindows()
# ---------------------------------------- PROBLEM 4 END ----------------------------------------


# ---------------------------------------- PROBLEM 5 START ----------------------------------------
# Last thing to do is find contours. Search up "cv2.findContours" and fill in the blanks denoted by underscores _____.

# cv2.findContours looks for strings of continuous white pixels, hence the name "contour." 
# The variable "contours" is a list of all the contours that were found in the source image. 

# Fill in the blank for the source image. Remember, we want the most processed version of the image that we have so far. 
contours, hierarchy = cv2.findContours(_______, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# Here we'll be drawing rectangles around the contours that the computer finds onto the original image.  
for c in contours:
    # This skips a contour if the area of the contour is not within a certain threshold.
    # Fill in the blank for the minimum area to see if you can get rectangles around just the dog's eyes!
    if cv2.contourArea(c) <= ______ or cv2.contourArea(c) >= 6000:
        continue
    # For each contour in the list of contours, we get the position and the size of a rectangle around that contour. 
    x, y, w, h = cv2.boundingRect(c)
    # Then, we draw that rectangle using the original image as a source. 
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Now see what came out of that by using cv2.imshow() to show the original image!
cv2.imshow("window", img)
cv2.waitKey()
cv2.destroyAllWindows()
# ---------------------------------------- PROBLEM 5 END ----------------------------------------