#include <iostream>
#include <limits.h>
#include <memory>
#include <string>
#include <sys/time.h>
#include <unistd.h>
#include <map>

#include <grpcpp/grpcpp.h>

#include "agent/v1/agent.grpc.pb.h"

using grpc::Channel;
using grpc::ClientContext;
using grpc::Status;

using v1::agent::Agent;
using v1::agent::PostDataResponse;
using v1::model::Datapoint;
using v1::model::Bitset;


class FormantAgentClient {
public:
   FormantAgentClient(std::shared_ptr<Channel> channel) : stub_(Agent::NewStub(channel)) {}

   void PostBitsetDatapoint(
      const std::string &stream,
      const std::map<std::string, bool> &bitset_map
   ) {
      std::cout << "posting bitset datapoint on stream '" << stream << "'" << std::endl;

      Datapoint datapoint;

      // Set the stream name
      datapoint.set_stream(stream);
      
      // Set the timestamp to now
      datapoint.set_timestamp(GetCurrentTimestamp());

      // Create the bitset from the map
      for (auto const& element : bitset_map) {
         auto bit = datapoint.mutable_bitset()->add_bits();
         bit->set_key(element.first);
         bit->set_value(element.second);
      }

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

   long int GetCurrentTimestamp() {
      struct timeval tp;
      gettimeofday(&tp, NULL);

      return tp.tv_sec * 1000 + tp.tv_usec / 1000;
  }
};

int main(int argc, char **argv)
{
   // Create the Formant Agent client object
   FormantAgentClient client(grpc::CreateChannel("localhost:5501", grpc::InsecureChannelCredentials()));
  
   // Create a map to send as a bitset
   std::map<std::string, bool> bitset;
   bitset.insert(std::pair<std::string, bool>("estop", false));
   bitset.insert(std::pair<std::string, bool>("lidar ok", true));
   bitset.insert(std::pair<std::string, bool>("planner ok", true));
   bitset.insert(std::pair<std::string, bool>("battery ok", true));
   bitset.insert(std::pair<std::string, bool>("motors ok", true));
   bitset.insert(std::pair<std::string, bool>("moving", false));
   
   client.PostBitsetDatapoint("example.bitset", bitset);
   
   return 0;
}