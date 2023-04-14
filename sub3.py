#!/usr/bin/env python3
import rospy
from std_msgs.msg import String


def this_listner(data: str):
    rospy.loginfo("I'm Sub3 and listening to %s", data.data)


def listner_sub3():
    rospy.init_node("sub_node_3", anonymous=True)
    rospy.Subscriber("CSE2034", String, this_listner)
    rospy.spin()


if __name__ == '__main__':
    try:
        listner_sub3()
    except rospy.ROSInterruptException:
        pass
