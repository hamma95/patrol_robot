#!/usr/bin/env python

from __future__ import print_function
import rospy
from smach import State,StateMachine
from time import sleep


class One(State):
	"""docstring for ClassName"""
	def __init__(self):
		State.__init__(self,outcomes=['success'])

	def execute(self, userdata):
		print("one")
		sleep(1)
		return 'success'


class Two(State):
	"""docstring for ClassName"""
	def __init__(self):
		State.__init__(self,outcomes=['success'])

	def execute(self, userdata):
		print("two")
		sleep(1)
		return 'success'




if __name__ == '__main__':



	sm=StateMachine(outcomes=['success'])
	with sm:
		StateMachine.add('one',One(),transitions={'success':'two'})
		StateMachine.add('two',Two(),transitions={'success':'one'})

	sm.execute()


	