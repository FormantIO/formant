# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/model/v1/datapoint.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protos.model.v1 import file_pb2 as protos_dot_model_dot_v1_dot_file__pb2
from protos.model.v1 import health_pb2 as protos_dot_model_dot_v1_dot_health__pb2
from protos.model.v1 import math_pb2 as protos_dot_model_dot_v1_dot_math__pb2
from protos.model.v1 import navigation_pb2 as protos_dot_model_dot_v1_dot_navigation__pb2
from protos.model.v1 import text_pb2 as protos_dot_model_dot_v1_dot_text__pb2
from protos.model.v1 import media_pb2 as protos_dot_model_dot_v1_dot_media__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/model/v1/datapoint.proto',
  package='v1.model',
  syntax='proto3',
  serialized_options=b'Z)github.com/FormantIO/genproto/go/v1/model',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1fprotos/model/v1/datapoint.proto\x12\x08v1.model\x1a\x1aprotos/model/v1/file.proto\x1a\x1cprotos/model/v1/health.proto\x1a\x1aprotos/model/v1/math.proto\x1a protos/model/v1/navigation.proto\x1a\x1aprotos/model/v1/text.proto\x1a\x1bprotos/model/v1/media.proto\"\xea\x05\n\tDatapoint\x12\x0e\n\x06stream\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\x03\x12+\n\x04tags\x18\x03 \x03(\x0b\x32\x1d.v1.model.Datapoint.TagsEntry\x12\x1e\n\x04text\x18\x04 \x01(\x0b\x32\x0e.v1.model.TextH\x00\x12$\n\x07numeric\x18\x05 \x01(\x0b\x32\x11.v1.model.NumericH\x00\x12+\n\x0bnumeric_set\x18\x11 \x01(\x0b\x32\x14.v1.model.NumericSetH\x00\x12\"\n\x06\x62itset\x18\x07 \x01(\x0b\x32\x10.v1.model.BitsetH\x00\x12\x1e\n\x04\x66ile\x18\x08 \x01(\x0b\x32\x0e.v1.model.FileH\x00\x12 \n\x05image\x18\t \x01(\x0b\x32\x0f.v1.model.ImageH\x00\x12+\n\x0bpoint_cloud\x18\n \x01(\x0b\x32\x14.v1.model.PointCloudH\x00\x12&\n\x08location\x18\x0b \x01(\x0b\x32\x12.v1.model.LocationH\x00\x12.\n\x0clocalization\x18\x0c \x01(\x0b\x32\x16.v1.model.LocalizationH\x00\x12\"\n\x06health\x18\r \x01(\x0b\x32\x10.v1.model.HealthH\x00\x12\x1e\n\x04json\x18\x0e \x01(\x0b\x32\x0e.v1.model.JsonH\x00\x12$\n\x07\x62\x61ttery\x18\x0f \x01(\x0b\x32\x11.v1.model.BatteryH\x00\x12 \n\x05video\x18\x10 \x01(\x0b\x32\x0f.v1.model.VideoH\x00\x12\x31\n\x0etransform_tree\x18\x12 \x01(\x0b\x32\x17.v1.model.TransformTreeH\x00\x12&\n\x08odometry\x18\x13 \x01(\x0b\x32\x12.v1.model.OdometryH\x00\x12\r\n\x05label\x18\x14 \x01(\t\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x06\n\x04\x64\x61taJ\x04\x08\x06\x10\x07\"\xea\x02\n\x10\x43ontrolDatapoint\x12\x0e\n\x06stream\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\x03\x12\"\n\x06\x62itset\x18\x03 \x01(\x0b\x32\x10.v1.model.BitsetH\x00\x12 \n\x05twist\x18\x04 \x01(\x0b\x32\x0f.v1.model.TwistH\x00\x12#\n\x04pose\x18\x05 \x01(\x0b\x32\x13.v1.model.TransformH\x00\x12$\n\x07numeric\x18\x06 \x01(\x0b\x32\x11.v1.model.NumericH\x00\x12<\n\x14pose_with_covariance\x18\x07 \x01(\x0b\x32\x1c.v1.model.PoseWithCovarianceH\x00\x12 \n\x05point\x18\x08 \x01(\x0b\x32\x0f.v1.model.PointH\x00\x12\x1c\n\x03joy\x18\t \x01(\x0b\x32\r.v1.model.JoyH\x00\x12\x1c\n\x03\x62it\x18\n \x01(\x0b\x32\r.v1.model.BitH\x00\x42\x06\n\x04\x64\x61ta\"\x81\x02\n\x13GenericAPIDatapoint\x12\x0e\n\x06Method\x18\x01 \x01(\t\x12\x10\n\x08\x45ndpoint\x18\x02 \x01(\t\x12;\n\x07Headers\x18\x03 \x03(\x0b\x32*.v1.model.GenericAPIDatapoint.HeadersEntry\x12\x0c\n\x04\x42ody\x18\x04 \x01(\t\x12\x13\n\x0bIsRetryable\x18\x05 \x01(\x08\x12\x1a\n\x12RequireFormantAuth\x18\x06 \x01(\x08\x12\x1c\n\x14RetryableStatusCodes\x18\x07 \x03(\x03\x1a.\n\x0cHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42+Z)github.com/FormantIO/genproto/go/v1/modelb\x06proto3'
  ,
  dependencies=[protos_dot_model_dot_v1_dot_file__pb2.DESCRIPTOR,protos_dot_model_dot_v1_dot_health__pb2.DESCRIPTOR,protos_dot_model_dot_v1_dot_math__pb2.DESCRIPTOR,protos_dot_model_dot_v1_dot_navigation__pb2.DESCRIPTOR,protos_dot_model_dot_v1_dot_text__pb2.DESCRIPTOR,protos_dot_model_dot_v1_dot_media__pb2.DESCRIPTOR,])




