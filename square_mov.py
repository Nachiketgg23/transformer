#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import radians


class Square:
    def __init__(self):
        rospy.init_node('square_turtle', anonymous=False)

        self.velocity_publisher = rospy.Publisher(
            '/turtle1/cmd_vel', Twist, queue_size=10)
        self.pose_subscriber = rospy.Subscriber(
            '/turtle1/pose', Pose, self.update_pose)

        self.pose = Pose()

    def update_pose(self, data):
        self.pose = data

    def move(self, linear_vel, angular_vel, duration):
        vel_msg = Twist()
        vel_msg.linear.x = linear_vel
        vel_msg.angular.z = angular_vel

        t0 = rospy.Time.now().to_sec()
        current_distance = 0
        rate = rospy.Rate(10)

        while current_distance < duration:
            self.velocity_publisher.publish(vel_msg)
            t1 = rospy.Time.now().to_sec()
            current_distance = linear_vel * (t1 - t0)
            rate.sleep()

        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)

    def rotate(self, angle):
        angular_speed = radians(45)
        relative_angle = radians(angle)

        vel_msg = Twist()
        vel_msg.linear.x = 0
        vel_msg.angular.z = angular_speed

        t0 = rospy.Time.now().to_sec()
        current_angle = 0
        rate = rospy.Rate(10)

        while current_angle < relative_angle:
            self.velocity_publisher.publish(vel_msg)
            t1 = rospy.Time.now().to_sec()
            current_angle = angular_speed * (t1 - t0)
            rate.sleep()

        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)

    def draw_square(self):
        self.move(1, 0, 3)  # move forward for 3 seconds
        self.rotate(90)     # rotate 90 degrees
        self.move(1, 0, 3)  # move forward for 3 seconds
        self.rotate(90)     # rotate 90 degrees
        self.move(1, 0, 3)  # move forward for 3 seconds
        self.rotate(90)     # rotate 90 degrees
        self.move(1, 0, 3)  # move forward for 3 seconds


if __name__ == '__main__':
    try:
        square = Square()
        square.draw_square()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
