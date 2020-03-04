# Note: you can update your agent application configuration
# through the web app or `fctl` command line tool

import grpc

from protos.agent.v1 import agent_pb2, agent_pb2_grpc

channel = grpc.insecure_channel("localhost:5501")
agent = agent_pb2_grpc.AgentStub(channel)

request = agent_pb2.GetApplicationConfigurationRequest()
app_config = agent.GetApplicationConfiguration(request)
config_map = app_config.configuration.configuration_map

print("Application configuration: %s" % config_map)
