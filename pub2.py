#!/usr/bin/env python3
import rospy
from std_msgs.msg import String


def talker_pub2():
    rospy.init_node("pub_node_2", anonymous=True)
    pub = rospy.Publisher("CSE2034", String, queue_size=10)
    rate = rospy.Rate(1)
    i = 0
    while not rospy.is_shutdown():
        i += 1
        _str = str(i) + " Topic name: \CSE2034"
        rospy.loginfo(_str)
        pub.publish(_str)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker_pub2()
    except rospy.ROSInterruptException:
        pass