_DATAPOINT_TAGSENTRY = _descriptor.Descriptor(
  name='TagsEntry',
  full_name='v1.model.Datapoint.TagsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='v1.model.Datapoint.TagsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='v1.model.Datapoint.TagsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=912,
  serialized_end=955,
)

_DATAPOINT = _descriptor.Descriptor(
  name='Datapoint',
  full_name='v1.model.Datapoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='stream', full_name='v1.model.Datapoint.stream', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='v1.model.Datapoint.timestamp', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tags', full_name='v1.model.Datapoint.tags', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text', full_name='v1.model.Datapoint.text', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='numeric', full_name='v1.model.Datapoint.numeric', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='numeric_set', full_name='v1.model.Datapoint.numeric_set', index=5,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bitset', full_name='v1.model.Datapoint.bitset', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='file', full_name='v1.model.Datapoint.file', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='image', full_name='v1.model.Datapoint.image', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='point_cloud', full_name='v1.model.Datapoint.point_cloud', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='location', full_name='v1.model.Datapoint.location', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='localization', full_name='v1.model.Datapoint.localization', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='health', full_name='v1.model.Datapoint.health', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='json', full_name='v1.model.Datapoint.json', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='battery', full_name='v1.model.Datapoint.battery', index=14,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='video', full_name='v1.model.Datapoint.video', index=15,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='transform_tree', full_name='v1.model.Datapoint.transform_tree', index=16,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='odometry', full_name='v1.model.Datapoint.odometry', index=17,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='label', full_name='v1.model.Datapoint.label', index=18,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_DATAPOINT_TAGSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='data', full_name='v1.model.Datapoint.data',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=223,
  serialized_end=969,
)


_CONTROLDATAPOINT = _descriptor.Descriptor(
  name='ControlDatapoint',
  full_name='v1.model.ControlDatapoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='stream', full_name='v1.model.ControlDatapoint.stream', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='v1.model.ControlDatapoint.timestamp', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bitset', full_name='v1.model.ControlDatapoint.bitset', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='twist', full_name='v1.model.ControlDatapoint.twist', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pose', full_name='v1.model.ControlDatapoint.pose', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='numeric', full_name='v1.model.ControlDatapoint.numeric', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pose_with_covariance', full_name='v1.model.ControlDatapoint.pose_with_covariance', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='point', full_name='v1.model.ControlDatapoint.point', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='joy', full_name='v1.model.ControlDatapoint.joy', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bit', full_name='v1.model.ControlDatapoint.bit', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
      name='data', full_name='v1.model.ControlDatapoint.data',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=972,
  serialized_end=1334,
)


_GENERICAPIDATAPOINT_HEADERSENTRY = _descriptor.Descriptor(
  name='HeadersEntry',
  full_name='v1.model.GenericAPIDatapoint.HeadersEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='v1.model.GenericAPIDatapoint.HeadersEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='v1.model.GenericAPIDatapoint.HeadersEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1548,
  serialized_end=1594,
)

