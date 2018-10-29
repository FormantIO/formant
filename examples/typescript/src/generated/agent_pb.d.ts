// package: agent
// file: agent.proto

import * as jspb from "google-protobuf";

export class StreamDataResponse extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): StreamDataResponse.AsObject;
  static toObject(includeInstance: boolean, msg: StreamDataResponse): StreamDataResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: StreamDataResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): StreamDataResponse;
  static deserializeBinaryFromReader(message: StreamDataResponse, reader: jspb.BinaryReader): StreamDataResponse;
}

export namespace StreamDataResponse {
  export type AsObject = {
  }
}

export class PostDataResponse extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): PostDataResponse.AsObject;
  static toObject(includeInstance: boolean, msg: PostDataResponse): PostDataResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: PostDataResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): PostDataResponse;
  static deserializeBinaryFromReader(message: PostDataResponse, reader: jspb.BinaryReader): PostDataResponse;
}

export namespace PostDataResponse {
  export type AsObject = {
  }
}

export class GetROSTopicsRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetROSTopicsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetROSTopicsRequest): GetROSTopicsRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetROSTopicsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetROSTopicsRequest;
  static deserializeBinaryFromReader(message: GetROSTopicsRequest, reader: jspb.BinaryReader): GetROSTopicsRequest;
}

export namespace GetROSTopicsRequest {
  export type AsObject = {
  }
}

export class RegisterROSTopicResponse extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RegisterROSTopicResponse.AsObject;
  static toObject(includeInstance: boolean, msg: RegisterROSTopicResponse): RegisterROSTopicResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: RegisterROSTopicResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RegisterROSTopicResponse;
  static deserializeBinaryFromReader(message: RegisterROSTopicResponse, reader: jspb.BinaryReader): RegisterROSTopicResponse;
}

export namespace RegisterROSTopicResponse {
  export type AsObject = {
  }
}

export class GetROSTopicsResponse extends jspb.Message {
  clearTopicsList(): void;
  getTopicsList(): Array<string>;
  setTopicsList(value: Array<string>): void;
  addTopics(value: string, index?: number): string;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetROSTopicsResponse.AsObject;
  static toObject(includeInstance: boolean, msg: GetROSTopicsResponse): GetROSTopicsResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetROSTopicsResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetROSTopicsResponse;
  static deserializeBinaryFromReader(message: GetROSTopicsResponse, reader: jspb.BinaryReader): GetROSTopicsResponse;
}

export namespace GetROSTopicsResponse {
  export type AsObject = {
    topicsList: Array<string>,
  }
}

export class GetInterventionRequestRequest extends jspb.Message {
  getId(): string;
  setId(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetInterventionRequestRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetInterventionRequestRequest): GetInterventionRequestRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetInterventionRequestRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetInterventionRequestRequest;
  static deserializeBinaryFromReader(message: GetInterventionRequestRequest, reader: jspb.BinaryReader): GetInterventionRequestRequest;
}

export namespace GetInterventionRequestRequest {
  export type AsObject = {
    id: string,
  }
}

export class GetInterventionResponseRequest extends jspb.Message {
  getRequestId(): string;
  setRequestId(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetInterventionResponseRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetInterventionResponseRequest): GetInterventionResponseRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: GetInterventionResponseRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetInterventionResponseRequest;
  static deserializeBinaryFromReader(message: GetInterventionResponseRequest, reader: jspb.BinaryReader): GetInterventionResponseRequest;
}

export namespace GetInterventionResponseRequest {
  export type AsObject = {
    requestId: string,
  }
}

export class InterventionRequest extends jspb.Message {
  getId(): string;
  setId(value: string): void;

  getTimestamp(): number;
  setTimestamp(value: number): void;

  getSeverity(): Severity;
  setSeverity(value: Severity): void;

  hasSelectionRequest(): boolean;
  clearSelectionRequest(): void;
  getSelectionRequest(): SelectionRequest | undefined;
  setSelectionRequest(value?: SelectionRequest): void;

