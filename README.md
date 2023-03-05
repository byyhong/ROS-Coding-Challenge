# ROS-Coding-Challenge
	The ros2 folder takes two input array in std_msgs/Int32MultiArray type and output a merged array in std_msgs/Int32MultiArray type.
# Run the folloing commands:
	colcon build --packages-select merge_arrays
	ros2 run merge_arrays merge_arrays_node
	ros2 topic pub /input/array1  std_msgs/msg/Int32MultiArray "{data: [3,9,18,20,30], layout: {dim:[]}}"
	ros2 topic pub /input/array1  std_msgs/msg/Int32MultiArray "{data: [1,4,8,12,36], layout: {dim:[]}}"
	
