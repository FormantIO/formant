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
using v1::agent::GetTeleopControlDataStreamRequest;
using v1::agent::GetTeleopControlDataStreamResponse;
using v1::agent::PostDataResponse;
using v1::model::Datapoint;
using v1::model::Bitset;

class FormantAgentClient
{
public:
   FormantAgentClient(std::shared_ptr<Channel> channel) : stub_(Agent::NewStub(channel)) {}

   void Teleop()
   {
      std::cout << "beginning to listen for data..." << std::endl;

      // Set up the stream
      ClientContext context;
      GetTeleopControlDataStreamRequest request;
      auto stream = stub_->GetTeleopControlDataStream(&context, request);

      // Handle an infinite blocking list of commands
      GetTeleopControlDataStreamResponse message;
      while (stream->Read(&message))
      {
         auto stream = message.control_datapoint().stream();
         auto timestamp = message.control_datapoint().timestamp();

         // Print the stream name and timestamp
         std::cout << "Stream name: " << stream
                     <<  " at timestamp: " << timestamp <<std::endl;

         if (stream == "joystick") {
            // Capture joystick axes
            auto twist_x = message.control_datapoint().twist().angular().x();
            auto twist_y = message.control_datapoint().twist().angular().y();
            auto twist_z = message.control_datapoint().twist().angular().z();

            auto linear_x = message.control_datapoint().twist().linear().x();
            auto linear_y = message.control_datapoint().twist().linear().y();
            auto linear_z = message.control_datapoint().twist().linear().z();

            std::cout << "    " 
                        << "Twist:  " << twist_x << ", " 
                                    << twist_y << ", " 
                                    << twist_z << ", " 
                        << "  Linear: " << linear_x << ", " 
                                       << linear_y << ", " 
                                       << linear_z << std::endl;

         } else if (stream == "Buttons") {

            auto button_name = message.control_datapoint().bitset().bits()[0].key();
            std::cout << "    Button " << button_name << " has been pressed." << std::endl;
            
         } else if (stream == "Localization") {
            auto translation_x = message.control_datapoint().pose().translation().x();
            auto quaternion_w = message.control_datapoint().pose().rotation().w();
            std::cout << "    translation x: " <<  translation_x << " quaternion w: " << quaternion_w << std::endl;
         }

         // Rate limit to max 20Hz
         if (GetCurrentTimestamp() - last_status_time > 50) {
            
            last_status_time = GetCurrentTimestamp();

            // Create a map to send as a bitset
            std::map<std::string, bool> bitset;
            bitset.insert(std::pair<std::string, bool>("PTZ mode", true));
            bitset.insert(std::pair<std::string, bool>("Walk mode", false));
            bitset.insert(std::pair<std::string, bool>("Has lease", true));
            bitset.insert(std::pair<std::string, bool>("Has estop", false));
            bitset.insert(std::pair<std::string, bool>("FLIR online", true));
            
            PostBitsetDatapoint("Status", bitset);
         }
      }
      Status status = stream->Finish();
   
         return;
   }

   void PostBitsetDatapoint(
      const std::string &stream,
      const std::map<std::string, bool> &bitset_map
   ) {
      std::cout << "posting bitset datapoint on stream '" << stream << "'" << std::endl;

      Datapoint datapoint;

      // Set the stream name
      datapoint.set_stream(stream);
      
      // Set the timestamp to now
      datapoint.set_timestamp(GetCurrentTimestamp());

      // Create the bitset from the map
      for (auto const& element : bitset_map) {
         auto bit = datapoint.mutable_bitset()->add_bits();
         bit->set_key(element.first);
         bit->set_value(element.second);
      }

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

   long int last_status_time{0};

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

   // Start listening for commands
   client.Teleop();

   return 0;
}