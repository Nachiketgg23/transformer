#!/usr/bin/env python3
import rospy
from std_msgs.msg import String


def this_listner(data: str):
    rospy.loginfo("I'm Sub1 and listening to %s", data.data)


def listner_sub1():
    rospy.init_node("sub_node_1", anonymous=True)
    rospy.Subscriber("CSE3102", String, this_listner)
    rospy.spin()


if __name__ == '__main__':
    try:
        listner_sub1()
    except rospy.ROSInterruptException:
        pass
