#!/usr/bin/env python

import rospy
from sbot_msg.msg import Position2D

def talker():
	pub = rospy.Publisher('targetposition', Position2D, queue_size =10)
	rospy.init_node('talker', anonymous=True)
	rate = rospy.Rate(1)
	outputData = Position2D()
	myX = 0
	myY = 60
	while not rospy.is_shutdown():
		outputData.x = myX
		outputData.y = myY

		# myX = myX+5
		# if (myX > 43):
		# 	myX = -43
		 	# myY = myY + 5
			# if (myY > 43):
			# 	myY = -43

		#rospy.loginfo(outputData)
		pub.publish(outputData)
		rate.sleep()

	# outputData.x = myX
	# outputData.y = myY

	# pub.publish(outputData)


if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass