#!/usr/bin/env python

from __future__ import print_function
import rospy
from smach import State,StateMachine
from time import sleep


class Drive(State):
	"""docstring for Drive"""
	def __init__(self, distance):
		State.__init__(self,outcomes=['success'])
		self.distance = distance

	def execute(self,userdata):

		print("driving at {} m/s".format (self.distance))
		sleep(1)
		return 'success'




class Turn(State):
	"""docstring for Turn"""
	def __init__(self, angle):
		State.__init__(self,outcomes=['success'])
		self.angle = angle

	def execute(self,userdata):

		print("turning at {} degrees".format (self.angle))
		sleep(1)
		return 'success'

def polygon(sides):
	polygon = StateMachine(outcomes=['success'])
	with polygon :
		for i in xrange(sides-1):
			StateMachine.add('side{0}'.format(i+1),Drive(1),transitions={'success':'turn{0}'.format(i+1)})
			StateMachine.add('turn{0}'.format(i+1),Turn(360/sides),transitions={'success':'side{0}'.format(i+2)})

		StateMachine.add('side{0}'.format(sides),Drive(1),transitions={'success':'success'})

	return polygon





if __name__=='__main__':
	triangle=polygon(3)
	square=polygon(4)

	shapes=StateMachine(outcomes=['success'])
	with shapes:
		StateMachine.add('triangle',triangle,transitions={'success':'square'})
		StateMachine.add('square',square,transitions={'success':'triangle'})


	shapes.execute()



