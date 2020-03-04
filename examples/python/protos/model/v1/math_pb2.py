# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/model/v1/math.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/model/v1/math.proto',
  package='v1.model',
  syntax='proto3',
  serialized_options=b'Z)github.com/FormantIO/genproto/go/v1/model',
  serialized_pb=b'\n\x1aprotos/model/v1/math.proto\x12\x08v1.model\"\x1f\n\x07Numeric\x12\x14\n\x05value\x18\x01 \x01(\x01R\x05value\"7\n\tMetricSet\x12*\n\x07metrics\x18\x01 \x03(\x0b\x32\x10.v1.model.MetricR\x07metrics\"2\n\x06Metric\x12\x14\n\x05value\x18\x01 \x01(\x01R\x05value\x12\x12\n\x04unit\x18\x02 \x01(\tR\x04unit\"-\n\x03\x42it\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x08R\x05value\"+\n\x06\x42itset\x12!\n\x04\x62its\x18\x01 \x03(\x0b\x32\r.v1.model.BitR\x04\x62its\"_\n\x05Twist\x12)\n\x06linear\x18\x01 \x01(\x0b\x32\x11.v1.model.Vector3R\x06linear\x12+\n\x07\x61ngular\x18\x02 \x01(\x0b\x32\x11.v1.model.Vector3R\x07\x61ngular\"r\n\tTransform\x12\x33\n\x0btranslation\x18\x01 \x01(\x0b\x32\x11.v1.model.Vector3R\x0btranslation\x12\x30\n\x08rotation\x18\x02 \x01(\x0b\x32\x14.v1.model.QuaternionR\x08rotation\"\x87\x01\n\x0eTransformFrame\x12!\n\x0cparent_frame\x18\x01 \x01(\tR\x0bparentFrame\x12\x1f\n\x0b\x63hild_frame\x18\x02 \x01(\tR\nchildFrame\x12\x31\n\ttransform\x18\x03 \x01(\x0b\x32\x13.v1.model.TransformR\ttransform\"3\n\x07Vector3\x12\x0c\n\x01x\x18\x01 \x01(\x01R\x01x\x12\x0c\n\x01y\x18\x02 \x01(\x01R\x01y\x12\x0c\n\x01z\x18\x03 \x01(\x01R\x01z\"D\n\nQuaternion\x12\x0c\n\x01x\x18\x01 \x01(\x01R\x01x\x12\x0c\n\x01y\x18\x02 \x01(\x01R\x01y\x12\x0c\n\x01z\x18\x03 \x01(\x01R\x01z\x12\x0c\n\x01w\x18\x04 \x01(\x01R\x01wB+Z)github.com/FormantIO/genproto/go/v1/modelb\x06proto3'
)




_NUMERIC = _descriptor.Descriptor(
  name='Numeric',
  full_name='v1.model.Numeric',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='v1.model.Numeric.value', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='value', file=DESCRIPTOR),
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
  ],
  serialized_start=40,
  serialized_end=71,
)


_METRICSET = _descriptor.Descriptor(
  name='MetricSet',
  full_name='v1.model.MetricSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metrics', full_name='v1.model.MetricSet.metrics', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='metrics', file=DESCRIPTOR),
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
  ],
  serialized_start=73,
  serialized_end=128,
)


_METRIC = _descriptor.Descriptor(
  name='Metric',
  full_name='v1.model.Metric',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='v1.model.Metric.value', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='value', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unit', full_name='v1.model.Metric.unit', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='unit', file=DESCRIPTOR),
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
  ],
  serialized_start=130,
  serialized_end=180,
)


_BIT = _descriptor.Descriptor(
  name='Bit',
  full_name='v1.model.Bit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='v1.model.Bit.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='key', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='v1.model.Bit.value', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='value', file=DESCRIPTOR),
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
  ],
  serialized_start=182,
  serialized_end=227,
)


_BITSET = _descriptor.Descriptor(
  name='Bitset',
  full_name='v1.model.Bitset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bits', full_name='v1.model.Bitset.bits', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='bits', file=DESCRIPTOR),
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
  ],
  serialized_start=229,
  serialized_end=272,
)


_TWIST = _descriptor.Descriptor(
  name='Twist',
  full_name='v1.model.Twist',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='linear', full_name='v1.model.Twist.linear', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='linear', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='angular', full_name='v1.model.Twist.angular', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='angular', file=DESCRIPTOR),
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
  ],
  serialized_start=274,
  serialized_end=369,
)


_TRANSFORM = _descriptor.Descriptor(
  name='Transform',
  full_name='v1.model.Transform',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='translation', full_name='v1.model.Transform.translation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='translation', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rotation', full_name='v1.model.Transform.rotation', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='rotation', file=DESCRIPTOR),
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
  ],
  serialized_start=371,
  serialized_end=485,
)


_TRANSFORMFRAME = _descriptor.Descriptor(
  name='TransformFrame',
  full_name='v1.model.TransformFrame',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent_frame', full_name='v1.model.TransformFrame.parent_frame', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='parentFrame', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='child_frame', full_name='v1.model.TransformFrame.child_frame', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='childFrame', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transform', full_name='v1.model.TransformFrame.transform', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='transform', file=DESCRIPTOR),
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
  ],
  serialized_start=488,
  serialized_end=623,
)


