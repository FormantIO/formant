#include <iostream>
#include <limits.h>
#include <memory>
#include <string>
#include <sys/time.h>
#include <unistd.h>
#include <signal.h>
#include <thread>

#include <grpcpp/grpcpp.h>

#include "agent/v1/agent.grpc.pb.h"

using grpc::Channel;
using grpc::ClientContext;
using grpc::ClientAsyncResponseReader;
using grpc::CompletionQueue;
using grpc::Status;

using v1::agent::Agent;
using v1::agent::GetTeleopHeartbeatStreamRequest;
using v1::agent::GetTeleopHeartbeatStreamResponse;

class FormantAgentClient
{
public:
   FormantAgentClient(std::shared_ptr<Channel> channel) : stub_(Agent::NewStub(channel)) {}

   void Listen()
   {
      std::cout << "beginning to listen for data..." << std::endl;

      ClientContext context;
      GetTeleopHeartbeatStreamRequest request;
      auto stream = stub_->GetTeleopHeartbeatStream(&context, request);

      // Handle an infinite blocking list of commands
      GetTeleopHeartbeatStreamResponse message;
      while (stream->Read(&message)) {

         std::cout << "Received heartbeat,  disconnect state: " << message.is_disconnect() << std::endl;
      
      }

      std::cout << "ending listen for data..." << std::endl;
   }

private:

   std::unique_ptr<Agent::Stub> stub_;

};

int main(int argc, char **argv)
{
   // Create the Formant Agent client object
   FormantAgentClient client(grpc::CreateChannel("localhose:5501", grpc::InsecureChannelCredentials()));

   std::cout << "Press control-c to quit" << std::endl << std::endl;

   // Start listening for commands
   std::thread thread_ = std::thread(&FormantAgentClient::Listen, &client);
   
   thread_.join();  // blocks forever

   return 0;
}