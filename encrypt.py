#!/usr/bin/env python3
import rospy
from std_msgs.msg import String


def caeser(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result


def encrypt(data: String):
    pub = rospy.Publisher("xyz", String, queue_size=3)
    rospy.loginfo(f"Pre Encrypted message -> {data.data}")
    encrypted_string = caeser(data.data, 3)
    rospy.loginfo(f"Encrypted message -> {encrypted_string}")
    rospy.sleep(1)
    pub.publish(encrypted_string)


def listener():
    rospy.init_node("encrypt", anonymous=True)
    rospy.Subscriber("ABC", String, encrypt)
    rospy.spin()


if __name__ == "__main__":
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
