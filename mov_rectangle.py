#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist


def mov_rectangle():
    rospy.init_node("mov_reactangle", anonymous=True)
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    rate = rospy.Rate(10)
    vel = Twist()
    while not rospy.is_shutdown():
        vel.linear.x = 3
        pub.publish(vel)
        rospy.sleep(2)

        vel.linear.x = 0
        vel.linear.y = 6
        pub.publish(vel)
        rospy.sleep(2)

        vel.linear.y = 0
        vel.linear.x = -3
        pub.publish(vel)
        rospy.sleep(2)

        vel.linear.x = 0
        vel.linear.y = -6
        pub.publish(vel)
        rospy.sleep(2)

        vel.linear.x = 0
        vel.linear.y = 0
        vel.linear.z = 0
        pub.publish(vel)
        rate.sleep()


if __name__ == '__main__':
    try:
        mov_rectangle()
    except rospy.ROSInterruptException:
        pass
