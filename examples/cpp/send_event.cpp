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
using v1::agent::CreateEventRequest;
using v1::agent::CreateEventResponse;
using v1::model::Event;


class FormantAgentClient {
public:
   FormantAgentClient(std::shared_ptr<Channel> channel) : stub_(Agent::NewStub(channel)) {}

   void PostEvent() {
      std::cout << "posting event" << std::endl;

      // Set up the event
      ClientContext context;
      CreateEventRequest event_request;
      CreateEventResponse event_response;

      event_request.mutable_event()->set_timestamp(GetCurrentTimestamp());
      event_request.mutable_event()->set_message("event sent from test function");
      event_request.mutable_event()->set_notification_enabled(true);

      // Post the event
      auto status = stub_->CreateEvent(&context, event_request, &event_response);

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
   FormantAgentClient client(
      grpc::CreateChannel(
         "localhost:5501", 
         grpc::InsecureChannelCredentials()
      )
   );
  
   // Send an event
   client.PostEvent();
   
   return 0;
}