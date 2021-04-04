# Shape-Detection-and-Path-Planning-of-Mobile-Robot
Contributers- Deep Saran Masanam, Jaji Bala Jyothika Pamarthi and Anna Gallo

## Description: 
Navigation is one of the key aspect in mobile robots. There are many techniques by which we can estimate the current position and make the robot to move to desired position. Using odometry we have made the Amigobot to move to some set of point, which are obtained from the image captured, which has an arbitrary shape drawn on it. This project is divided in two main parts namely image processing using OpenCv and odometry. In simple terms, an image with an arbitrary shape drawn is captured using the webcam of the laptop which is then supplied to the code which has an image processing which gives out the contour of that arbitrary shape. This contour consists of arrays of X & Y coordinates which are given to the odometry part where the robot divides them into series of goals and reaches them one after the other to form that shape. This shape can be observed in the Rviz of the simulator which maps the movement of the robot making the covered path of the robot visible.
## Libraries:
1. cv2 -OpenCV
2. numpy
3. matplotlib
## Directions:
1. Run PathGenerator.py. Two ways you can give image as either through the webcam or either by providing the path to script to generate the coordinates.
2. These coordinates are published via ROS to Amigobot.