  hasBoundingBox2dRequest(): boolean;
  clearBoundingBox2dRequest(): void;
  getBoundingBox2dRequest(): BoundingBox2dRequest | undefined;
  setBoundingBox2dRequest(value?: BoundingBox2dRequest): void;

  getTagsMap(): jspb.Map<string, string>;
  clearTagsMap(): void;
  clearResponsesList(): void;
  getResponsesList(): Array<InterventionResponse>;
  setResponsesList(value: Array<InterventionResponse>): void;
  addResponses(value?: InterventionResponse, index?: number): InterventionResponse;

  getDataCase(): InterventionRequest.DataCase;
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): InterventionRequest.AsObject;
  static toObject(includeInstance: boolean, msg: InterventionRequest): InterventionRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: InterventionRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): InterventionRequest;
  static deserializeBinaryFromReader(message: InterventionRequest, reader: jspb.BinaryReader): InterventionRequest;
}

export namespace InterventionRequest {
  export type AsObject = {
    id: string,
    timestamp: number,
    severity: Severity,
    selectionRequest?: SelectionRequest.AsObject,
    boundingBox2dRequest?: BoundingBox2dRequest.AsObject,
    tagsMap: Array<[string, string]>,
    responsesList: Array<InterventionResponse.AsObject>,
  }

  export enum DataCase {
    DATA_NOT_SET = 0,
    SELECTION_REQUEST = 4,
    BOUNDING_BOX_2D_REQUEST = 5,
  }
}

export class InterventionResponse extends jspb.Message {
  getId(): string;
  setId(value: string): void;

  getRequestId(): string;
  setRequestId(value: string): void;

  getTimestamp(): number;
  setTimestamp(value: number): void;

  hasSelectionResponse(): boolean;
  clearSelectionResponse(): void;
  getSelectionResponse(): SelectionResponse | undefined;
  setSelectionResponse(value?: SelectionResponse): void;

  hasBoundingBox2dResponse(): boolean;
  clearBoundingBox2dResponse(): void;
  getBoundingBox2dResponse(): BoundingBox2dResponse | undefined;
  setBoundingBox2dResponse(value?: BoundingBox2dResponse): void;

  getDataCase(): InterventionResponse.DataCase;
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): InterventionResponse.AsObject;
  static toObject(includeInstance: boolean, msg: InterventionResponse): InterventionResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: InterventionResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): InterventionResponse;
  static deserializeBinaryFromReader(message: InterventionResponse, reader: jspb.BinaryReader): InterventionResponse;
}

export namespace InterventionResponse {
  export type AsObject = {
    id: string,
    requestId: string,
    timestamp: number,
    selectionResponse?: SelectionResponse.AsObject,
    boundingBox2dResponse?: BoundingBox2dResponse.AsObject,
  }

  export enum DataCase {
    DATA_NOT_SET = 0,
    SELECTION_RESPONSE = 4,
    BOUNDING_BOX_2D_RESPONSE = 5,
  }
}

export class BoundingBox2d extends jspb.Message {
  getX(): number;
  setX(value: number): void;

  getY(): number;
  setY(value: number): void;

  getWidth(): number;
  setWidth(value: number): void;

  getHeight(): number;
  setHeight(value: number): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): BoundingBox2d.AsObject;
  static toObject(includeInstance: boolean, msg: BoundingBox2d): BoundingBox2d.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: BoundingBox2d, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): BoundingBox2d;
  static deserializeBinaryFromReader(message: BoundingBox2d, reader: jspb.BinaryReader): BoundingBox2d;
}

export namespace BoundingBox2d {
  export type AsObject = {
    x: number,
    y: number,
    width: number,
    height: number,
  }
}

export class BoundingBox2dRequest extends jspb.Message {
  hasImage(): boolean;
  clearImage(): void;
  getImage(): Image | undefined;
  setImage(value?: Image): void;

  getInstruction(): string;
  setInstruction(value: string): void;

