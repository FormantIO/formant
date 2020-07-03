import subprocess
import time

import grpc
from formant.protos.agent.v1 import agent_pb2, agent_pb2_grpc
from formant.protos.model.v1.commands_pb2 import CommandResponse
from formant.protos.model.v1.datapoint_pb2 import Datapoint
from formant.protos.model.v1.text_pb2 import Text

channel = grpc.insecure_channel("localhost:5501")
agent = agent_pb2_grpc.AgentStub(channel)


def ping(address):
    # check if the address responds within 0.1 seconds
    shell_command = ["timeout", "0.1", "ping", "-c", "1", address]
    try:
        subprocess.check_output(shell_command)
        return True
    except (OSError, subprocess.CalledProcessError):
        return False


SENSOR_ADDRESSES = ["192.168.1.28"]
MOTOR_ADDRESSES = ["192.168.30.90", "192.168.30.91", "192.168.30.92", "192.168.30.93"]

command_request_request = agent_pb2.GetCommandRequestRequest(
    command_filter=["sensor_check", "motor_check"]
)

if __name__ == "__main__":
    while True:
        command_request = agent.GetCommandRequest(command_request_request).request
        command = command_request.command
        command_request_id = command_request.id

        if command == "sensor_check":
            addresses = SENSOR_ADDRESSES
        elif command == "motor_check":
            addresses = MOTOR_ADDRESSES
        else:
            continue

        success = not (False in list(map(ping, addresses)))

        if success:
            message = "Health check succeeded"
        else:
            message = "Health check failed"

        datapoint = Datapoint(
            stream=command,
            text=Text(value=message),
            timestamp=int(time.time() * 1000.0),
        )

        command_response = CommandResponse(
            request_id=command_request_id, success=True, datapoint=datapoint
        )
        command_response = agent_pb2.SendCommandResponseRequest(
            response=command_response
        )
        agent.SendCommandResponse(command_response)

        time.sleep(0.05)
