# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/model/v1/event.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/model/v1/event.proto',
  package='v1.model',
  syntax='proto3',
  serialized_options=b'Z)github.com/FormantIO/genproto/go/v1/model',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1bprotos/model/v1/event.proto\x12\x08v1.model\"\xf7\x02\n\x05\x45vent\x12\x1c\n\ttimestamp\x18\x01 \x01(\x03R\ttimestamp\x12#\n\rend_timestamp\x18\x08 \x01(\x03R\x0c\x65ndTimestamp\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12\x1f\n\x0bstream_name\x18\x03 \x01(\tR\nstreamName\x12\x1f\n\x0bstream_type\x18\x04 \x01(\tR\nstreamType\x12\x31\n\x14notification_enabled\x18\x05 \x01(\x08R\x13notificationEnabled\x12.\n\x08severity\x18\t \x01(\x0e\x32\x12.v1.model.SeverityR\x08severity\x12-\n\x04tags\x18\x06 \x03(\x0b\x32\x19.v1.model.Event.TagsEntryR\x04tags\x1a\x37\n\tTagsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01J\x04\x08\x07\x10\x08\"\x80\x01\n\x17\x41gentEventConfiguration\x12\x42\n\x0e\x65vent_triggers\x18\x01 \x03(\x0b\x32\x1b.v1.model.AgentEventTriggerR\reventTriggers\x12!\n\x0clast_updated\x18\x02 \x01(\x03R\x0blastUpdated\"\xf4\x02\n\x11\x41gentEventTrigger\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x16\n\x06stream\x18\x02 \x01(\tR\x06stream\x12\x1a\n\x08interval\x18\x03 \x01(\x03R\x08interval\x12\x45\n\x08presence\x18\x04 \x01(\x0b\x32\'.v1.model.PresenceEventTriggerConditionH\x00R\x08presence\x12H\n\tthreshold\x18\x05 \x01(\x0b\x32(.v1.model.ThresholdEventTriggerConditionH\x00R\tthreshold\x12<\n\x05regex\x18\x06 \x01(\x0b\x32$.v1.model.RegexEventTriggerConditionH\x00R\x05regex\x12?\n\x06\x62itset\x18\x07 \x01(\x0b\x32%.v1.model.BitsetEventTriggerConditionH\x00R\x06\x62itsetB\x0b\n\tcondition\"\x1f\n\x1dPresenceEventTriggerCondition\"o\n\x1eThresholdEventTriggerCondition\x12\x14\n\x05value\x18\x01 \x01(\x01R\x05value\x12\x37\n\x08operator\x18\x02 \x01(\x0e\x32\x1b.v1.model.ThresholdOperatorR\x08operator\"2\n\x1aRegexEventTriggerCondition\x12\x14\n\x05value\x18\x01 \x01(\tR\x05value\"\x95\x01\n\x1b\x42itsetEventTriggerCondition\x12@\n\x0e\x62it_conditions\x18\x01 \x03(\x0b\x32\x19.v1.model.BitsetConditionR\rbitConditions\x12\x34\n\x08operator\x18\x02 \x01(\x0e\x32\x18.v1.model.BitsetOperatorR\x08operator\"M\n\x0f\x42itsetCondition\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x12\n\x04true\x18\x02 \x01(\x08R\x04true\x12\x14\n\x05\x66\x61lse\x18\x03 \x01(\x08R\x05\x66\x61lse*:\n\x08Severity\x12\x08\n\x04INFO\x10\x00\x12\x0b\n\x07WARNING\x10\x01\x12\t\n\x05\x45RROR\x10\x02\x12\x0c\n\x08\x43RITICAL\x10\x03*F\n\x11ThresholdOperator\x12\x06\n\x02LT\x10\x00\x12\x07\n\x03LTE\x10\x01\x12\x06\n\x02GT\x10\x02\x12\x07\n\x03GTE\x10\x03\x12\x06\n\x02\x45Q\x10\x04\x12\x07\n\x03NEQ\x10\x05*\"\n\x0e\x42itsetOperator\x12\x07\n\x03\x41NY\x10\x00\x12\x07\n\x03\x41LL\x10\x01\x42+Z)github.com/FormantIO/genproto/go/v1/modelb\x06proto3'
)

