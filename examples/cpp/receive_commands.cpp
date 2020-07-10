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
using v1::agent::GetCommandRequestStreamRequest;
using v1::agent::GetCommandRequestStreamResponse;
using v1::agent::SendCommandResponseResponse;
using v1::agent::SendCommandResponseRequest;


class FormantAgentClient {
public:
   FormantAgentClient(std::shared_ptr<Channel> channel) : stub_(Agent::NewStub(channel)) {}

   void HandleCommands()
   {
      std::cout << "beginning to listen for commands" << std::endl;

      // Set up the stream
      ClientContext context;
      GetCommandRequestStreamRequest request;
      auto stream = stub_->GetCommandRequestStream(&context, request);

      // Handle an infinite blocking list of commands
      GetCommandRequestStreamResponse message;
      while (stream->Read(&message)) {
         auto command = message.request().command();
         auto payload = message.request().text();
         auto id = message.request().id();

         // Print the command name
         std::cout << "Command: " << command << std::endl;

         // Print the command payload
         std::cout << "Payload: " << payload << std::endl;

         // Handle each command separately
         if (command == "test.one") {
            std::cout << "command one run with payload: " << payload << std::endl;

         } else if (command == "test.two") {
            std::cout << "command two run with payload: " << payload << std::endl;

         }

         // Set up for the finish call
         ClientContext finishContext;
         SendCommandResponseRequest finishRequest;
         SendCommandResponseResponse finishResponse;

         // Set the response with the request id and success / failure
         finishRequest.mutable_response()->set_request_id(id);
         finishRequest.mutable_response()->set_success(true);
         
         // Send the response
         stub_->SendCommandResponse(&finishContext, finishRequest, &finishResponse);
      }
      Status status = stream->Finish();
      
      return;
   }

private:
  
   std::unique_ptr<Agent::Stub> stub_;

};

int main(int argc, char **argv)
{
   // Create the Formant Agent client object
   FormantAgentClient client(grpc::CreateChannel("localhost:5501", grpc::InsecureChannelCredentials()));
   
   // Start listening for commands
   client.HandleCommands();

   return 0;
}