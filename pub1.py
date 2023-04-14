#!/usr/bin/env python3
import rospy
from std_msgs.msg import String


def talker_pub1():
    rospy.init_node("pub_node_1", anonymous=True)
    # this is to create the node
    pub = rospy.Publisher("CSE3102", String, queue_size=10)
    # this is to create the publisher
    rate = rospy.Rate(1)
    # this sets the rate
    i = 0
    while not rospy.is_shutdown():
        i += 1
        _str = str(i) + " Topic name: \CSE3102"
        rospy.loginfo(_str)  # loginfo -> to print on the treminal
        pub.publish(_str)  # this function publishes to the publisher node
        rate.sleep()  # this sleeps after a while


if __name__ == '__main__':
    try:
        talker_pub1()
    except rospy.ROSInterruptException:
        pass
