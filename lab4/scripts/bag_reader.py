#!/usr/bin/env python
#import all required libraries
import roslib
import rospy
roslib.load_manifest('lab4')
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist,Vector3
import random
import math
import rosbag
from geometry_msgs.msg import Point, Quaternion


def bag_reader():
	motion_publisher = rospy.Publisher('Movements',Motion,queue_size=10)
	observation_publisher = rospy.Publisher('Observations',Observation,queue_size=10)
	bag = rosbag.Bag('grid.bag');
	motion_msg = Motion()
	observation_msg = Observation()
	for topic,timetag,msg in bag.read_messages(topics = ['Observations','Movements']):
		print msg
		print '-->topic: ',topic
		print '-->time tag:, ',timetag
		if(topic == 'Movements'):
			motion_msg.timeTag = timetag
			motion_msg.rotation1 = msg.rotation1
			motion_msg.translation = msg.translation
			motion_msg.rotation2 = msg.rotation2
			motion_publisher.publish(motion_msg)
		else:
			observation_msg.timeTag = timetag
			observation_msg.tagNum = msg.tagNum
			observation_msg.range = msg.range
			observation_msg.bearing = msg.bearing
			observation_publisher.publish(observation_msg)

#create the main block
if __name__=='__main__':
	try:
		bag_reader()
	except rospy.ROSInterruptException:
		pass

