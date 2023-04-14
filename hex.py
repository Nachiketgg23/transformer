#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import radians, degrees

angles = [60.0, 120.0, 180.0, -120.0, -60.0, 0.0]
count = 0
stop = 300


def rrad(x: float):
    return round(radians(x), 2)


def pub_callback(pose: Pose):
    global count, stop, angles
    ang = round(pose.theta, 2)
    x = round(pose.x, 2)
    y = round(pose.y, 2)
    vel = Twist()

    count += 1
    if count >= stop:
        vel.linear.x = 0
        vel.angular.z = rrad(5.0)
        stop_ang = rrad(angles[0])
        if ang == stop_ang:
            rospy.loginfo(f'stop ang={angles[0]}')
            stop_ang = angles.pop(0)
            angles.append(stop_ang)
            vel.angular.z = 0.0
            count = 0
    else:
        vel.linear.x = 0.5
        vel.angular.z = 0.0

    rospy.loginfo(f'T2-> x={x}, y={y}, theta={degrees(ang)}, cntr={count}')
    pub.publish(vel)


if __name__ == '__main__':
    try:
        rospy.init_node("mov_star", anonymous=True)
        pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
        sub = rospy.Subscriber('/turtle1/pose', Pose, callback=pub_callback)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
