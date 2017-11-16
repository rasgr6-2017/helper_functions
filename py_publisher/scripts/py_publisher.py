#!/usr/bin/env python
import roslib
import sys
import rospy
from geometry_msgs.msg import Polygon
from geometry_msgs.msg import Point32


if __name__ == '__main__':
	
    pub = rospy.Publisher('target_point', Polygon, queue_size=1)
    rospy.init_node('target_send_tester', anonymous=True)
    rate = rospy.Rate(1) # 10hz
    target_msg = Polygon()
    target_msg.points = [Point32(x=10,y=84), Point32(x=105,y=106)]
    while not rospy.is_shutdown():
        pub.publish(target_msg)
        rate.sleep()
