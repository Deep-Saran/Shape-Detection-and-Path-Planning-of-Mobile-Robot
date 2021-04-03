# Shape-Detection-and-Path-Planning-of-Mobile-Robot
## Description: 
Navigation is one of the key aspect in mobile robots. There are many techniques by which we can estimate the current position and make the robot to move to desired position. Using odometry we have made the Amigobot to move to some set of point, which are obtained from the image captured, which has an arbitrary shape drawn on it. This project is divided in two main parts namely image processing using OpenCv and odometry. In simple terms, an image with an arbitrary shape drawn is captured using the webcam of the laptop which is then supplied to the code which has an image processing which gives out the contour of that arbitrary shape. This contour consists of arrays of X & Y coordinates which are given to the odometry part where the robot divides them into series of goals and reaches them one after the other to form that shape. This shape can be observed in the Rviz of the simulator which maps the movement of the robot making the covered path of the robot visible.
## Libraries:
1. Cv2 -OpenCV
2. Numpy