_GENERICAPIDATAPOINT = _descriptor.Descriptor(
  name='GenericAPIDatapoint',
  full_name='v1.model.GenericAPIDatapoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Method', full_name='v1.model.GenericAPIDatapoint.Method', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Endpoint', full_name='v1.model.GenericAPIDatapoint.Endpoint', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Headers', full_name='v1.model.GenericAPIDatapoint.Headers', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Body', full_name='v1.model.GenericAPIDatapoint.Body', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='IsRetryable', full_name='v1.model.GenericAPIDatapoint.IsRetryable', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='RequireFormantAuth', full_name='v1.model.GenericAPIDatapoint.RequireFormantAuth', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='RetryableStatusCodes', full_name='v1.model.GenericAPIDatapoint.RetryableStatusCodes', index=6,
      number=7, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_GENERICAPIDATAPOINT_HEADERSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1337,
  serialized_end=1594,
)

_DATAPOINT_TAGSENTRY.containing_type = _DATAPOINT
_DATAPOINT.fields_by_name['tags'].message_type = _DATAPOINT_TAGSENTRY
_DATAPOINT.fields_by_name['text'].message_type = protos_dot_model_dot_v1_dot_text__pb2._TEXT
_DATAPOINT.fields_by_name['numeric'].message_type = protos_dot_model_dot_v1_dot_math__pb2._NUMERIC
_DATAPOINT.fields_by_name['numeric_set'].message_type = protos_dot_model_dot_v1_dot_math__pb2._NUMERICSET
_DATAPOINT.fields_by_name['bitset'].message_type = protos_dot_model_dot_v1_dot_math__pb2._BITSET
_DATAPOINT.fields_by_name['file'].message_type = protos_dot_model_dot_v1_dot_file__pb2._FILE
_DATAPOINT.fields_by_name['image'].message_type = protos_dot_model_dot_v1_dot_media__pb2._IMAGE
_DATAPOINT.fields_by_name['point_cloud'].message_type = protos_dot_model_dot_v1_dot_media__pb2._POINTCLOUD
_DATAPOINT.fields_by_name['location'].message_type = protos_dot_model_dot_v1_dot_navigation__pb2._LOCATION
_DATAPOINT.fields_by_name['localization'].message_type = protos_dot_model_dot_v1_dot_navigation__pb2._LOCALIZATION
_DATAPOINT.fields_by_name['health'].message_type = protos_dot_model_dot_v1_dot_health__pb2._HEALTH
_DATAPOINT.fields_by_name['json'].message_type = protos_dot_model_dot_v1_dot_text__pb2._JSON
_DATAPOINT.fields_by_name['battery'].message_type = protos_dot_model_dot_v1_dot_health__pb2._BATTERY
_DATAPOINT.fields_by_name['video'].message_type = protos_dot_model_dot_v1_dot_media__pb2._VIDEO
_DATAPOINT.fields_by_name['transform_tree'].message_type = protos_dot_model_dot_v1_dot_media__pb2._TRANSFORMTREE
_DATAPOINT.fields_by_name['odometry'].message_type = protos_dot_model_dot_v1_dot_navigation__pb2._ODOMETRY
_DATAPOINT.oneofs_by_name['data'].fields.append(
  _DATAPOINT.fields_by_name['text'])
_DATAPOINT.fields_by_name['text'].containing_oneof = _DATAPOINT.oneofs_by_name['data']
_DATAPOINT.oneofs_by_name['data'].fields.append(
  _DATAPOINT.fields_by_name['numeric'])
_DATAPOINT.fields_by_name['numeric'].containing_oneof = _DATAPOINT.oneofs_by_name['data']
_DATAPOINT.oneofs_by_name['data'].fields.append(
  _DATAPOINT.fields_by_name['numeric_set'])
_DATAPOINT.fields_by_name['numeric_set'].containing_oneof = _DATAPOINT.oneofs_by_name['data']
_DATAPOINT.oneofs_by_name['data'].fields.append(
  _DATAPOINT.fields_by_name['bitset'])
_DATAPOINT.fields_by_name['bitset'].containing_oneof = _DATAPOINT.oneofs_by_name['data']
_DATAPOINT.oneofs_by_name['data'].fields.append(
  _DATAPOINT.fields_by_name['file'])
_DATAPOINT.fields_by_name['file'].containing_oneof = _DATAPOINT.oneofs_by_name['data']
_DATAPOINT.oneofs_by_name['data'].fields.append(
  _DATAPOINT.fields_by_name['image'])
