#!/usr/bin/env python
import rospy
import actionlib
from smach import State,StateMachine
from move_base_msgs.msg import MoveBaseAction,MoveBaseGoal




waypoints = [
['one', (2.1, 2.2), (0.0, 0.0, 0.0, 1.0)],
['two', (6.5, 4.43), (0.0, 0.0, -0.984047240305, 0.177907360295)]
]


class patrol(State):
	"""docstring for patrol"""
	def __init__(self,pose):
		State.__init__(self,outcomes=['success'])
		
		self.client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
		self.client.wait_for_server()


		self.goal = MoveBaseGoal()
		self.goal.target_pose.header.frame_id='map'
		self.goal.target_pose.pose.position.x=pose[1][0]
		self.goal.target_pose.pose.position.y=pose[1][1]
		self.goal.target_pose.pose.position.z=0
		self.goal.target_pose.pose.orientation.x=pose[2][0]
		self.goal.target_pose.pose.orientation.y=pose[2][1]
		self.goal.target_pose.pose.orientation.z=pose[2][2]
		self.goal.target_pose.pose.orientation.w=pose[2][3]


	def execute(self,userdata):
		self.client.send_goal(self.goal)
		self.client.wait_for_result()
		return 'success'

if __name__=='__main__':
	rospy.init_node('patrol')
	sm=StateMachine(outcomes=['success'])

	with sm:
		for i,pose in enumerate(waypoints):
			StateMachine.add(pose[0],patrol(pose),transitions={'success': waypoints[(i+1)%len(waypoints)][0]})
	


	sm.execute()

	











