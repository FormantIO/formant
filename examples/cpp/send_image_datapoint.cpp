#include <limits.h>
#include <memory>
#include <string>
#include <sys/time.h>
#include <unistd.h>
#include <stdio.h>
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

class FormantAgentClient {
public:
   FormantAgentClient(std::shared_ptr<Channel> channel) : stub_(Agent::NewStub(channel)) {}

   void PostImageDatapoint(
      const std::string &stream,
      const std::string &imageFilePath
   ) {
      std::cout << "posting image datapoint on stream '" << stream << "'" << std::endl;

      Datapoint datapoint;
      
      // Set the stream name
      datapoint.set_stream(stream);

      // Set the timestamp to now
      datapoint.set_timestamp(GetCurrentTimestamp());

      // Get the image and add it to the datapoint
      auto full_path = GetCurrentDirectory() + "/" + imageFilePath;
      datapoint.mutable_image()->set_url(full_path);

      // If you have the image as a const char *:
      // datapoint.mutable_image()->set_raw(image);

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
  
   // Send an image datapoint
   client.PostImageDatapoint("example.image", "../data/cargo.png");
   
   return 0;
}