#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>
#include "geometry_msgs/Twist.h"
#include "std_msgs/Float32MultiArray.h"

int main(int argc, char **argv)
{

  ros::init(argc, argv, "simple_publisher");

  ros::NodeHandle n;

  geometry_msgs::Twist twist_msg;
  std_msgs::Float32MultiArray tar_array;

  double tar_x[3] = {1.0, 1.82, 1.82};
  double tar_y[3] = {0.0, -0.67, -1.47};
  tar_array.data.clear();
  for(int i = 0; i < 3; i++)
  {
      tar_array.data.push_back(tar_x[i]);
      tar_array.data.push_back(tar_y[i]);
  }

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
