#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32


def print_data(data: Int32):
    rospy.loginfo("Number of packets encrypted: " + str(data.data))


def listener():
    rospy.init_node("final_sub", anonymous=True)
    rospy.Subscriber("xyz", Int32, print_data)
    rospy.spin()


if __name__ == "__main__":
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
