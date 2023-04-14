#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
arr = ["Rohil", "is", "a", "Bitch"]


def talker():
    rospy.init_node("pub1", anonymous=True)
    pub = rospy.Publisher("ABC", String, queue_size=10)
    rate = rospy.Rate(10)
    while not rospy.is_shutown():
        for i in arr:
            str = i
            rospy.loginfo("Published -> " + str)
            pub.publish(str)
            rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
