import time

from formant.sdk.agent.v1 import Client
from formant.protos.agent.v1 import agent_pb2

fclient = Client(agent_url="unix:///tmp/agent.sock")

time.sleep(0.01)

sdp = input("> ")

r = fclient.agent_stub.PostLanRtcOffer(agent_pb2.PostLanRtcOfferRequest(offer_sdp=sdp))
print("\n\n" + r.answer_sdp)
