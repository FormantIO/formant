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
using v1::agent::GetCustomDataChannelMessageStreamRequest;
using v1::agent::GetCustomDataChannelMessageStreamResponse;
using v1::agent::SendOnCustomDataChannelRequest;
using v1::agent::SendOnCustomDataChannelResponse;

class FormantAgentClient
{
public:
   FormantAgentClient(std::shared_ptr<Channel> channel) : stub_(Agent::NewStub(channel)) {}

   void SendReceiveOnCustomDataChannel()
   {
      std::cout << "beginning to listen for data..." << std::endl;

      // Set up the stream
      ClientContext context;
      GetCustomDataChannelMessageStreamRequest request;
      auto stream = stub_->GetCustomDataChannelMessageStream(&context, request);

      // Handle an infinite blocking list of commands
      GetCustomDataChannelMessageStreamResponse message;
      while (stream->Read(&message))
      {
         auto peer_id = message.peer_id();
         auto channel_name = message.channel_name();
         auto payload = message.payload();

         // Print the peer id
         std::cout << "Peer id: " << peer_id << std::endl;

         // Print the channel name
         std::cout << "Channel: " << channel_name << std::endl;

         // Print the payload
         std::cout << "Payload: " << payload << std::endl;

         // Handle each command separately
         if (channel_name == "test-on-channel")
         {
            std::cout << "test-sdk channel message with payload: " << payload << std::endl;
         }
         else if (channel_name == "joystick")
         {
            std::cout << "joystick channel message with payload: " << payload << std::endl;
         }

         // Set up for the finish call
         ClientContext finishContext;
         SendOnCustomDataChannelRequest finishRequest;
         SendOnCustomDataChannelResponse finishResponse;

         // create json payload
         auto json = "{\"values\": [1, 2, 3], \"states\": [true, false, true]}";

         // Set the response with the request id and success / failure
         finishRequest.set_channel_name("test-sdk");
         finishRequest.set_payload(json);

         // Send the response
         stub_->SendOnCustomDataChannel(&finishContext, finishRequest, &finishResponse);
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
   client.SendReceiveOnCustomDataChannel();

   return 0;
}