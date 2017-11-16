#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>
#include "geometry_msgs/Twist.h"
#include "std_msgs/Float32MultiArray.h"

#define TARGET_NUMBER 28

int main(int argc, char **argv)
{

  ros::init(argc, argv, "simple_publisher");

  ros::NodeHandle n;

  geometry_msgs::Twist twist_msg;
  std_msgs::Float32MultiArray tar_array;

  // double tar_x[21] = {0.74, 1.52,  1.72,   1.6,  1.48,  0.92, 0.04,   -0.2, -0.14, 0.02,  0.3,   0.54,   0.4,  0.36, 0.52,  0.96,  1.22,  1.62,  1.76,  1.64, 1.14};
  // double tar_y[21] = {0.0, -0.22, -0.94, -1.64, -1.92, -1.94, -1.96, -1.74, -0.72, -0.4, -0.38, -0.58, -0.96, -1.34, -1.42, -1.3, -1.32, -1.44, -1.04, -0.38, -0.2};

  double tar_x[21] = {0.74, 1.52,  1.72,   1.6,  1.48,  0.92, 0.04,   -0.2, -0.14, 0.02,  0.3,   0.54,   0.4,  0.36, 0.52,  0.96,  1.22,  1.62,  1.76,  1.64, 1.14};
  double tar_y[21] = {0.0, -0.22, -0.94, -1.64, -1.92, -1.94, -1.96, -1.74, -0.72, -0.4, -0.38, -0.58, -0.96, -1.34, -1.42, -1.3, -1.32, -1.44, -1.04, -0.38, -0.2};

  double data_out[TARGET_NUMBER] = {0.34, 0.0, 0.66, 0.0, 0.98, -0.04, 1.14, -0.18, 1.14, -0.18, 0.88, -0.4, 0.58, -0.54, 0.54, -0.54, 0.54, -0.54, 0.44, -0.86, 0.34, -1.18, 0.36, -1.42, 0.36, -1.42, 0.68, -1.4}; //, 0.74, -1.38

  tar_array.data.clear();
  /*
  for(int i = 0; i < 21; i++)
  {
      tar_array.data.push_back(tar_x[i]);
      tar_array.data.push_back(tar_y[i]);
  }
  */
  for(int i = 0; i < TARGET_NUMBER; i++)
  {
      tar_array.data.push_back(data_out[i]);
  }

  int command_number = 0;
  tar_array.data.push_back(command_number);

  twist_msg.linear.x = 0.6;
  twist_msg.linear.y = -0.5;

  ros::Publisher chatter_pub = n.advertise<std_msgs::Float32MultiArray>("target", 1);

  ros::Rate loop_rate(2);

  while (ros::ok())
  {
    chatter_pub.publish(tar_array);

    ros::spinOnce();

    loop_rate.sleep();
  }

  return 0;
}
