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
using v1::agent::GetInterventionRequestRequest;
using v1::agent::GetInterventionResponseRequest;
using v1::model::Image;
using v1::model::Severity;
using v1::model::InterventionRequest;
using v1::model::InterventionResponse;


class FormantAgentClient
{
public:
   FormantAgentClient(std::shared_ptr<Channel> channel) : stub_(Agent::NewStub(channel)) {}

   void SendReceiveInterventionRequest()
   {
      std::cout << "beginning intervention request" << std::endl;

      // Set up the request
      ClientContext request_context;
      InterventionRequest request_request;
      InterventionRequest request_response;

      // Set the properties for the request
      request_request.set_timestamp(GetCurrentTimestamp());
      request_request.set_severity(Severity::INFO);

      // Set up an image labeling request - also try .mutable_selection_request()
      auto image_url = GetCurrentDirectory() + "/../data/cargo.png";
      request_request.mutable_labeling_request()->mutable_image()->set_url(image_url);
      request_request.mutable_labeling_request()->mutable_image()->set_content_type("image/png");
      request_request.mutable_labeling_request()->set_title("Label blue packages");
      request_request.mutable_labeling_request()->set_instruction(
         "Select the individual blue packages in the front row."
      );

      // Send the request
      std::cout << "sending intevention request...";
      auto request_status = stub_->CreateInterventionRequest(
         &request_context, 
         request_request, 
         &request_response
      );
      std::cout << " done" << std::endl;

      // Exit out if the request failed
      if (!request_status.ok()) {
         std::cout << "intervention request failed" << std::endl;

         return;
      }

      // Wait for input to allow time for answering
      std::cout << "pausing - please complete the request through the Formant app" << std::endl;
      std::cin.get();

      // Get an existing request by ID - it may still be incomplete
      ClientContext get_request_context;
      GetInterventionRequestRequest get_request_request;
      InterventionRequest get_request_response;

      // Set the id that was assigned to our request
      get_request_request.set_id(request_response.id());

      // Run the query - this will be polled from the device
      auto get_request_status = stub_->GetInterventionRequest(
         &get_request_context,
         get_request_request,
         &get_request_response
      );

      // Check to make sure a response exists
      if (get_request_response.responses_size() > 0) {
         // Print the debug string to show the entire structure
         std::cout << get_request_response.DebugString() << std::endl;
      } else {
         std::cout << "no response found" << std::endl;

         return;
      }

      // Loop through responses
      for (int i = 0; i < get_request_response.responses().size(); i++) {
         std::cout << "response " << i << ": " << std::endl;
         auto response = get_request_response.responses().at(i);

         for (int j = 0; j < response.labeling_response().value_size(); j++) {
            std::cout << "  object " << j << ": " << std::endl;
            auto value = response.labeling_response().value().at(j);

            for (int k = 0; k < value.vertices_size(); k++) {
               std::cout << "    vertices for point " << k << ": ";
               std::cout << "(" << value.vertices().at(k).x() << ", ";
               std::cout << value.vertices().at(k).y() << ")" << std::endl; 
            }
         }

      }
      return;
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

   // Start listening for commands
   client.SendReceiveInterventionRequest();

   return 0;
}