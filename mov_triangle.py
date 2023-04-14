#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist


def mov_triangle():
    rospy.init_node("mov_triangle", anonymous=True)
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    rate = rospy.Rate(10)
    vel = Twist()

    while not rospy.is_shutdown():
        vel.linear.x = 4
        pub.publish(vel)
        rospy.sleep(2)

        vel.linear.x = -2
        vel.linear.y = 2
        pub.publish(vel)
        rospy.sleep(2)

        vel.linear.x = -2
        vel.linear.y = -2
        pub.publish(vel)
        rospy.sleep(2)

        vel.linear.x = 0
        vel.linear.y = 0
        vel.linear.z = 0
        pub.publish(vel)
        rate.sleep()


if __name__ == '__main__':
    try:
        mov_triangle()
    except rospy.ROSInterruptException:
        pass