_DATAPOINT.fields_by_name['image'].containing_oneof = _DATAPOINT.oneofs_by_name['data']
_DATAPOINT.oneofs_by_name['data'].fields.append(
  _DATAPOINT.fields_by_name['point_cloud'])
_DATAPOINT.fields_by_name['point_cloud'].containing_oneof = _DATAPOINT.oneofs_by_name['data']
_DATAPOINT.oneofs_by_name['data'].fields.append(
  _DATAPOINT.fields_by_name['location'])
_DATAPOINT.fields_by_name['location'].containing_oneof = _DATAPOINT.oneofs_by_name['data']
_DATAPOINT.oneofs_by_name['data'].fields.append(
  _DATAPOINT.fields_by_name['localization'])
_DATAPOINT.fields_by_name['localization'].containing_oneof = _DATAPOINT.oneofs_by_name['data']
_DATAPOINT.oneofs_by_name['data'].fields.append(
  _DATAPOINT.fields_by_name['health'])
_DATAPOINT.fields_by_name['health'].containing_oneof = _DATAPOINT.oneofs_by_name['data']
_DATAPOINT.oneofs_by_name['data'].fields.append(
  _DATAPOINT.fields_by_name['json'])
_DATAPOINT.fields_by_name['json'].containing_oneof = _DATAPOINT.oneofs_by_name['data']
_DATAPOINT.oneofs_by_name['data'].fields.append(
  _DATAPOINT.fields_by_name['battery'])
_DATAPOINT.fields_by_name['battery'].containing_oneof = _DATAPOINT.oneofs_by_name['data']
_DATAPOINT.oneofs_by_name['data'].fields.append(
  _DATAPOINT.fields_by_name['video'])
_DATAPOINT.fields_by_name['video'].containing_oneof = _DATAPOINT.oneofs_by_name['data']
_DATAPOINT.oneofs_by_name['data'].fields.append(
  _DATAPOINT.fields_by_name['transform_tree'])
_DATAPOINT.fields_by_name['transform_tree'].containing_oneof = _DATAPOINT.oneofs_by_name['data']
_DATAPOINT.oneofs_by_name['data'].fields.append(
  _DATAPOINT.fields_by_name['odometry'])
_DATAPOINT.fields_by_name['odometry'].containing_oneof = _DATAPOINT.oneofs_by_name['data']
_CONTROLDATAPOINT.fields_by_name['bitset'].message_type = protos_dot_model_dot_v1_dot_math__pb2._BITSET
_CONTROLDATAPOINT.fields_by_name['twist'].message_type = protos_dot_model_dot_v1_dot_math__pb2._TWIST
_CONTROLDATAPOINT.fields_by_name['pose'].message_type = protos_dot_model_dot_v1_dot_math__pb2._TRANSFORM
_CONTROLDATAPOINT.fields_by_name['numeric'].message_type = protos_dot_model_dot_v1_dot_math__pb2._NUMERIC
_CONTROLDATAPOINT.fields_by_name['pose_with_covariance'].message_type = protos_dot_model_dot_v1_dot_navigation__pb2._POSEWITHCOVARIANCE
_CONTROLDATAPOINT.fields_by_name['point'].message_type = protos_dot_model_dot_v1_dot_math__pb2._POINT
_CONTROLDATAPOINT.fields_by_name['joy'].message_type = protos_dot_model_dot_v1_dot_navigation__pb2._JOY
_CONTROLDATAPOINT.fields_by_name['bit'].message_type = protos_dot_model_dot_v1_dot_math__pb2._BIT
_CONTROLDATAPOINT.oneofs_by_name['data'].fields.append(
  _CONTROLDATAPOINT.fields_by_name['bitset'])
_CONTROLDATAPOINT.fields_by_name['bitset'].containing_oneof = _CONTROLDATAPOINT.oneofs_by_name['data']
_CONTROLDATAPOINT.oneofs_by_name['data'].fields.append(
  _CONTROLDATAPOINT.fields_by_name['twist'])
_CONTROLDATAPOINT.fields_by_name['twist'].containing_oneof = _CONTROLDATAPOINT.oneofs_by_name['data']
_CONTROLDATAPOINT.oneofs_by_name['data'].fields.append(
  _CONTROLDATAPOINT.fields_by_name['pose'])
_CONTROLDATAPOINT.fields_by_name['pose'].containing_oneof = _CONTROLDATAPOINT.oneofs_by_name['data']
_CONTROLDATAPOINT.oneofs_by_name['data'].fields.append(
  _CONTROLDATAPOINT.fields_by_name['numeric'])
