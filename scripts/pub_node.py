#!/usr/bin/env python
#-*- coding:utf-8 -*-
import rospy
import sys

from std_msgs.msg import Int32

def talker():

	pub = rospy.Publisher('finish', Int32, queue_size=10)

	rate = rospy.Rate(1)

	pub_msg = Int32()
	
	count = 1

	while not rospy.is_shutdown():
		pub_msg.data = count
		pub.publish(pub_msg)
		rospy.loginfo(rospy.get_caller_id() + '/ Publish : %d' % pub_msg.data)

		rate.sleep()

if __name__ == '__main__':
	rospy.init_node('rfid', anonymous=True)

	try:
		talker()

	except rospy.ROSInterruptException:
		sys.exit(0)