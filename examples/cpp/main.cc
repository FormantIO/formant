#include <iostream>
#include <limits.h>
#include <memory>
#include <string>
#include <sys/time.h>
#include <unistd.h>

#include <grpcpp/grpcpp.h>

#include "protos/agent/v1/agent.grpc.pb.h"

using grpc::Channel;
using grpc::ClientContext;
using grpc::Status;

using v1::agent::Agent;
using v1::agent::PostDataResponse;
using v1::model::Datapoint;
using v1::model::File;
using v1::model::Text;

class AgentClient {
public:
  AgentClient(std::shared_ptr<Channel> channel)
      : stub_(Agent::NewStub(channel)) {}

  void PostTextDatapoint(const std::string &stream,
                         const std::string &payload) {
    std::cout << "posting text datapoint on " << stream << std::endl;
    Datapoint datapoint;
    (*datapoint.mutable_tags())["annotation"] = "formant_exp_001";
    datapoint.mutable_text()->set_value(payload);
    datapoint.set_stream(stream);
    datapoint.set_timestamp(GetCurrentTimestamp());
    PostDataResponse response;
    ClientContext context;
    Status status = stub_->PostData(&context, datapoint, &response);
    if (!status.ok()) {
      std::cout << "gRPC error: " << status.error_code() << ": "
                << status.error_message() << std::endl;
    }
  }

  void PostFileDatapoint(const std::string &stream,
                         const std::string &filePath) {
    std::cout << "posting file datapoint on " << stream << std::endl;
    Datapoint datapoint;
    (*datapoint.mutable_tags())["annotation"] = "formant_exp_002";
    datapoint.mutable_file()->set_url("file://" + filePath);
    datapoint.set_stream(stream);
    datapoint.set_timestamp(GetCurrentTimestamp());
    PostDataResponse response;
    ClientContext context;
    Status status = stub_->PostData(&context, datapoint, &response);
    if (!status.ok()) {
      std::cout << "gRPC error: " << status.error_code() << ": "
                << status.error_message() << std::endl;
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

int main(int argc, char **argv) {
  AgentClient client(grpc::CreateChannel("localhost:5501",
                                         grpc::InsecureChannelCredentials()));
  client.PostTextDatapoint("stream.001", "example datapoint");
  std::string filePath;
  std::cout << "enter full file path: ";
  std::cin >> filePath;
  client.PostFileDatapoint("stream.002", filePath);
  return 0;
}
