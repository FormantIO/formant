// package: agent
// file: agent.proto

import * as agent_pb from "./agent_pb";
import {grpc} from "grpc-web-client";

type AgentStreamData = {
  readonly methodName: string;
  readonly service: typeof Agent;
  readonly requestStream: true;
  readonly responseStream: false;
  readonly requestType: typeof agent_pb.Datapoint;
  readonly responseType: typeof agent_pb.StreamDataResponse;
};

type AgentPostData = {
  readonly methodName: string;
  readonly service: typeof Agent;
  readonly requestStream: false;
  readonly responseStream: false;
  readonly requestType: typeof agent_pb.Datapoint;
  readonly responseType: typeof agent_pb.PostDataResponse;
};

type AgentRegisterROSTopic = {
  readonly methodName: string;
  readonly service: typeof Agent;
  readonly requestStream: false;
  readonly responseStream: false;
  readonly requestType: typeof agent_pb.ROSTopic;
  readonly responseType: typeof agent_pb.RegisterROSTopicResponse;
};

type AgentGetROSTopics = {
  readonly methodName: string;
  readonly service: typeof Agent;
  readonly requestStream: false;
  readonly responseStream: false;
  readonly requestType: typeof agent_pb.GetROSTopicsRequest;
  readonly responseType: typeof agent_pb.GetROSTopicsResponse;
};

type AgentCreateInterventionRequest = {
  readonly methodName: string;
  readonly service: typeof Agent;
  readonly requestStream: false;
  readonly responseStream: false;
  readonly requestType: typeof agent_pb.InterventionRequest;
  readonly responseType: typeof agent_pb.InterventionRequest;
};

type AgentGetInterventionRequest = {
  readonly methodName: string;
  readonly service: typeof Agent;
  readonly requestStream: false;
  readonly responseStream: false;
  readonly requestType: typeof agent_pb.GetInterventionRequestRequest;
  readonly responseType: typeof agent_pb.InterventionRequest;
};

type AgentGetInterventionResponse = {
  readonly methodName: string;
  readonly service: typeof Agent;
  readonly requestStream: false;
  readonly responseStream: false;
  readonly requestType: typeof agent_pb.GetInterventionResponseRequest;
  readonly responseType: typeof agent_pb.InterventionResponse;
};

export class Agent {
  static readonly serviceName: string;
  static readonly StreamData: AgentStreamData;
  static readonly PostData: AgentPostData;
  static readonly RegisterROSTopic: AgentRegisterROSTopic;
  static readonly GetROSTopics: AgentGetROSTopics;
  static readonly CreateInterventionRequest: AgentCreateInterventionRequest;
  static readonly GetInterventionRequest: AgentGetInterventionRequest;
  static readonly GetInterventionResponse: AgentGetInterventionResponse;
}

export type ServiceError = { message: string, code: number; metadata: grpc.Metadata }
export type Status = { details: string, code: number; metadata: grpc.Metadata }
export type ServiceClientOptions = { transport: grpc.TransportConstructor; debug?: boolean }

interface ResponseStream<T> {
  cancel(): void;
  on(type: 'data', handler: (message: T) => void): ResponseStream<T>;
  on(type: 'end', handler: () => void): ResponseStream<T>;
  on(type: 'status', handler: (status: Status) => void): ResponseStream<T>;
}
interface RequestStream<T> {
  write(message: T): RequestStream<T>;
  end(): void;
  cancel(): void;
  on(type: 'end', handler: () => void): RequestStream<T>;
  on(type: 'status', handler: (status: Status) => void): RequestStream<T>;
}
interface BidirectionalStream<T> {
  write(message: T): BidirectionalStream<T>;
  end(): void;
  cancel(): void;
  on(type: 'data', handler: (message: T) => void): BidirectionalStream<T>;
  on(type: 'end', handler: () => void): BidirectionalStream<T>;
  on(type: 'status', handler: (status: Status) => void): BidirectionalStream<T>;
}

export class AgentClient {
  readonly serviceHost: string;

  constructor(serviceHost: string, options?: ServiceClientOptions);
  streamData(metadata?: grpc.Metadata): RequestStream<agent_pb.StreamDataResponse>;
  postData(
    requestMessage: agent_pb.Datapoint,
    metadata: grpc.Metadata,
    callback: (error: ServiceError|null, responseMessage: agent_pb.PostDataResponse|null) => void
  ): void;
  postData(
    requestMessage: agent_pb.Datapoint,
    callback: (error: ServiceError|null, responseMessage: agent_pb.PostDataResponse|null) => void
  ): void;
  registerROSTopic(
    requestMessage: agent_pb.ROSTopic,
    metadata: grpc.Metadata,
    callback: (error: ServiceError|null, responseMessage: agent_pb.RegisterROSTopicResponse|null) => void
  ): void;
  registerROSTopic(
    requestMessage: agent_pb.ROSTopic,
    callback: (error: ServiceError|null, responseMessage: agent_pb.RegisterROSTopicResponse|null) => void
  ): void;
  getROSTopics(
    requestMessage: agent_pb.GetROSTopicsRequest,
    metadata: grpc.Metadata,
    callback: (error: ServiceError|null, responseMessage: agent_pb.GetROSTopicsResponse|null) => void
  ): void;
  getROSTopics(
    requestMessage: agent_pb.GetROSTopicsRequest,
    callback: (error: ServiceError|null, responseMessage: agent_pb.GetROSTopicsResponse|null) => void
  ): void;
  createInterventionRequest(
    requestMessage: agent_pb.InterventionRequest,
    metadata: grpc.Metadata,
    callback: (error: ServiceError|null, responseMessage: agent_pb.InterventionRequest|null) => void
  ): void;
  createInterventionRequest(
    requestMessage: agent_pb.InterventionRequest,
    callback: (error: ServiceError|null, responseMessage: agent_pb.InterventionRequest|null) => void
  ): void;
  getInterventionRequest(
    requestMessage: agent_pb.GetInterventionRequestRequest,
    metadata: grpc.Metadata,
    callback: (error: ServiceError|null, responseMessage: agent_pb.InterventionRequest|null) => void
  ): void;
  getInterventionRequest(
    requestMessage: agent_pb.GetInterventionRequestRequest,
    callback: (error: ServiceError|null, responseMessage: agent_pb.InterventionRequest|null) => void
  ): void;
  getInterventionResponse(
    requestMessage: agent_pb.GetInterventionResponseRequest,
    metadata: grpc.Metadata,
    callback: (error: ServiceError|null, responseMessage: agent_pb.InterventionResponse|null) => void
  ): void;
  getInterventionResponse(
    requestMessage: agent_pb.GetInterventionResponseRequest,
    callback: (error: ServiceError|null, responseMessage: agent_pb.InterventionResponse|null) => void
  ): void;
}

