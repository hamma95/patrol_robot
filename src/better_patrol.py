#!/usr/bin/env python
import rospy
from smach import StateMachine
from smach_ros import SimpleActionState
from move_base_msgs.msg import MoveBaseAction,MoveBaseGoal




waypoints = [
['one', (2.1, 2.2), (0.0, 0.0, 0.0, 1.0)],
['two', (6.5, 4.43), (0.0, 0.0, -0.984047240305, 0.177907360295)]
]




if __name__=='__main__':



	rospy.init_node('patrol')
	sm=StateMachine(['succeeded','aborted','preempted'])
	with sm:
		for i,pose in enumerate(waypoints):
			goal_pose = MoveBaseGoal()
			goal_pose.target_pose.header.frame_id='map'
			goal_pose.target_pose.pose.position.x=pose[1][0]
			goal_pose.target_pose.pose.position.y=pose[1][1]
			goal_pose.target_pose.pose.position.z=0
			goal_pose.target_pose.pose.orientation.x=pose[2][0]
			goal_pose.target_pose.pose.orientation.y=pose[2][1]
			goal_pose.target_pose.pose.orientation.z=pose[2][2]
			goal_pose.target_pose.pose.orientation.w=pose[2][3]
			StateMachine.add(pose[0],SimpleActionState('move_base',MoveBaseAction,goal=goal_pose),transitions={'succeeded':waypoints[(i+1)%len(waypoints)][0]})

	sm.execute()
