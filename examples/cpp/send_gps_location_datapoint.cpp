#include <iostream>
#include <limits.h>
#include <memory>
#include <string>
#include <sys/time.h>
#include <unistd.h>

#include <grpcpp/grpcpp.h>

#include "agent/v1/agent.grpc.pb.h"

using grpc::Channel;
using grpc::ClientContext;
using grpc::Status;

using v1::agent::Agent;
using v1::agent::PostDataResponse;
using v1::model::Datapoint;
using v1::model::Location;

class FormantAgentClient {
public:
   FormantAgentClient(std::shared_ptr<Channel> channel) : stub_(Agent::NewStub(channel)) {}

   void PostLocationDatapoint(
      const std::string &stream,
      const float &latitude,
      const float &longitude
   ) {
      std::cout << "posting location datapoint on stream '" << stream << "'" << std::endl;

      Datapoint datapoint;
      
      // Set the stream name
      datapoint.set_stream(stream);

      // Set the timestamp to now
      datapoint.set_timestamp(GetCurrentTimestamp());

      // Set the gps coordinate values
      datapoint.mutable_location()->set_latitude(latitude);
      datapoint.mutable_location()->set_longitude(longitude);

      // Set tags if desired
      (*datapoint.mutable_tags())["example_tag_key"] = "example_tag_value";

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
  
   // Send a numeric datapoint
   client.PostLocationDatapoint("example.location", 40.473926, -79.948547);
   
   return 0;
}