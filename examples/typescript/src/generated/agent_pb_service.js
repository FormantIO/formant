// package: agent
// file: agent.proto

var agent_pb = require("./agent_pb");
var grpc = require("grpc-web-client").grpc;

var Agent = (function () {
  function Agent() {}
  Agent.serviceName = "agent.Agent";
  return Agent;
}());

Agent.StreamData = {
  methodName: "StreamData",
  service: Agent,
  requestStream: true,
  responseStream: false,
  requestType: agent_pb.Datapoint,
  responseType: agent_pb.StreamDataResponse
};

Agent.PostData = {
  methodName: "PostData",
  service: Agent,
  requestStream: false,
  responseStream: false,
  requestType: agent_pb.Datapoint,
  responseType: agent_pb.PostDataResponse
};

Agent.RegisterROSTopic = {
  methodName: "RegisterROSTopic",
  service: Agent,
  requestStream: false,
  responseStream: false,
  requestType: agent_pb.ROSTopic,
  responseType: agent_pb.RegisterROSTopicResponse
};

Agent.GetROSTopics = {
  methodName: "GetROSTopics",
  service: Agent,
  requestStream: false,
  responseStream: false,
  requestType: agent_pb.GetROSTopicsRequest,
  responseType: agent_pb.GetROSTopicsResponse
};

Agent.CreateInterventionRequest = {
  methodName: "CreateInterventionRequest",
  service: Agent,
  requestStream: false,
  responseStream: false,
  requestType: agent_pb.InterventionRequest,
  responseType: agent_pb.InterventionRequest
};

Agent.GetInterventionRequest = {
  methodName: "GetInterventionRequest",
  service: Agent,
  requestStream: false,
  responseStream: false,
  requestType: agent_pb.GetInterventionRequestRequest,
  responseType: agent_pb.InterventionRequest
};

Agent.GetInterventionResponse = {
  methodName: "GetInterventionResponse",
  service: Agent,
  requestStream: false,
  responseStream: false,
  requestType: agent_pb.GetInterventionResponseRequest,
  responseType: agent_pb.InterventionResponse
};

exports.Agent = Agent;

function AgentClient(serviceHost, options) {
  this.serviceHost = serviceHost;
  this.options = options || {};
}

AgentClient.prototype.streamData = function streamData(metadata) {
  var listeners = {
    end: [],
    status: []
  };
  var client = grpc.client(Agent.StreamData, {
    host: this.serviceHost,
    metadata: metadata,
    transport: this.options.transport
  });
  client.onEnd(function (status, statusMessage, trailers) {
    listeners.end.forEach(function (handler) {
      handler();
    });
    listeners.status.forEach(function (handler) {
      handler({ code: status, details: statusMessage, metadata: trailers });
    });
    listeners = null;
  });
  return {
    on: function (type, handler) {
      listeners[type].push(handler);
      return this;
    },
    write: function (requestMessage) {
      if (!client.started) {
        client.start(metadata);
      }
      client.send(requestMessage);
      return this;
    },
    end: function () {
      client.finishSend();
    },
    cancel: function () {
      listeners = null;
      client.close();
    }
  };
};

AgentClient.prototype.postData = function postData(requestMessage, metadata, callback) {
  if (arguments.length === 2) {
    callback = arguments[1];
  }
  grpc.unary(Agent.PostData, {
    request: requestMessage,
    host: this.serviceHost,
    metadata: metadata,
    transport: this.options.transport,
    debug: this.options.debug,
    onEnd: function (response) {
      if (callback) {
        if (response.status !== grpc.Code.OK) {
          var err = new Error(response.statusMessage);
          err.code = response.status;
          err.metadata = response.trailers;
          callback(err, null);
        } else {
          callback(null, response.message);
        }
      }
    }
  });
};

AgentClient.prototype.registerROSTopic = function registerROSTopic(requestMessage, metadata, callback) {
  if (arguments.length === 2) {
    callback = arguments[1];
  }
  grpc.unary(Agent.RegisterROSTopic, {
    request: requestMessage,
    host: this.serviceHost,
    metadata: metadata,
    transport: this.options.transport,
    debug: this.options.debug,
    onEnd: function (response) {
      if (callback) {
        if (response.status !== grpc.Code.OK) {
          var err = new Error(response.statusMessage);
          err.code = response.status;
          err.metadata = response.trailers;
          callback(err, null);
        } else {
          callback(null, response.message);
        }
      }
    }
  });
};

AgentClient.prototype.getROSTopics = function getROSTopics(requestMessage, metadata, callback) {
  if (arguments.length === 2) {
    callback = arguments[1];
  }
  grpc.unary(Agent.GetROSTopics, {
    request: requestMessage,
    host: this.serviceHost,
    metadata: metadata,
    transport: this.options.transport,
    debug: this.options.debug,
    onEnd: function (response) {
      if (callback) {
        if (response.status !== grpc.Code.OK) {
          var err = new Error(response.statusMessage);
          err.code = response.status;
          err.metadata = response.trailers;
          callback(err, null);
        } else {
          callback(null, response.message);
        }
      }
    }
  });
};

AgentClient.prototype.createInterventionRequest = function createInterventionRequest(requestMessage, metadata, callback) {
  if (arguments.length === 2) {
    callback = arguments[1];
  }
  grpc.unary(Agent.CreateInterventionRequest, {
    request: requestMessage,
    host: this.serviceHost,
    metadata: metadata,
    transport: this.options.transport,
    debug: this.options.debug,
    onEnd: function (response) {
      if (callback) {
        if (response.status !== grpc.Code.OK) {
          var err = new Error(response.statusMessage);
          err.code = response.status;
          err.metadata = response.trailers;
          callback(err, null);
        } else {
          callback(null, response.message);
        }
      }
    }
  });
};

AgentClient.prototype.getInterventionRequest = function getInterventionRequest(requestMessage, metadata, callback) {
  if (arguments.length === 2) {
    callback = arguments[1];
  }
  grpc.unary(Agent.GetInterventionRequest, {
    request: requestMessage,
    host: this.serviceHost,
    metadata: metadata,
    transport: this.options.transport,
    debug: this.options.debug,
    onEnd: function (response) {
      if (callback) {
        if (response.status !== grpc.Code.OK) {
          var err = new Error(response.statusMessage);
          err.code = response.status;
          err.metadata = response.trailers;
          callback(err, null);
        } else {
          callback(null, response.message);
        }
      }
    }
  });
};

AgentClient.prototype.getInterventionResponse = function getInterventionResponse(requestMessage, metadata, callback) {
  if (arguments.length === 2) {
    callback = arguments[1];
  }
  grpc.unary(Agent.GetInterventionResponse, {
    request: requestMessage,
    host: this.serviceHost,
    metadata: metadata,
    transport: this.options.transport,
    debug: this.options.debug,
    onEnd: function (response) {
      if (callback) {
        if (response.status !== grpc.Code.OK) {
          var err = new Error(response.statusMessage);
          err.code = response.status;
          err.metadata = response.trailers;
          callback(err, null);
        } else {
          callback(null, response.message);
        }
      }
    }
  });
};

exports.AgentClient = AgentClient;