_VECTOR3 = _descriptor.Descriptor(
  name='Vector3',
  full_name='v1.model.Vector3',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='v1.model.Vector3.x', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='x', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='v1.model.Vector3.y', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='y', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='z', full_name='v1.model.Vector3.z', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='z', file=DESCRIPTOR),
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
  ],
  serialized_start=625,
  serialized_end=676,
)


_QUATERNION = _descriptor.Descriptor(
  name='Quaternion',
  full_name='v1.model.Quaternion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='v1.model.Quaternion.x', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='x', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='v1.model.Quaternion.y', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='y', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='z', full_name='v1.model.Quaternion.z', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='z', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='w', full_name='v1.model.Quaternion.w', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='w', file=DESCRIPTOR),
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
  ],
  serialized_start=678,
  serialized_end=746,
)

_METRICSET.fields_by_name['metrics'].message_type = _METRIC
_BITSET.fields_by_name['bits'].message_type = _BIT
_TWIST.fields_by_name['linear'].message_type = _VECTOR3
_TWIST.fields_by_name['angular'].message_type = _VECTOR3
_TRANSFORM.fields_by_name['translation'].message_type = _VECTOR3
_TRANSFORM.fields_by_name['rotation'].message_type = _QUATERNION
_TRANSFORMFRAME.fields_by_name['transform'].message_type = _TRANSFORM
DESCRIPTOR.message_types_by_name['Numeric'] = _NUMERIC
DESCRIPTOR.message_types_by_name['MetricSet'] = _METRICSET
DESCRIPTOR.message_types_by_name['Metric'] = _METRIC
DESCRIPTOR.message_types_by_name['Bit'] = _BIT
DESCRIPTOR.message_types_by_name['Bitset'] = _BITSET
DESCRIPTOR.message_types_by_name['Twist'] = _TWIST
DESCRIPTOR.message_types_by_name['Transform'] = _TRANSFORM
DESCRIPTOR.message_types_by_name['TransformFrame'] = _TRANSFORMFRAME
DESCRIPTOR.message_types_by_name['Vector3'] = _VECTOR3
DESCRIPTOR.message_types_by_name['Quaternion'] = _QUATERNION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Numeric = _reflection.GeneratedProtocolMessageType('Numeric', (_message.Message,), {
  'DESCRIPTOR' : _NUMERIC,
  '__module__' : 'protos.model.v1.math_pb2'
  # @@protoc_insertion_point(class_scope:v1.model.Numeric)
  })
_sym_db.RegisterMessage(Numeric)

MetricSet = _reflection.GeneratedProtocolMessageType('MetricSet', (_message.Message,), {
  'DESCRIPTOR' : _METRICSET,
  '__module__' : 'protos.model.v1.math_pb2'
  # @@protoc_insertion_point(class_scope:v1.model.MetricSet)
  })
_sym_db.RegisterMessage(MetricSet)

Metric = _reflection.GeneratedProtocolMessageType('Metric', (_message.Message,), {
  'DESCRIPTOR' : _METRIC,
  '__module__' : 'protos.model.v1.math_pb2'
  # @@protoc_insertion_point(class_scope:v1.model.Metric)
  })
_sym_db.RegisterMessage(Metric)

Bit = _reflection.GeneratedProtocolMessageType('Bit', (_message.Message,), {
  'DESCRIPTOR' : _BIT,
  '__module__' : 'protos.model.v1.math_pb2'
  # @@protoc_insertion_point(class_scope:v1.model.Bit)
  })
_sym_db.RegisterMessage(Bit)

Bitset = _reflection.GeneratedProtocolMessageType('Bitset', (_message.Message,), {
  'DESCRIPTOR' : _BITSET,
  '__module__' : 'protos.model.v1.math_pb2'
  # @@protoc_insertion_point(class_scope:v1.model.Bitset)
  })
_sym_db.RegisterMessage(Bitset)

Twist = _reflection.GeneratedProtocolMessageType('Twist', (_message.Message,), {
  'DESCRIPTOR' : _TWIST,
  '__module__' : 'protos.model.v1.math_pb2'
  # @@protoc_insertion_point(class_scope:v1.model.Twist)
  })
_sym_db.RegisterMessage(Twist)

Transform = _reflection.GeneratedProtocolMessageType('Transform', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFORM,
  '__module__' : 'protos.model.v1.math_pb2'
  # @@protoc_insertion_point(class_scope:v1.model.Transform)
  })
_sym_db.RegisterMessage(Transform)

TransformFrame = _reflection.GeneratedProtocolMessageType('TransformFrame', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFORMFRAME,
  '__module__' : 'protos.model.v1.math_pb2'
  # @@protoc_insertion_point(class_scope:v1.model.TransformFrame)
  })
_sym_db.RegisterMessage(TransformFrame)

Vector3 = _reflection.GeneratedProtocolMessageType('Vector3', (_message.Message,), {
  'DESCRIPTOR' : _VECTOR3,
  '__module__' : 'protos.model.v1.math_pb2'
  # @@protoc_insertion_point(class_scope:v1.model.Vector3)
  })
_sym_db.RegisterMessage(Vector3)

Quaternion = _reflection.GeneratedProtocolMessageType('Quaternion', (_message.Message,), {
  'DESCRIPTOR' : _QUATERNION,
  '__module__' : 'protos.model.v1.math_pb2'
  # @@protoc_insertion_point(class_scope:v1.model.Quaternion)
  })
_sym_db.RegisterMessage(Quaternion)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