  clearHintList(): void;
  getHintList(): Array<BoundingBox2d>;
  setHintList(value: Array<BoundingBox2d>): void;
  addHint(value?: BoundingBox2d, index?: number): BoundingBox2d;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): BoundingBox2dRequest.AsObject;
  static toObject(includeInstance: boolean, msg: BoundingBox2dRequest): BoundingBox2dRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: BoundingBox2dRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): BoundingBox2dRequest;
  static deserializeBinaryFromReader(message: BoundingBox2dRequest, reader: jspb.BinaryReader): BoundingBox2dRequest;
}

export namespace BoundingBox2dRequest {
  export type AsObject = {
    image?: Image.AsObject,
    instruction: string,
    hintList: Array<BoundingBox2d.AsObject>,
  }
}

export class BoundingBox2dResponse extends jspb.Message {
  clearValueList(): void;
  getValueList(): Array<BoundingBox2d>;
  setValueList(value: Array<BoundingBox2d>): void;
  addValue(value?: BoundingBox2d, index?: number): BoundingBox2d;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): BoundingBox2dResponse.AsObject;
  static toObject(includeInstance: boolean, msg: BoundingBox2dResponse): BoundingBox2dResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: BoundingBox2dResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): BoundingBox2dResponse;
  static deserializeBinaryFromReader(message: BoundingBox2dResponse, reader: jspb.BinaryReader): BoundingBox2dResponse;
}

export namespace BoundingBox2dResponse {
  export type AsObject = {
    valueList: Array<BoundingBox2d.AsObject>,
  }
}

export class SelectionRequest extends jspb.Message {
  hasImage(): boolean;
  clearImage(): void;
  getImage(): Image | undefined;
  setImage(value?: Image): void;

  getInstruction(): string;
  setInstruction(value: string): void;

  clearOptionsList(): void;
  getOptionsList(): Array<string>;
  setOptionsList(value: Array<string>): void;
  addOptions(value: string, index?: number): string;

  getHint(): number;
  setHint(value: number): void;

  getDataCase(): SelectionRequest.DataCase;
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SelectionRequest.AsObject;
  static toObject(includeInstance: boolean, msg: SelectionRequest): SelectionRequest.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SelectionRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SelectionRequest;
  static deserializeBinaryFromReader(message: SelectionRequest, reader: jspb.BinaryReader): SelectionRequest;
}

export namespace SelectionRequest {
  export type AsObject = {
    image?: Image.AsObject,
    instruction: string,
    optionsList: Array<string>,
    hint: number,
  }

  export enum DataCase {
    DATA_NOT_SET = 0,
    IMAGE = 1,
  }
}

export class SelectionResponse extends jspb.Message {
  getValue(): number;
  setValue(value: number): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SelectionResponse.AsObject;
  static toObject(includeInstance: boolean, msg: SelectionResponse): SelectionResponse.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: SelectionResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SelectionResponse;
  static deserializeBinaryFromReader(message: SelectionResponse, reader: jspb.BinaryReader): SelectionResponse;
}

export namespace SelectionResponse {
  export type AsObject = {
    value: number,
  }
}

export class Datapoint extends jspb.Message {
  getStream(): string;
  setStream(value: string): void;

  getTimestamp(): number;
  setTimestamp(value: number): void;

  hasText(): boolean;
  clearText(): void;
  getText(): Text | undefined;
  setText(value?: Text): void;

  hasNumeric(): boolean;
  clearNumeric(): void;
  getNumeric(): Numeric | undefined;
  setNumeric(value?: Numeric): void;

  hasFile(): boolean;
  clearFile(): void;
  getFile(): File | undefined;
  setFile(value?: File): void;

  hasImage(): boolean;
  clearImage(): void;
  getImage(): Image | undefined;
  setImage(value?: Image): void;

  hasVideo(): boolean;
  clearVideo(): void;
  getVideo(): Video | undefined;
  setVideo(value?: Video): void;

  hasPointCloud(): boolean;
  clearPointCloud(): void;
  getPointCloud(): PointCloud | undefined;
  setPointCloud(value?: PointCloud): void;

