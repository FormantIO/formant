import time

import grpc
from formant.protos.agent.v1 import agent_pb2_grpc
from formant.protos.model.v1.datapoint_pb2 import Datapoint
from formant.protos.model.v1.math_pb2 import Quaternion, Transform, Twist, Vector3
from formant.protos.model.v1.navigation_pb2 import (
    Goal,
    Localization,
    Map,
    OccupancyGrid,
    Odometry,
    Path,
)

channel = grpc.insecure_channel("localhost:5501")
agent = agent_pb2_grpc.AgentStub(channel)

zero = Transform(
    translation=Vector3(x=0.0, y=0.0, z=0.0),
    rotation=Quaternion(x=0.0, y=0.0, z=0.0, w=1.0),
)

map_resolution = 1
map_width = 100
map_height = 100
occupancy_grid_data = []
for i in range(map_height):
    for j in range(map_width):
        occupancy_grid_data.append(0)


localization = Localization(
    odometry=Odometry(pose=zero, twist=Twist(), world_to_local=zero),
    map=Map(
        resolution=map_resolution,
        width=map_width,
        height=map_height,
        origin=zero,
        world_to_local=zero,
        occupancy_grid=OccupancyGrid(),
    ),
    path=Path(world_to_local=zero),
    goal=Goal(pose=zero, world_to_local=zero),
)

localization.map.occupancy_grid.data.extend(occupancy_grid_data)
localization.path.poses.extend([zero, zero])

datapoint = Datapoint(
    stream="test.localization",
    localization=localization,
    timestamp=int(time.time() * 1000),
)

agent.PostData(datapoint)
