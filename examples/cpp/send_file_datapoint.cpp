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
using v1::model::File;


class FormantAgentClient {
public:
   FormantAgentClient(std::shared_ptr<Channel> channel) : stub_(Agent::NewStub(channel)) {}

   void PostFileDatapoint(
      const std::string &stream,
      const std::string &filePath
   ) {
      std::cout << "posting file datapoint on stream '" << stream << "'" << std::endl;

      Datapoint datapoint;
      
      // Set the stream name
      datapoint.set_stream(stream);

      // Set the timestamp to now
      datapoint.set_timestamp(GetCurrentTimestamp());

      // Set the file location
      datapoint.mutable_file()->set_url(filePath);

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
  
   // Send a file datapoint based on user input
   std::string filePath;
   std::cout << "enter the full file path: ";
   std::cin >> filePath;
   client.PostFileDatapoint("example.file", filePath);
   
   return 0;
}