  hasLocation(): boolean;
  clearLocation(): void;
  getLocation(): Location | undefined;
  setLocation(value?: Location): void;

  hasRosMessage(): boolean;
  clearRosMessage(): void;
  getRosMessage(): ROSMessage | undefined;
  setRosMessage(value?: ROSMessage): void;

  getDataCase(): Datapoint.DataCase;
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Datapoint.AsObject;
  static toObject(includeInstance: boolean, msg: Datapoint): Datapoint.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Datapoint, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Datapoint;
  static deserializeBinaryFromReader(message: Datapoint, reader: jspb.BinaryReader): Datapoint;
}

export namespace Datapoint {
  export type AsObject = {
    stream: string,
    timestamp: number,
    text?: Text.AsObject,
    numeric?: Numeric.AsObject,
    file?: File.AsObject,
    image?: Image.AsObject,
    video?: Video.AsObject,
    pointCloud?: PointCloud.AsObject,
    location?: Location.AsObject,
    rosMessage?: ROSMessage.AsObject,
  }

  export enum DataCase {
    DATA_NOT_SET = 0,
    TEXT = 3,
    NUMERIC = 4,
    FILE = 5,
    IMAGE = 6,
    VIDEO = 7,
    POINT_CLOUD = 8,
    LOCATION = 9,
    ROS_MESSAGE = 10,
  }
}

export class Text extends jspb.Message {
  getValue(): string;
  setValue(value: string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Text.AsObject;
  static toObject(includeInstance: boolean, msg: Text): Text.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Text, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Text;
  static deserializeBinaryFromReader(message: Text, reader: jspb.BinaryReader): Text;
}

export namespace Text {
  export type AsObject = {
    value: string,
  }
}

export class Numeric extends jspb.Message {
  getValue(): number;
  setValue(value: number): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Numeric.AsObject;
  static toObject(includeInstance: boolean, msg: Numeric): Numeric.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Numeric, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Numeric;
  static deserializeBinaryFromReader(message: Numeric, reader: jspb.BinaryReader): Numeric;
}

export namespace Numeric {
  export type AsObject = {
    value: number,
  }
}

export class File extends jspb.Message {
  hasUrl(): boolean;
  clearUrl(): void;
  getUrl(): string;
  setUrl(value: string): void;

  hasRaw(): boolean;
  clearRaw(): void;
  getRaw(): Uint8Array | string;
  getRaw_asU8(): Uint8Array;
  getRaw_asB64(): string;
  setRaw(value: Uint8Array | string): void;

  getFilename(): string;
  setFilename(value: string): void;

  getSize(): number;
  setSize(value: number): void;

  getDataCase(): File.DataCase;
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): File.AsObject;
  static toObject(includeInstance: boolean, msg: File): File.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: File, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): File;
  static deserializeBinaryFromReader(message: File, reader: jspb.BinaryReader): File;
}

export namespace File {
  export type AsObject = {
    url: string,
    raw: Uint8Array | string,
    filename: string,
    size: number,
  }

  export enum DataCase {
    DATA_NOT_SET = 0,
    URL = 1,
    RAW = 2,
  }
}

export class Image extends jspb.Message {
  getContentType(): string;
  setContentType(value: string): void;

  hasUrl(): boolean;
  clearUrl(): void;
  getUrl(): string;
  setUrl(value: string): void;

  hasRaw(): boolean;
  clearRaw(): void;
  getRaw(): Uint8Array | string;
  getRaw_asU8(): Uint8Array;
  getRaw_asB64(): string;
  setRaw(value: Uint8Array | string): void;

  getDataCase(): Image.DataCase;
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Image.AsObject;
  static toObject(includeInstance: boolean, msg: Image): Image.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Image, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Image;
  static deserializeBinaryFromReader(message: Image, reader: jspb.BinaryReader): Image;
}

export namespace Image {
  export type AsObject = {
    contentType: string,
    url: string,
    raw: Uint8Array | string,
  }

