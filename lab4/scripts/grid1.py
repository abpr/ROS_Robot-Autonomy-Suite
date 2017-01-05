#!/usr/bin/env python
#import all required libraries
import roslib
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist,Vector3
import random
import math
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Quaternion
from geometry_msgs.msg import Pose, PoseArray
from rospy_tutorials.msg import Floats
from rospy.numpy_msg import numpy_msg
import numpy
from visualization_msgs.msg import Marker

class Grid_cell:
	x = 0.0
	y = 0.0
	theta = 0.0
	tag = 0
	#discretization value = 90 degrees
	#so the robot can be in one of the 4 zones
	zone = 0
	probability = 0.0

	def __init__(self,x,y,theta,tag):
		self.x = x
		self.y = y
		self.theta = theta
		self.tag = tag
		self.zone = round(theta/90)
		#print zone


if __name__=='__main__':
	try:
		tag0 = Grid_cell(1.25,5.25,0,1)
		tag1 = Grid_cell(1.25,3.25,0,1)
		tag2 = Grid_cell(1.25,1.25,0,1)
		tag3 = Grid_cell(4.25,1.25,0,1)
		tag4 = Grid_cell(4.25,3.25,0,1)
		tag5 = Grid_cell(4.25,5.25,0,1)
		initial_pose = Grid_cell(12,28,200.52,0)
		#create the grid
		#w,h = 35,35
		#total_grid = [[Grid_cell(0,0,0,0) for x in range(w)] for y in range(h)]
		#print str(total_grid)
		#total_grid[]
		#grid = Grid_cell(5,10,315,0)
		#print grid.x
		#print grid.zone
		#rospy.spin()

	except rospy.ROSInterruptException:
		pass

#doubt1
