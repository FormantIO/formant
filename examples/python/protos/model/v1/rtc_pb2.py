# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/model/v1/rtc.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protos.model.v1 import math_pb2 as protos_dot_model_dot_v1_dot_math__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/model/v1/rtc.proto',
  package='v1.model',
  syntax='proto3',
  serialized_options=b'Z)github.com/FormantIO/genproto/go/v1/model',
  serialized_pb=b'\n\x19protos/model/v1/rtc.proto\x12\x08v1.model\x1a\x1aprotos/model/v1/math.proto\"\xb6\x01\n\nRTCMessage\x12\x16\n\x06stream\x18\x01 \x01(\tR\x06stream\x12\x1c\n\ttimestamp\x18\x02 \x01(\x03R\ttimestamp\x12\'\n\x05twist\x18\x03 \x01(\x0b\x32\x0f.v1.model.TwistH\x00R\x05twist\x12\x14\n\x04\x62ool\x18\x04 \x01(\x08H\x00R\x04\x62ool\x12+\n\x10\x63ompressed_image\x18\x05 \x01(\x0cH\x00R\x0f\x63ompressedImageB\x06\n\x04\x64\x61taB+Z)github.com/FormantIO/genproto/go/v1/modelb\x06proto3'
  ,
  dependencies=[protos_dot_model_dot_v1_dot_math__pb2.DESCRIPTOR,])




_RTCMESSAGE = _descriptor.Descriptor(
  name='RTCMessage',
  full_name='v1.model.RTCMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stream', full_name='v1.model.RTCMessage.stream', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='stream', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='v1.model.RTCMessage.timestamp', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='timestamp', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='twist', full_name='v1.model.RTCMessage.twist', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='twist', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bool', full_name='v1.model.RTCMessage.bool', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='bool', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='compressed_image', full_name='v1.model.RTCMessage.compressed_image', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='compressedImage', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='data', full_name='v1.model.RTCMessage.data',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=68,
  serialized_end=250,
)

_RTCMESSAGE.fields_by_name['twist'].message_type = protos_dot_model_dot_v1_dot_math__pb2._TWIST
_RTCMESSAGE.oneofs_by_name['data'].fields.append(
  _RTCMESSAGE.fields_by_name['twist'])
_RTCMESSAGE.fields_by_name['twist'].containing_oneof = _RTCMESSAGE.oneofs_by_name['data']
_RTCMESSAGE.oneofs_by_name['data'].fields.append(
  _RTCMESSAGE.fields_by_name['bool'])
_RTCMESSAGE.fields_by_name['bool'].containing_oneof = _RTCMESSAGE.oneofs_by_name['data']
_RTCMESSAGE.oneofs_by_name['data'].fields.append(
  _RTCMESSAGE.fields_by_name['compressed_image'])
_RTCMESSAGE.fields_by_name['compressed_image'].containing_oneof = _RTCMESSAGE.oneofs_by_name['data']
DESCRIPTOR.message_types_by_name['RTCMessage'] = _RTCMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RTCMessage = _reflection.GeneratedProtocolMessageType('RTCMessage', (_message.Message,), {
  'DESCRIPTOR' : _RTCMESSAGE,
  '__module__' : 'protos.model.v1.rtc_pb2'
  # @@protoc_insertion_point(class_scope:v1.model.RTCMessage)
  })
_sym_db.RegisterMessage(RTCMessage)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