  export enum DataCase {
    DATA_NOT_SET = 0,
    URL = 2,
    RAW = 3,
  }
}

export class Video extends jspb.Message {
  getContentType(): string;
  setContentType(value: string): void;

  hasUrl(): boolean;
  clearUrl(): void;
  getUrl(): string;
  setUrl(value: string): void;

  hasRaw(): boolean;
  clearRaw(): void;
  getRaw(): Uint8Array | string;
  getRaw_asU8(): Uint8Array;
  getRaw_asB64(): string;
  setRaw(value: Uint8Array | string): void;

  getDataCase(): Video.DataCase;
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Video.AsObject;
  static toObject(includeInstance: boolean, msg: Video): Video.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Video, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Video;
  static deserializeBinaryFromReader(message: Video, reader: jspb.BinaryReader): Video;
}

export namespace Video {
  export type AsObject = {
    contentType: string,
    url: string,
    raw: Uint8Array | string,
  }

  export enum DataCase {
    DATA_NOT_SET = 0,
    URL = 2,
    RAW = 3,
  }
}

export class PointCloud extends jspb.Message {
  hasUrl(): boolean;
  clearUrl(): void;
  getUrl(): string;
  setUrl(value: string): void;

  hasRaw(): boolean;
  clearRaw(): void;
  getRaw(): Uint8Array | string;
  getRaw_asU8(): Uint8Array;
  getRaw_asB64(): string;
  setRaw(value: Uint8Array | string): void;

  getDataCase(): PointCloud.DataCase;
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): PointCloud.AsObject;
  static toObject(includeInstance: boolean, msg: PointCloud): PointCloud.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: PointCloud, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): PointCloud;
  static deserializeBinaryFromReader(message: PointCloud, reader: jspb.BinaryReader): PointCloud;
}

export namespace PointCloud {
  export type AsObject = {
    url: string,
    raw: Uint8Array | string,
  }

  export enum DataCase {
    DATA_NOT_SET = 0,
    URL = 1,
    RAW = 2,
  }
}

export class Location extends jspb.Message {
  getLatitude(): number;
  setLatitude(value: number): void;

  getLongitude(): number;
  setLongitude(value: number): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Location.AsObject;
  static toObject(includeInstance: boolean, msg: Location): Location.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: Location, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Location;
  static deserializeBinaryFromReader(message: Location, reader: jspb.BinaryReader): Location;
}

export namespace Location {
  export type AsObject = {
    latitude: number,
    longitude: number,
  }
}

export class ROSMessage extends jspb.Message {
  getRaw(): Uint8Array | string;
  getRaw_asU8(): Uint8Array;
  getRaw_asB64(): string;
  setRaw(value: Uint8Array | string): void;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ROSMessage.AsObject;
  static toObject(includeInstance: boolean, msg: ROSMessage): ROSMessage.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ROSMessage, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ROSMessage;
  static deserializeBinaryFromReader(message: ROSMessage, reader: jspb.BinaryReader): ROSMessage;
}

export namespace ROSMessage {
  export type AsObject = {
    raw: Uint8Array | string,
  }
}

export class ROSTopic extends jspb.Message {
  getName(): string;
  setName(value: string): void;

  getDataType(): string;
  setDataType(value: string): void;

  getMsgDesc(): string;
  setMsgDesc(value: string): void;

  getTagsMap(): jspb.Map<string, string>;
  clearTagsMap(): void;
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ROSTopic.AsObject;
  static toObject(includeInstance: boolean, msg: ROSTopic): ROSTopic.AsObject;
  static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
  static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
  static serializeBinaryToWriter(message: ROSTopic, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ROSTopic;
  static deserializeBinaryFromReader(message: ROSTopic, reader: jspb.BinaryReader): ROSTopic;
}

export namespace ROSTopic {
  export type AsObject = {
    name: string,
    dataType: string,
    msgDesc: string,
    tagsMap: Array<[string, string]>,
  }
}

export enum Severity {
  INFO = 0,
  WARNING = 1,
  ERROR = 2,
  CRITICAL = 3,
}