_SEVERITY = _descriptor.EnumDescriptor(
  name='Severity',
  full_name='v1.model.Severity',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INFO', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WARNING', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CRITICAL', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1354,
  serialized_end=1412,
)
_sym_db.RegisterEnumDescriptor(_SEVERITY)

Severity = enum_type_wrapper.EnumTypeWrapper(_SEVERITY)
_THRESHOLDOPERATOR = _descriptor.EnumDescriptor(
  name='ThresholdOperator',
  full_name='v1.model.ThresholdOperator',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LT', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LTE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GT', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GTE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EQ', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NEQ', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1414,
  serialized_end=1484,
)
_sym_db.RegisterEnumDescriptor(_THRESHOLDOPERATOR)

ThresholdOperator = enum_type_wrapper.EnumTypeWrapper(_THRESHOLDOPERATOR)
_BITSETOPERATOR = _descriptor.EnumDescriptor(
  name='BitsetOperator',
  full_name='v1.model.BitsetOperator',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ANY', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALL', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1486,
  serialized_end=1520,
)
_sym_db.RegisterEnumDescriptor(_BITSETOPERATOR)

BitsetOperator = enum_type_wrapper.EnumTypeWrapper(_BITSETOPERATOR)
INFO = 0
WARNING = 1
ERROR = 2
CRITICAL = 3
LT = 0
LTE = 1
GT = 2
GTE = 3
EQ = 4
NEQ = 5
ANY = 0
ALL = 1



_EVENT_TAGSENTRY = _descriptor.Descriptor(
  name='TagsEntry',
  full_name='v1.model.Event.TagsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='v1.model.Event.TagsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='key', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='v1.model.Event.TagsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='value', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=356,
  serialized_end=411,
)

_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='v1.model.Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='v1.model.Event.timestamp', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='timestamp', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_timestamp', full_name='v1.model.Event.end_timestamp', index=1,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='endTimestamp', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='v1.model.Event.message', index=2,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='message', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stream_name', full_name='v1.model.Event.stream_name', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='streamName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stream_type', full_name='v1.model.Event.stream_type', index=4,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='streamType', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='notification_enabled', full_name='v1.model.Event.notification_enabled', index=5,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='notificationEnabled', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='severity', full_name='v1.model.Event.severity', index=6,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='severity', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tags', full_name='v1.model.Event.tags', index=7,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='tags', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_EVENT_TAGSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=42,
  serialized_end=417,
)


_AGENTEVENTCONFIGURATION = _descriptor.Descriptor(
  name='AgentEventConfiguration',
  full_name='v1.model.AgentEventConfiguration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='event_triggers', full_name='v1.model.AgentEventConfiguration.event_triggers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='eventTriggers', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_updated', full_name='v1.model.AgentEventConfiguration.last_updated', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='lastUpdated', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=420,
  serialized_end=548,
)


_AGENTEVENTTRIGGER = _descriptor.Descriptor(
  name='AgentEventTrigger',
  full_name='v1.model.AgentEventTrigger',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='v1.model.AgentEventTrigger.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='id', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stream', full_name='v1.model.AgentEventTrigger.stream', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='stream', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='interval', full_name='v1.model.AgentEventTrigger.interval', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='interval', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='presence', full_name='v1.model.AgentEventTrigger.presence', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='presence', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='threshold', full_name='v1.model.AgentEventTrigger.threshold', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='threshold', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='regex', full_name='v1.model.AgentEventTrigger.regex', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='regex', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bitset', full_name='v1.model.AgentEventTrigger.bitset', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='bitset', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
      name='condition', full_name='v1.model.AgentEventTrigger.condition',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=551,
  serialized_end=923,
)


_PRESENCEEVENTTRIGGERCONDITION = _descriptor.Descriptor(
  name='PresenceEventTriggerCondition',
  full_name='v1.model.PresenceEventTriggerCondition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=925,
  serialized_end=956,
)


_THRESHOLDEVENTTRIGGERCONDITION = _descriptor.Descriptor(
  name='ThresholdEventTriggerCondition',
  full_name='v1.model.ThresholdEventTriggerCondition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='v1.model.ThresholdEventTriggerCondition.value', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='value', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operator', full_name='v1.model.ThresholdEventTriggerCondition.operator', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='operator', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=958,
  serialized_end=1069,
)


_REGEXEVENTTRIGGERCONDITION = _descriptor.Descriptor(
  name='RegexEventTriggerCondition',
  full_name='v1.model.RegexEventTriggerCondition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='v1.model.RegexEventTriggerCondition.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='value', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1071,
  serialized_end=1121,
)


