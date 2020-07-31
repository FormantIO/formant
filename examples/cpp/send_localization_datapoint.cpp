#include <limits.h>
#include <memory>
#include <string>
#include <sys/time.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <grpcpp/grpcpp.h>

#include "agent/v1/agent.grpc.pb.h"

using grpc::Channel;
using grpc::ClientContext;
using grpc::Status;

using v1::agent::Agent;
using v1::agent::PostDataResponse;
using v1::model::Datapoint;
using v1::model::Image;
using v1::model::Localization;
using v1::model::Transform;
using v1::model::Goal;
using v1::model::Map;
using v1::model::OccupancyGrid;
using v1::model::Odometry;
using v1::model::Path;


class FormantAgentClient {
public:
   FormantAgentClient(std::shared_ptr<Channel> channel) : stub_(Agent::NewStub(channel)) {}

   void PostLocalizationDatapoint(const std::string &stream) {
      std::cout << "posting localization datapoint on stream '" << stream << "'" << std::endl;

      Datapoint datapoint;
      
      // Set the stream name
      datapoint.set_stream(stream);

      // Set the timestamp to now
      datapoint.set_timestamp(GetCurrentTimestamp());

      // Set the current odometry
      auto odom = datapoint.mutable_localization()->mutable_odometry();

      odom->mutable_pose()->mutable_rotation()->set_w(1.0);
      odom->mutable_pose()->mutable_rotation()->set_x(0.0);
      odom->mutable_pose()->mutable_rotation()->set_y(0.0);
      odom->mutable_pose()->mutable_rotation()->set_z(0.0);
      odom->mutable_pose()->mutable_translation()->set_x(0.0);
      odom->mutable_pose()->mutable_translation()->set_y(0.0);
      odom->mutable_pose()->mutable_translation()->set_z(0.0);

      odom->mutable_twist()->mutable_angular()->set_x(0.0);
      odom->mutable_twist()->mutable_angular()->set_y(0.0);
      odom->mutable_twist()->mutable_angular()->set_z(0.0);
      odom->mutable_twist()->mutable_linear()->set_x(0.0);
      odom->mutable_twist()->mutable_linear()->set_y(0.0);
      odom->mutable_twist()->mutable_linear()->set_z(0.0);

      odom->mutable_world_to_local()->mutable_rotation()->set_w(1.0);
      odom->mutable_world_to_local()->mutable_rotation()->set_x(0.0);
      odom->mutable_world_to_local()->mutable_rotation()->set_y(0.0);
      odom->mutable_world_to_local()->mutable_rotation()->set_z(0.0);
      odom->mutable_world_to_local()->mutable_translation()->set_x(0.0);
      odom->mutable_world_to_local()->mutable_translation()->set_y(0.0);
      odom->mutable_world_to_local()->mutable_translation()->set_z(0.0);

      // Create a path datapoint
      auto path = datapoint.mutable_localization()->mutable_path();
      path->mutable_world_to_local()->mutable_rotation()->set_w(1.0);
      path->mutable_world_to_local()->mutable_rotation()->set_x(0.0);
      path->mutable_world_to_local()->mutable_rotation()->set_y(0.0);
      path->mutable_world_to_local()->mutable_rotation()->set_z(0.0);
      path->mutable_world_to_local()->mutable_translation()->set_x(0.0);
      path->mutable_world_to_local()->mutable_translation()->set_y(0.0);
      path->mutable_world_to_local()->mutable_translation()->set_z(0.0);
      
      // Use generated example waypoints for the path
      auto waypoint_x = 0.0;
      auto waypoint_y = 0.0;
      auto waypoint_z = 0.0;
      for (int i = 0; i < 15; i++) {
         if (i > 0) {
            // Update current translation with random walk (for example purposes)    
            waypoint_x += static_cast<double>(rand() % 10 - 5);
            waypoint_y += static_cast<double>(rand() % 10 - 5);
            waypoint_z += 0.1 * static_cast<double>(rand() % 10 - 5);
         }

         // Add waypoints to the path
         auto pose = path->add_poses();
         pose->mutable_rotation()->set_w(i);
         pose->mutable_rotation()->set_x(i);
         pose->mutable_rotation()->set_y(i);
         pose->mutable_rotation()->set_z(i);
         pose->mutable_translation()->set_x(waypoint_x);
         pose->mutable_translation()->set_y(waypoint_y);
         pose->mutable_translation()->set_z(waypoint_z);
      }

      // Add a map to the localization datapoint
      auto map_width = 25.0;
      auto map_height = 25.0;
      auto map = datapoint.mutable_localization()->mutable_map();

      map->mutable_origin()->mutable_rotation()->set_w(1.0);
      map->mutable_origin()->mutable_rotation()->set_x(0.0);
      map->mutable_origin()->mutable_rotation()->set_y(0.0);
      map->mutable_origin()->mutable_rotation()->set_z(0.0);
      map->mutable_origin()->mutable_translation()->set_x(-(map_width / 2.0));
      map->mutable_origin()->mutable_translation()->set_y(-(map_height / 2.0));
      map->mutable_origin()->mutable_translation()->set_z(0.0);
   
      map->mutable_world_to_local()->mutable_rotation()->set_w(1.0);
      map->mutable_world_to_local()->mutable_rotation()->set_x(0.0);
      map->mutable_world_to_local()->mutable_rotation()->set_y(0.0);
      map->mutable_world_to_local()->mutable_rotation()->set_z(0.0);
      map->mutable_world_to_local()->mutable_translation()->set_x(0.0);
      map->mutable_world_to_local()->mutable_translation()->set_y(0.0);
      map->mutable_world_to_local()->mutable_translation()->set_z(0.0);
      

      // Set the map as an occupancy grid

      for (int i = 0; i < (map_height * map_width); i++) {
         // Add a grid value between -1 (unmapped) and 100
         map->mutable_occupancy_grid()->add_data(rand() % 100 - 1);
      }
      map->set_width(map_width);
      map->set_height(map_height);
      map->set_resolution(1);

      // Set a goal (using the final example waypoint)
      auto goal = datapoint.mutable_localization()->mutable_goal();

      goal->mutable_pose()->mutable_rotation()->set_w(1.0);
      goal->mutable_pose()->mutable_rotation()->set_x(0.0);
      goal->mutable_pose()->mutable_rotation()->set_y(0.0);
      goal->mutable_pose()->mutable_rotation()->set_z(0.0);
      goal->mutable_pose()->mutable_translation()->set_x(waypoint_x);
      goal->mutable_pose()->mutable_translation()->set_y(waypoint_y);
      goal->mutable_pose()->mutable_translation()->set_z(waypoint_z);
      
      goal->mutable_world_to_local()->mutable_rotation()->set_w(1.0);
      goal->mutable_world_to_local()->mutable_rotation()->set_x(0.0);
      goal->mutable_world_to_local()->mutable_rotation()->set_y(0.0);
      goal->mutable_world_to_local()->mutable_rotation()->set_z(0.0);
      goal->mutable_world_to_local()->mutable_translation()->set_x(0.0);
      goal->mutable_world_to_local()->mutable_translation()->set_y(0.0);
      goal->mutable_world_to_local()->mutable_translation()->set_z(0.0);
      
      // Send the datapoint to the Formant Agent
      PostDataResponse response;
      ClientContext context;
      Status status = stub_->PostData(&context, datapoint, &response);
    
      if (!status.ok()) {
         std::cout << "gRPC error: " << status.error_code() << ": " << status.error_message() << std::endl;
      } else {
         std::cout << "complete" << std::endl;
      }
   }

private:
  
   std::unique_ptr<Agent::Stub> stub_;

   // Return the current timestamp
   long int GetCurrentTimestamp() {
      struct timeval tp;
      gettimeofday(&tp, NULL);

      return tp.tv_sec * 1000 + tp.tv_usec / 1000;
   }

   // Get the current working directory
   std::string GetCurrentDirectory() {
      char cwd[PATH_MAX];
      if (getcwd(cwd, sizeof(cwd)) != NULL) {
         std::string s(cwd);
         return s;
      } else {
         return NULL;
      }
   }
};

int main(int argc, char **argv)
{
   // Create the Formant Agent client object
   FormantAgentClient client(grpc::CreateChannel("localhost:5501", grpc::InsecureChannelCredentials()));
  
   // Send a localization datapoint
   client.PostLocalizationDatapoint("example.localization");
   
   return 0;
}