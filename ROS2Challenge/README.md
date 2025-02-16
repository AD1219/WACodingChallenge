# Merge Arrays in ROS2

How I ran my project: 
- In my original terminal:
  - colcon build --packages-select merge_arrays
  - ros2 run merge_arrays merge_arrays_node
- Next, I opened two more new terminals, one for each array to merge
- In each terminal I first ran: 
  - source install/setup.bash
  - ros2 topic pub /input/array1 std_msgs/Int32MultiArray "{data: [0, 2, 4, 6, 8]}"
  - ros2 topic pub /input/array1 std_msgs/Int32MultiArray "{data: [1, 3, 5, 7, 9]}"
- Finally, I got my output stream in the original terminal

I am unsure if this is the right way to solve the challenge, but I enjoyed my first experience with ROS2 
and I am very willing to learn more!