_CONTROLDATAPOINT.fields_by_name['numeric'].containing_oneof = _CONTROLDATAPOINT.oneofs_by_name['data']
_CONTROLDATAPOINT.oneofs_by_name['data'].fields.append(
  _CONTROLDATAPOINT.fields_by_name['pose_with_covariance'])
_CONTROLDATAPOINT.fields_by_name['pose_with_covariance'].containing_oneof = _CONTROLDATAPOINT.oneofs_by_name['data']
_CONTROLDATAPOINT.oneofs_by_name['data'].fields.append(
  _CONTROLDATAPOINT.fields_by_name['point'])
_CONTROLDATAPOINT.fields_by_name['point'].containing_oneof = _CONTROLDATAPOINT.oneofs_by_name['data']
_CONTROLDATAPOINT.oneofs_by_name['data'].fields.append(
  _CONTROLDATAPOINT.fields_by_name['joy'])
_CONTROLDATAPOINT.fields_by_name['joy'].containing_oneof = _CONTROLDATAPOINT.oneofs_by_name['data']
_CONTROLDATAPOINT.oneofs_by_name['data'].fields.append(
  _CONTROLDATAPOINT.fields_by_name['bit'])
_CONTROLDATAPOINT.fields_by_name['bit'].containing_oneof = _CONTROLDATAPOINT.oneofs_by_name['data']
_GENERICAPIDATAPOINT_HEADERSENTRY.containing_type = _GENERICAPIDATAPOINT
_GENERICAPIDATAPOINT.fields_by_name['Headers'].message_type = _GENERICAPIDATAPOINT_HEADERSENTRY
DESCRIPTOR.message_types_by_name['Datapoint'] = _DATAPOINT
DESCRIPTOR.message_types_by_name['ControlDatapoint'] = _CONTROLDATAPOINT
DESCRIPTOR.message_types_by_name['GenericAPIDatapoint'] = _GENERICAPIDATAPOINT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Datapoint = _reflection.GeneratedProtocolMessageType('Datapoint', (_message.Message,), {

  'TagsEntry' : _reflection.GeneratedProtocolMessageType('TagsEntry', (_message.Message,), {
    'DESCRIPTOR' : _DATAPOINT_TAGSENTRY,
    '__module__' : 'protos.model.v1.datapoint_pb2'
    # @@protoc_insertion_point(class_scope:v1.model.Datapoint.TagsEntry)
    })
  ,
  'DESCRIPTOR' : _DATAPOINT,
  '__module__' : 'protos.model.v1.datapoint_pb2'
  # @@protoc_insertion_point(class_scope:v1.model.Datapoint)
  })
_sym_db.RegisterMessage(Datapoint)
_sym_db.RegisterMessage(Datapoint.TagsEntry)

ControlDatapoint = _reflection.GeneratedProtocolMessageType('ControlDatapoint', (_message.Message,), {
  'DESCRIPTOR' : _CONTROLDATAPOINT,
  '__module__' : 'protos.model.v1.datapoint_pb2'
  # @@protoc_insertion_point(class_scope:v1.model.ControlDatapoint)
  })
_sym_db.RegisterMessage(ControlDatapoint)

GenericAPIDatapoint = _reflection.GeneratedProtocolMessageType('GenericAPIDatapoint', (_message.Message,), {

  'HeadersEntry' : _reflection.GeneratedProtocolMessageType('HeadersEntry', (_message.Message,), {
    'DESCRIPTOR' : _GENERICAPIDATAPOINT_HEADERSENTRY,
    '__module__' : 'protos.model.v1.datapoint_pb2'
    # @@protoc_insertion_point(class_scope:v1.model.GenericAPIDatapoint.HeadersEntry)
    })
  ,
  'DESCRIPTOR' : _GENERICAPIDATAPOINT,
  '__module__' : 'protos.model.v1.datapoint_pb2'
  # @@protoc_insertion_point(class_scope:v1.model.GenericAPIDatapoint)
  })
_sym_db.RegisterMessage(GenericAPIDatapoint)
_sym_db.RegisterMessage(GenericAPIDatapoint.HeadersEntry)


DESCRIPTOR._options = None
_DATAPOINT_TAGSENTRY._options = None
_GENERICAPIDATAPOINT_HEADERSENTRY._options = None
# @@protoc_insertion_point(module_scope)
