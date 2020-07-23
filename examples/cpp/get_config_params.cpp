#include <iostream>
#include <limits.h>
#include <memory>
#include <string>
#include <sys/time.h>
#include <unistd.h>
#include <signal.h>

#include <grpcpp/grpcpp.h>

#include "agent/v1/agent.grpc.pb.h"

using grpc::Channel;
using grpc::ClientContext;
using grpc::Status;

using v1::agent::Agent;
using v1::agent::GetApplicationConfigurationRequest;
using v1::agent::GetApplicationConfigurationResponse;

class FormantAgentClient
{
public:
   FormantAgentClient(std::shared_ptr<Channel> channel) : stub_(Agent::NewStub(channel)) {}

   void GetConfig()
   {
      std::cout << "getting configuration parameters..." << std::endl;

      // Set up the request
      ClientContext context;
      GetApplicationConfigurationRequest request;
      GetApplicationConfigurationResponse response;

      // Get the configuration object from the agent
      stub_->GetApplicationConfiguration(&context, request, &response);

      // Print the configuration object
      auto config = response.configuration();

      std::cout << "number of params: " << config.configuration_map_size() << std::endl;

      // Print the value of the "test" key
      if (config.configuration_map().contains("test"))
      {
         auto test_val = config.configuration_map().find("test")->second.c_str();
         std::cout << "value for 'test' key: " << test_val << std::endl;
      }

      // Print the whole config object
      std::cout << "whole config object: " << std::endl;
      std::cout << config.DebugString() << std::endl;

      return;
   }

private:
   std::unique_ptr<Agent::Stub> stub_;
};

int main(int argc, char **argv)
{
   // Create the Formant Agent client object
   FormantAgentClient client(grpc::CreateChannel("localhost:5501", grpc::InsecureChannelCredentials()));

   // Get and print the current config
   client.GetConfig();

   return 0;
}
