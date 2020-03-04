# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/model/v1/media.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/model/v1/media.proto',
  package='v1.model',
  syntax='proto3',
  serialized_options=b'Z)github.com/FormantIO/genproto/go/v1/model',
  serialized_pb=b'\n\x1bprotos/model/v1/media.proto\x12\x08v1.model\"Z\n\x05Image\x12!\n\x0c\x63ontent_type\x18\x01 \x01(\tR\x0b\x63ontentType\x12\x12\n\x03url\x18\x02 \x01(\tH\x00R\x03url\x12\x12\n\x03raw\x18\x03 \x01(\x0cH\x00R\x03rawB\x06\n\x04\x64\x61ta\"<\n\nPointCloud\x12\x12\n\x03url\x18\x01 \x01(\tH\x00R\x03url\x12\x12\n\x03raw\x18\x02 \x01(\x0cH\x00R\x03rawB\x06\n\x04\x64\x61taB+Z)github.com/FormantIO/genproto/go/v1/modelb\x06proto3'
)




_IMAGE = _descriptor.Descriptor(
  name='Image',
  full_name='v1.model.Image',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='content_type', full_name='v1.model.Image.content_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='contentType', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='v1.model.Image.url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='url', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='raw', full_name='v1.model.Image.raw', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='raw', file=DESCRIPTOR),
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
      name='data', full_name='v1.model.Image.data',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=41,
  serialized_end=131,
)


_POINTCLOUD = _descriptor.Descriptor(
  name='PointCloud',
  full_name='v1.model.PointCloud',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='v1.model.PointCloud.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='url', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='raw', full_name='v1.model.PointCloud.raw', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='raw', file=DESCRIPTOR),
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
      name='data', full_name='v1.model.PointCloud.data',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=133,
  serialized_end=193,
)

_IMAGE.oneofs_by_name['data'].fields.append(
  _IMAGE.fields_by_name['url'])
_IMAGE.fields_by_name['url'].containing_oneof = _IMAGE.oneofs_by_name['data']
_IMAGE.oneofs_by_name['data'].fields.append(
  _IMAGE.fields_by_name['raw'])
_IMAGE.fields_by_name['raw'].containing_oneof = _IMAGE.oneofs_by_name['data']
_POINTCLOUD.oneofs_by_name['data'].fields.append(
  _POINTCLOUD.fields_by_name['url'])
_POINTCLOUD.fields_by_name['url'].containing_oneof = _POINTCLOUD.oneofs_by_name['data']
_POINTCLOUD.oneofs_by_name['data'].fields.append(
  _POINTCLOUD.fields_by_name['raw'])
_POINTCLOUD.fields_by_name['raw'].containing_oneof = _POINTCLOUD.oneofs_by_name['data']
DESCRIPTOR.message_types_by_name['Image'] = _IMAGE
DESCRIPTOR.message_types_by_name['PointCloud'] = _POINTCLOUD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Image = _reflection.GeneratedProtocolMessageType('Image', (_message.Message,), {
  'DESCRIPTOR' : _IMAGE,
  '__module__' : 'protos.model.v1.media_pb2'
  # @@protoc_insertion_point(class_scope:v1.model.Image)
  })
_sym_db.RegisterMessage(Image)

PointCloud = _reflection.GeneratedProtocolMessageType('PointCloud', (_message.Message,), {
  'DESCRIPTOR' : _POINTCLOUD,
  '__module__' : 'protos.model.v1.media_pb2'
  # @@protoc_insertion_point(class_scope:v1.model.PointCloud)
  })
_sym_db.RegisterMessage(PointCloud)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
