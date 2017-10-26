#!/usr/bin/env python
import numpy as np
from matplotlib import pyplot as plt
import rospy
from std_msgs.msg import Float32MultiArray

def callback(msg):
    global count
    global data_list1
    global data_list2
    global data_list3
    global data_list4
    global data_list5
    global data_list6
    # color = ['bo',  'go',  'ro',  'ko',  'yo',  'co']
    if count % 2 == 0:
        for i in range(6):
            rospy.loginfo(msg.data[i])
            if i == 0:
                data_list1.append(msg.data[i])
            if i == 1:
                data_list2.append(-msg.data[i])
            if i == 2:
                data_list3.append(msg.data[i])
            if i == 3:
                data_list4.append(-msg.data[i])
            if i == 4:
                data_list5.append(msg.data[i])
            if i == 5:
                data_list6.append(-msg.data[i])
            # plt.plot( count*0.02, msg.data[i*2], color[i*2])
            # plt.axis("equal")
            # plt.draw()
        
        # plt.pause(0.01)
        rospy.loginfo("-----------------")

    if count == 600:
        x = range(len(data_list1))
        # circle for measurement, triangle for control output, square for reference input
        plt.figure(1)
        plt.subplot(211)
        plt.plot(x, data_list1, 'ro',  x, data_list3, 'bs',  x,  data_list5,  'g^')

        plt.subplot(212)
        plt.plot(x, data_list2, 'ro',  x, data_list4, 'bs',  x,  data_list6,  'g^')
        plt.show()
        plt.pause(600)
    count += 1

def listener():
    
    rospy.init_node('signal_visualizor', anonymous=True)
    rospy.Subscriber("/motorcontrol/signal_packup", Float32MultiArray, callback)
    
    plt.ion()
    plt.show()

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    count = 0
    data_list1 = []
    data_list2 = []
    data_list3 = []
    data_list4 = []
    data_list5 = []
    data_list6 = []
    listener()

