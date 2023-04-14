#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist


def move_turtle_circle(linear_val, angular_val):
    rospy.init_node("trutle_move_circle", anonymous=True)
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    rate = rospy.Rate(10)
    vel = Twist()

    while not rospy.is_shutdown():
        vel.linear.x = linear_val
        vel.linear.y = 0
        vel.linear.z = 0

        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = angular_val

        pub.publish(vel)
        rate.sleep()


if __name__ == '__main__':
    try:
        move_turtle_circle(10.0, 12.5)
    except rospy.ROSInterruptException:
        pass
