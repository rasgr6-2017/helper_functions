#!/usr/bin/env python
import numpy as np
from matplotlib import pyplot as plt
import rospy
from std_msgs.msg import Float32MultiArray
import message_filters

def callback(msg):
    global count
    global state
    global data_list1
    global data_list2
    global data_list3
    global data_list4
    global data_list5
    global data_list6
    
    count += 1
    if count%2 == 0:
        i = 0
        while(i < 360):
            data_list1.append(msg.data[i])
            i += 1
        while(i < 720):
            data_list2.append(msg.data[i])
            i += 1
        while(i < 1080):
            data_list3.append(msg.data[i])
            i += 1
        while(i < 1440):
            data_list4.append(msg.data[i])
            i += 1
        while(i < 1440 + 8):
            data_list5.append(msg.data[i])
            i += 1
            data_list6.append(msg.data[i])
            i += 1
        direction = msg.data[i]
        
        # x = range(len(data_list1))
        x = np.arange(-179.0, 181.0, 1.0)

        theta = ( np.pi/180.0 )*x
        direction = (direction - 180) * ( np.pi/180.0 )
        d5 = np.array(data_list5)
        d6 = (np.array(data_list6))*( np.pi/180.0 )
        print d6
        print d5

        fig = plt.figure(1)
        ax2 = fig.add_axes([0.1,0.1,0.8,0.8],polar=True)
        offset = 1.2
        ax2.plot(theta, data_list1, 'r', theta, data_list2, 'b', theta, data_list3, 'm', theta, data_list4, 'k', lw=1.0)
        ax2.plot(d6, d5, 'bs', lw=4)
        ax2.plot(direction, 0.5, 'ro', lw=4)
        ax2.set_rmax(offset)
        plt.ion()
        plt.show()
        plt.pause(0.12)
        plt.clf()

        data_list1 = []
        data_list2 = []
        data_list3 = []
        data_list4 = []
        data_list5 = []
        data_list6 = []
        
    
    
    """
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
    """


def listener():
    
    rospy.init_node('signal_visualizor', anonymous=True)
    # rospy.Subscriber("/motorcontrol/signal_packup", Float32MultiArray, callback)
    rospy.Subscriber("/histogram", Float32MultiArray, callback, queue_size=1)
    # sub_2 = rospy.Subscriber("/histogram_2", Float32MultiArray, callback_second)
    # sub_3 = rospy.Subscriber("/histogram_3", Float32MultiArray, callback_third)
    
    # spin() simply keeps python from exiting until this node is stopped

    rospy.spin()

if __name__ == '__main__':
    count = 0
    state = 0
    data_list1 = []
    data_list2 = []
    data_list3 = []
    data_list4 = []
    data_list5 = []
    data_list6 = []
    listener()
    

    """
    x = np.arange(0, 2.0, 0.05)
    data_list1 = np.ones(len(x)) - np.power(x, 0.1) * 0.933
    data_list3 = np.ones(len(x)) - np.power(x, 0.3) * 0.812
    data_list5 = np.ones(len(x)) - np.power(x, 0.5) * 0.707
    
    plt.figure(1)
    plt.plot(x, data_list1, 'ro',  x, data_list3, 'bs',  x,  data_list5,  'g^')
    plt.show()
    plt.pause(600)
    """

