#!/usr/bin/env python
import roslib #roslib.load_manifest('teleop_twist_keyboard')
import rospy

from geometry_msgs.msg import Twist

import sys, select, termios, tty

"""program modified from Graylin Trevor Jay's teleop_keyboard_twist package"""


msg = """
Reading from the keyboard  and Publishing to /motor_controller/Twist!
---------------------------

anything else : stop

w : increase linear speed by 0.05
s : decrease linear speed by 0.05
a : increase angular speed by 0.05
d : decrease angular speed by 0.05

CTRL-C to quit
"""
speedBindings={
		'w':(0.03, 0),
		's':(-0.03, 0),
		'a':(0, 0.4),
		'd':(0, -0.4),
	      }

def getKey():
	tty.setraw(sys.stdin.fileno())
	select.select([sys.stdin], [], [], 0)
	key = sys.stdin.read(1)
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
	return key


def vels(vel,ang):
	return "currently:\tspeed %s\tturn %s " % (vel,ang)

if __name__=="__main__":
    	settings = termios.tcgetattr(sys.stdin)
	
	pub = rospy.Publisher('/motor_controller/twist', Twist, queue_size = 10)
	rospy.init_node('keyboard_twist')

	# set default value for the speed and 
	vel = rospy.get_param("~vel", 0.0)
	ang = rospy.get_param("~ang", 0.0)

	status = 0

	try:
		print msg
		print vels(vel,ang)
		while(1):
			key = getKey()
			print vels(vel,ang)
			if key in speedBindings.keys():
				vel = vel + speedBindings[key][0]
				ang = ang + speedBindings[key][1]

				print vels(vel, ang)
				if (status == 29):
					print msg
				status = (status + 1) % 30
			else:
				# this is ctrl + C
				if (key == 'q'):
					break
			# roughly set a maximum speed
			if vel > 0.7:
				vel = 0.7
			if vel < -0.7:
				vel = -0.7
			if ang > 1:
				ang = 1
			if ang < -1:
				ang = -1

			twist = Twist()
			twist.linear.x = vel
			twist.angular.z = ang
			print vels(vel,ang)
			pub.publish(twist)
		
		vel = 0
		ang = 0

	except Exception, e:
		print e

	finally:
		twist = Twist()
		twist.linear.x = vel
		twist.angular.z = ang
		pub.publish(twist)

    	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)


