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
using v1::model::Text;


class FormantAgentClient {
public:
   FormantAgentClient(std::shared_ptr<Channel> channel) : stub_(Agent::NewStub(channel)) {}

   void PostTextDatapoint(
      const std::string &stream,
      const std::string &payload
   ) {
      std::cout << "posting text datapoint on stream '" << stream << "'" << std::endl;

      Datapoint datapoint;

      // Set the stream name
      datapoint.set_stream(stream);
      
      // Set the timestamp to now
      datapoint.set_timestamp(GetCurrentTimestamp());

      // Set the text value
      datapoint.mutable_text()->set_value(payload);

      // Set tags if desired
      (*datapoint.mutable_tags())["annotation"] = "formant_exp_001";

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
   client.PostTextDatapoint("example.text", "example datapoint");
   
   return 0;
}