_BITSETEVENTTRIGGERCONDITION = _descriptor.Descriptor(
  name='BitsetEventTriggerCondition',
  full_name='v1.model.BitsetEventTriggerCondition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='bit_conditions', full_name='v1.model.BitsetEventTriggerCondition.bit_conditions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='bitConditions', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operator', full_name='v1.model.BitsetEventTriggerCondition.operator', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='operator', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1124,
  serialized_end=1273,
)


_BITSETCONDITION = _descriptor.Descriptor(
  name='BitsetCondition',
  full_name='v1.model.BitsetCondition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='v1.model.BitsetCondition.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='key', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='true', full_name='v1.model.BitsetCondition.true', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='true', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='false', full_name='v1.model.BitsetCondition.false', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='false', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1275,
  serialized_end=1352,
)

_EVENT_TAGSENTRY.containing_type = _EVENT
_EVENT.fields_by_name['severity'].enum_type = _SEVERITY
_EVENT.fields_by_name['tags'].message_type = _EVENT_TAGSENTRY
_AGENTEVENTCONFIGURATION.fields_by_name['event_triggers'].message_type = _AGENTEVENTTRIGGER
_AGENTEVENTTRIGGER.fields_by_name['presence'].message_type = _PRESENCEEVENTTRIGGERCONDITION
_AGENTEVENTTRIGGER.fields_by_name['threshold'].message_type = _THRESHOLDEVENTTRIGGERCONDITION
_AGENTEVENTTRIGGER.fields_by_name['regex'].message_type = _REGEXEVENTTRIGGERCONDITION
_AGENTEVENTTRIGGER.fields_by_name['bitset'].message_type = _BITSETEVENTTRIGGERCONDITION
_AGENTEVENTTRIGGER.oneofs_by_name['condition'].fields.append(
  _AGENTEVENTTRIGGER.fields_by_name['presence'])
_AGENTEVENTTRIGGER.fields_by_name['presence'].containing_oneof = _AGENTEVENTTRIGGER.oneofs_by_name['condition']
_AGENTEVENTTRIGGER.oneofs_by_name['condition'].fields.append(
  _AGENTEVENTTRIGGER.fields_by_name['threshold'])
_AGENTEVENTTRIGGER.fields_by_name['threshold'].containing_oneof = _AGENTEVENTTRIGGER.oneofs_by_name['condition']
_AGENTEVENTTRIGGER.oneofs_by_name['condition'].fields.append(
  _AGENTEVENTTRIGGER.fields_by_name['regex'])
_AGENTEVENTTRIGGER.fields_by_name['regex'].containing_oneof = _AGENTEVENTTRIGGER.oneofs_by_name['condition']
_AGENTEVENTTRIGGER.oneofs_by_name['condition'].fields.append(
  _AGENTEVENTTRIGGER.fields_by_name['bitset'])
_AGENTEVENTTRIGGER.fields_by_name['bitset'].containing_oneof = _AGENTEVENTTRIGGER.oneofs_by_name['condition']
_THRESHOLDEVENTTRIGGERCONDITION.fields_by_name['operator'].enum_type = _THRESHOLDOPERATOR
_BITSETEVENTTRIGGERCONDITION.fields_by_name['bit_conditions'].message_type = _BITSETCONDITION
_BITSETEVENTTRIGGERCONDITION.fields_by_name['operator'].enum_type = _BITSETOPERATOR
DESCRIPTOR.message_types_by_name['Event'] = _EVENT
DESCRIPTOR.message_types_by_name['AgentEventConfiguration'] = _AGENTEVENTCONFIGURATION
DESCRIPTOR.message_types_by_name['AgentEventTrigger'] = _AGENTEVENTTRIGGER
DESCRIPTOR.message_types_by_name['PresenceEventTriggerCondition'] = _PRESENCEEVENTTRIGGERCONDITION
DESCRIPTOR.message_types_by_name['ThresholdEventTriggerCondition'] = _THRESHOLDEVENTTRIGGERCONDITION
DESCRIPTOR.message_types_by_name['RegexEventTriggerCondition'] = _REGEXEVENTTRIGGERCONDITION
DESCRIPTOR.message_types_by_name['BitsetEventTriggerCondition'] = _BITSETEVENTTRIGGERCONDITION
DESCRIPTOR.message_types_by_name['BitsetCondition'] = _BITSETCONDITION
DESCRIPTOR.enum_types_by_name['Severity'] = _SEVERITY
DESCRIPTOR.enum_types_by_name['ThresholdOperator'] = _THRESHOLDOPERATOR
DESCRIPTOR.enum_types_by_name['BitsetOperator'] = _BITSETOPERATOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), {

  'TagsEntry' : _reflection.GeneratedProtocolMessageType('TagsEntry', (_message.Message,), {
    'DESCRIPTOR' : _EVENT_TAGSENTRY,
    '__module__' : 'protos.model.v1.event_pb2'
    # @@protoc_insertion_point(class_scope:v1.model.Event.TagsEntry)
    })
  ,
  'DESCRIPTOR' : _EVENT,
  '__module__' : 'protos.model.v1.event_pb2'
  # @@protoc_insertion_point(class_scope:v1.model.Event)
  })
