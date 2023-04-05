# ROS-Coding-Challenge
The ros2 folder takes two input array in std_msgs/Int32MultiArray type and output a merged array in std_msgs/Int32MultiArray type. 

For some reason git thinks the src file is a submodule, and I wasn't able to turn the src folder back into a folder after trying git rm --cache src and deleting the .git directory in the src directory. Therefore after cloning the project, you need to run the folloing commands

	rm -rf ros2_ws/src
	mv src ros2_ws/src

The Approach I took on this project was to create two subscriber and one publisher in one node. The two subscriber are responsible for getting the message from the two topics for input, then we can merge the two input arrays and turn it into a new one. 
# Run the folloing commands:
	colcon build --packages-select merge_arrays
	ros2 run merge_arrays merge_arrays_node
	ros2 topic pub /input/array1  std_msgs/msg/Int32MultiArray "{data: [3,9,18,20,30], layout: {dim:[]}}"
	ros2 topic pub /input/array2  std_msgs/msg/Int32MultiArray "{data: [1,4,8,12,36], layout: {dim:[]}}"
	
