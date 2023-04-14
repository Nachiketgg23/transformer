# #!/usr/bin/env python3
# import rospy
# from std_msgs.msg import String


# def this_listner(data: str):
#     rospy.loginfo("Fuck, %s", data.data)


# def listner_sub1():
#     rospy.init_node("sub", anonymous=True)
#     rospy.Subscriber("ABC", String, this_listner)
#     rospy.spin()


# if __name__ == '__main__':
#     try:
#         listner_sub1()
#     except rospy.ROSInterruptException:
#         pass


#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
from std_msgs.msg import String
i = 0


def num(data):
    global i
    pub = rospy.Publisher("num_pub", Int32, queue_size=10)
    i += 1
    pub.publish(len(data.data))
    rospy.loginfo("Published Number of packets: " + str(i))


def listener():
    rospy.init_node("num_publisher", anonymous=True)
    rospy.Subscriber("xyz", String, num)
    rospy.spin()


if __name__ == "__main__":
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