_sym_db.RegisterMessage(Event)
_sym_db.RegisterMessage(Event.TagsEntry)

AgentEventConfiguration = _reflection.GeneratedProtocolMessageType('AgentEventConfiguration', (_message.Message,), {
  'DESCRIPTOR' : _AGENTEVENTCONFIGURATION,
  '__module__' : 'protos.model.v1.event_pb2'
  # @@protoc_insertion_point(class_scope:v1.model.AgentEventConfiguration)
  })
_sym_db.RegisterMessage(AgentEventConfiguration)

AgentEventTrigger = _reflection.GeneratedProtocolMessageType('AgentEventTrigger', (_message.Message,), {
  'DESCRIPTOR' : _AGENTEVENTTRIGGER,
  '__module__' : 'protos.model.v1.event_pb2'
  # @@protoc_insertion_point(class_scope:v1.model.AgentEventTrigger)
  })
_sym_db.RegisterMessage(AgentEventTrigger)

PresenceEventTriggerCondition = _reflection.GeneratedProtocolMessageType('PresenceEventTriggerCondition', (_message.Message,), {
  'DESCRIPTOR' : _PRESENCEEVENTTRIGGERCONDITION,
  '__module__' : 'protos.model.v1.event_pb2'
  # @@protoc_insertion_point(class_scope:v1.model.PresenceEventTriggerCondition)
  })
_sym_db.RegisterMessage(PresenceEventTriggerCondition)

ThresholdEventTriggerCondition = _reflection.GeneratedProtocolMessageType('ThresholdEventTriggerCondition', (_message.Message,), {
  'DESCRIPTOR' : _THRESHOLDEVENTTRIGGERCONDITION,
  '__module__' : 'protos.model.v1.event_pb2'
  # @@protoc_insertion_point(class_scope:v1.model.ThresholdEventTriggerCondition)
  })
_sym_db.RegisterMessage(ThresholdEventTriggerCondition)

RegexEventTriggerCondition = _reflection.GeneratedProtocolMessageType('RegexEventTriggerCondition', (_message.Message,), {
  'DESCRIPTOR' : _REGEXEVENTTRIGGERCONDITION,
  '__module__' : 'protos.model.v1.event_pb2'
  # @@protoc_insertion_point(class_scope:v1.model.RegexEventTriggerCondition)
  })
_sym_db.RegisterMessage(RegexEventTriggerCondition)

BitsetEventTriggerCondition = _reflection.GeneratedProtocolMessageType('BitsetEventTriggerCondition', (_message.Message,), {
  'DESCRIPTOR' : _BITSETEVENTTRIGGERCONDITION,
  '__module__' : 'protos.model.v1.event_pb2'
  # @@protoc_insertion_point(class_scope:v1.model.BitsetEventTriggerCondition)
  })
_sym_db.RegisterMessage(BitsetEventTriggerCondition)

BitsetCondition = _reflection.GeneratedProtocolMessageType('BitsetCondition', (_message.Message,), {
  'DESCRIPTOR' : _BITSETCONDITION,
  '__module__' : 'protos.model.v1.event_pb2'
  # @@protoc_insertion_point(class_scope:v1.model.BitsetCondition)
  })
_sym_db.RegisterMessage(BitsetCondition)


DESCRIPTOR._options = None
_EVENT_TAGSENTRY._options = None
# @@protoc_insertion_point(module_scope)