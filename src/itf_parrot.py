#!/usr/bin/env python

import rospy
from std_msgs.msg import String

class Parrot():
    NODE_NAME = 'itf_parrot'

    def __init__(self):
        rospy.init_node(Parrot.NODE_NAME, log_level=rospy.INFO)
        rospy.Subscriber("itf_listen", String, self.callback)
        self.parrotpub = rospy.Publisher('itf_talk', String)
        self.lastsentence = ""

    def callback(self, data):
        if (data.data != "BADINPUT"):
            rospy.loginfo(rospy.get_caller_id()+": I heard %s, I will now repeat it.", data.data)
            self.parrotpub.publish(data.data)
            self.lastsentence = data.data
        else:
            rospy.loginfo(rospy.get_caller_id()+": I heard %s, I will not repeat it. Please try speaking more clearly.", data.data)


if __name__ == '__main__':
    rospy.loginfo("Starting {0}...".format(Parrot.NODE_NAME))
    parrot = Parrot()

    rospy.loginfo("{0} started, listening for text input to parrot on topic itf_listen...".format(Parrot.NODE_NAME))

    rospy.spin()

    rospy.loginfo("Stopping {0}...".format(Parrot.NODE_NAME))
    rospy.loginfo("{0} stopped.".format(Parrot.NODE_NAME))



