// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: protos/model/v1/event.proto

#include "protos/model/v1/event.pb.h"

#include <algorithm>

#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/extension_set.h>
#include <google/protobuf/wire_format_lite.h>
#include <google/protobuf/descriptor.h>
#include <google/protobuf/generated_message_reflection.h>
#include <google/protobuf/reflection_ops.h>
#include <google/protobuf/wire_format.h>
// @@protoc_insertion_point(includes)
#include <google/protobuf/port_def.inc>
extern PROTOBUF_INTERNAL_EXPORT_protos_2fmodel_2fv1_2fevent_2eproto ::PROTOBUF_NAMESPACE_ID::internal::SCCInfo<0> scc_info_Event_TagsEntry_DoNotUse_protos_2fmodel_2fv1_2fevent_2eproto;
namespace v1 {
namespace model {
class Event_TagsEntry_DoNotUseDefaultTypeInternal {
 public:
  ::PROTOBUF_NAMESPACE_ID::internal::ExplicitlyConstructed<Event_TagsEntry_DoNotUse> _instance;
} _Event_TagsEntry_DoNotUse_default_instance_;
class EventDefaultTypeInternal {
 public:
  ::PROTOBUF_NAMESPACE_ID::internal::ExplicitlyConstructed<Event> _instance;
} _Event_default_instance_;
}  // namespace model
}  // namespace v1
static void InitDefaultsscc_info_Event_protos_2fmodel_2fv1_2fevent_2eproto() {
  GOOGLE_PROTOBUF_VERIFY_VERSION;

  {
    void* ptr = &::v1::model::_Event_default_instance_;
    new (ptr) ::v1::model::Event();
    ::PROTOBUF_NAMESPACE_ID::internal::OnShutdownDestroyMessage(ptr);
  }
  ::v1::model::Event::InitAsDefaultInstance();
}

::PROTOBUF_NAMESPACE_ID::internal::SCCInfo<1> scc_info_Event_protos_2fmodel_2fv1_2fevent_2eproto =
    {{ATOMIC_VAR_INIT(::PROTOBUF_NAMESPACE_ID::internal::SCCInfoBase::kUninitialized), 1, 0, InitDefaultsscc_info_Event_protos_2fmodel_2fv1_2fevent_2eproto}, {
      &scc_info_Event_TagsEntry_DoNotUse_protos_2fmodel_2fv1_2fevent_2eproto.base,}};

static void InitDefaultsscc_info_Event_TagsEntry_DoNotUse_protos_2fmodel_2fv1_2fevent_2eproto() {
  GOOGLE_PROTOBUF_VERIFY_VERSION;

  {
    void* ptr = &::v1::model::_Event_TagsEntry_DoNotUse_default_instance_;
    new (ptr) ::v1::model::Event_TagsEntry_DoNotUse();
  }
  ::v1::model::Event_TagsEntry_DoNotUse::InitAsDefaultInstance();
}

::PROTOBUF_NAMESPACE_ID::internal::SCCInfo<0> scc_info_Event_TagsEntry_DoNotUse_protos_2fmodel_2fv1_2fevent_2eproto =
    {{ATOMIC_VAR_INIT(::PROTOBUF_NAMESPACE_ID::internal::SCCInfoBase::kUninitialized), 0, 0, InitDefaultsscc_info_Event_TagsEntry_DoNotUse_protos_2fmodel_2fv1_2fevent_2eproto}, {}};

static ::PROTOBUF_NAMESPACE_ID::Metadata file_level_metadata_protos_2fmodel_2fv1_2fevent_2eproto[2];
static constexpr ::PROTOBUF_NAMESPACE_ID::EnumDescriptor const** file_level_enum_descriptors_protos_2fmodel_2fv1_2fevent_2eproto = nullptr;
static constexpr ::PROTOBUF_NAMESPACE_ID::ServiceDescriptor const** file_level_service_descriptors_protos_2fmodel_2fv1_2fevent_2eproto = nullptr;

const ::PROTOBUF_NAMESPACE_ID::uint32 TableStruct_protos_2fmodel_2fv1_2fevent_2eproto::offsets[] PROTOBUF_SECTION_VARIABLE(protodesc_cold) = {
  PROTOBUF_FIELD_OFFSET(::v1::model::Event_TagsEntry_DoNotUse, _has_bits_),
  PROTOBUF_FIELD_OFFSET(::v1::model::Event_TagsEntry_DoNotUse, _internal_metadata_),
  ~0u,  // no _extensions_
  ~0u,  // no _oneof_case_
  ~0u,  // no _weak_field_map_
  PROTOBUF_FIELD_OFFSET(::v1::model::Event_TagsEntry_DoNotUse, key_),
  PROTOBUF_FIELD_OFFSET(::v1::model::Event_TagsEntry_DoNotUse, value_),
  0,
  1,
  ~0u,  // no _has_bits_
  PROTOBUF_FIELD_OFFSET(::v1::model::Event, _internal_metadata_),
  ~0u,  // no _extensions_
  ~0u,  // no _oneof_case_
  ~0u,  // no _weak_field_map_
  PROTOBUF_FIELD_OFFSET(::v1::model::Event, timestamp_),
  PROTOBUF_FIELD_OFFSET(::v1::model::Event, message_),
  PROTOBUF_FIELD_OFFSET(::v1::model::Event, stream_name_),
  PROTOBUF_FIELD_OFFSET(::v1::model::Event, stream_type_),
  PROTOBUF_FIELD_OFFSET(::v1::model::Event, notification_enabled_),
  PROTOBUF_FIELD_OFFSET(::v1::model::Event, tags_),
};
static const ::PROTOBUF_NAMESPACE_ID::internal::MigrationSchema schemas[] PROTOBUF_SECTION_VARIABLE(protodesc_cold) = {
  { 0, 7, sizeof(::v1::model::Event_TagsEntry_DoNotUse)},
  { 9, -1, sizeof(::v1::model::Event)},
};

static ::PROTOBUF_NAMESPACE_ID::Message const * const file_default_instances[] = {
  reinterpret_cast<const ::PROTOBUF_NAMESPACE_ID::Message*>(&::v1::model::_Event_TagsEntry_DoNotUse_default_instance_),
  reinterpret_cast<const ::PROTOBUF_NAMESPACE_ID::Message*>(&::v1::model::_Event_default_instance_),
};

const char descriptor_table_protodef_protos_2fmodel_2fv1_2fevent_2eproto[] PROTOBUF_SECTION_VARIABLE(protodesc_cold) =
  "\n\033protos/model/v1/event.proto\022\010v1.model\""
  "\311\001\n\005Event\022\021\n\ttimestamp\030\001 \001(\003\022\017\n\007message\030"
  "\002 \001(\t\022\023\n\013stream_name\030\003 \001(\t\022\023\n\013stream_typ"
  "e\030\004 \001(\t\022\034\n\024notification_enabled\030\005 \001(\010\022\'\n"
  "\004tags\030\006 \003(\0132\031.v1.model.Event.TagsEntry\032+"
  "\n\tTagsEntry\022\013\n\003key\030\001 \001(\t\022\r\n\005value\030\002 \001(\t:"
  "\0028\001B+Z)github.com/FormantIO/genproto/go/"
  "v1/modelb\006proto3"
  ;
static const ::PROTOBUF_NAMESPACE_ID::internal::DescriptorTable*const descriptor_table_protos_2fmodel_2fv1_2fevent_2eproto_deps[1] = {
};
static ::PROTOBUF_NAMESPACE_ID::internal::SCCInfoBase*const descriptor_table_protos_2fmodel_2fv1_2fevent_2eproto_sccs[2] = {
  &scc_info_Event_protos_2fmodel_2fv1_2fevent_2eproto.base,
  &scc_info_Event_TagsEntry_DoNotUse_protos_2fmodel_2fv1_2fevent_2eproto.base,
};
static ::PROTOBUF_NAMESPACE_ID::internal::once_flag descriptor_table_protos_2fmodel_2fv1_2fevent_2eproto_once;
const ::PROTOBUF_NAMESPACE_ID::internal::DescriptorTable descriptor_table_protos_2fmodel_2fv1_2fevent_2eproto = {
  false, false, descriptor_table_protodef_protos_2fmodel_2fv1_2fevent_2eproto, "protos/model/v1/event.proto", 296,
  &descriptor_table_protos_2fmodel_2fv1_2fevent_2eproto_once, descriptor_table_protos_2fmodel_2fv1_2fevent_2eproto_sccs, descriptor_table_protos_2fmodel_2fv1_2fevent_2eproto_deps, 2, 0,
  schemas, file_default_instances, TableStruct_protos_2fmodel_2fv1_2fevent_2eproto::offsets,
  file_level_metadata_protos_2fmodel_2fv1_2fevent_2eproto, 2, file_level_enum_descriptors_protos_2fmodel_2fv1_2fevent_2eproto, file_level_service_descriptors_protos_2fmodel_2fv1_2fevent_2eproto,
};

// Force running AddDescriptors() at dynamic initialization time.
static bool dynamic_init_dummy_protos_2fmodel_2fv1_2fevent_2eproto = (static_cast<void>(::PROTOBUF_NAMESPACE_ID::internal::AddDescriptors(&descriptor_table_protos_2fmodel_2fv1_2fevent_2eproto)), true);
namespace v1 {
namespace model {

// ===================================================================

Event_TagsEntry_DoNotUse::Event_TagsEntry_DoNotUse() {}
Event_TagsEntry_DoNotUse::Event_TagsEntry_DoNotUse(::PROTOBUF_NAMESPACE_ID::Arena* arena)
    : SuperType(arena) {}
void Event_TagsEntry_DoNotUse::MergeFrom(const Event_TagsEntry_DoNotUse& other) {
  MergeFromInternal(other);
}
::PROTOBUF_NAMESPACE_ID::Metadata Event_TagsEntry_DoNotUse::GetMetadata() const {
  return GetMetadataStatic();
}
void Event_TagsEntry_DoNotUse::MergeFrom(
    const ::PROTOBUF_NAMESPACE_ID::Message& other) {
  ::PROTOBUF_NAMESPACE_ID::Message::MergeFrom(other);
}


// ===================================================================

void Event::InitAsDefaultInstance() {
}
class Event::_Internal {
 public:
};

Event::Event(::PROTOBUF_NAMESPACE_ID::Arena* arena)
  : ::PROTOBUF_NAMESPACE_ID::Message(arena),
  tags_(arena) {
  SharedCtor();
  RegisterArenaDtor(arena);
  // @@protoc_insertion_point(arena_constructor:v1.model.Event)
}
Event::Event(const Event& from)
  : ::PROTOBUF_NAMESPACE_ID::Message() {
  _internal_metadata_.MergeFrom<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(from._internal_metadata_);
  tags_.MergeFrom(from.tags_);
  message_.UnsafeSetDefault(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
  if (!from._internal_message().empty()) {
    message_.Set(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), from._internal_message(),
      GetArena());
  }
  stream_name_.UnsafeSetDefault(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
  if (!from._internal_stream_name().empty()) {
    stream_name_.Set(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), from._internal_stream_name(),
      GetArena());
  }
  stream_type_.UnsafeSetDefault(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
  if (!from._internal_stream_type().empty()) {
    stream_type_.Set(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), from._internal_stream_type(),
      GetArena());
  }
  ::memcpy(&timestamp_, &from.timestamp_,
    static_cast<size_t>(reinterpret_cast<char*>(&notification_enabled_) -
    reinterpret_cast<char*>(&timestamp_)) + sizeof(notification_enabled_));
  // @@protoc_insertion_point(copy_constructor:v1.model.Event)
}

void Event::SharedCtor() {
  ::PROTOBUF_NAMESPACE_ID::internal::InitSCC(&scc_info_Event_protos_2fmodel_2fv1_2fevent_2eproto.base);
  message_.UnsafeSetDefault(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
  stream_name_.UnsafeSetDefault(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
  stream_type_.UnsafeSetDefault(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
  ::memset(&timestamp_, 0, static_cast<size_t>(
      reinterpret_cast<char*>(&notification_enabled_) -
      reinterpret_cast<char*>(&timestamp_)) + sizeof(notification_enabled_));
}

Event::~Event() {
  // @@protoc_insertion_point(destructor:v1.model.Event)
  SharedDtor();
  _internal_metadata_.Delete<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>();
}

void Event::SharedDtor() {
  GOOGLE_DCHECK(GetArena() == nullptr);
  message_.DestroyNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
  stream_name_.DestroyNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
  stream_type_.DestroyNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
}

void Event::ArenaDtor(void* object) {
  Event* _this = reinterpret_cast< Event* >(object);
  (void)_this;
}
void Event::RegisterArenaDtor(::PROTOBUF_NAMESPACE_ID::Arena*) {
}
void Event::SetCachedSize(int size) const {
  _cached_size_.Set(size);
}
const Event& Event::default_instance() {
  ::PROTOBUF_NAMESPACE_ID::internal::InitSCC(&::scc_info_Event_protos_2fmodel_2fv1_2fevent_2eproto.base);
  return *internal_default_instance();
}


void Event::Clear() {
// @@protoc_insertion_point(message_clear_start:v1.model.Event)
  ::PROTOBUF_NAMESPACE_ID::uint32 cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  tags_.Clear();
  message_.ClearToEmpty(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), GetArena());
  stream_name_.ClearToEmpty(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), GetArena());
  stream_type_.ClearToEmpty(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), GetArena());
  ::memset(&timestamp_, 0, static_cast<size_t>(
      reinterpret_cast<char*>(&notification_enabled_) -
      reinterpret_cast<char*>(&timestamp_)) + sizeof(notification_enabled_));
  _internal_metadata_.Clear<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>();
}

const char* Event::_InternalParse(const char* ptr, ::PROTOBUF_NAMESPACE_ID::internal::ParseContext* ctx) {
#define CHK_(x) if (PROTOBUF_PREDICT_FALSE(!(x))) goto failure
  ::PROTOBUF_NAMESPACE_ID::Arena* arena = GetArena(); (void)arena;
  while (!ctx->Done(&ptr)) {
    ::PROTOBUF_NAMESPACE_ID::uint32 tag;
    ptr = ::PROTOBUF_NAMESPACE_ID::internal::ReadTag(ptr, &tag);
    CHK_(ptr);
    switch (tag >> 3) {
      // int64 timestamp = 1;
      case 1:
        if (PROTOBUF_PREDICT_TRUE(static_cast<::PROTOBUF_NAMESPACE_ID::uint8>(tag) == 8)) {
          timestamp_ = ::PROTOBUF_NAMESPACE_ID::internal::ReadVarint64(&ptr);
          CHK_(ptr);
        } else goto handle_unusual;
        continue;
      // string message = 2;
      case 2:
        if (PROTOBUF_PREDICT_TRUE(static_cast<::PROTOBUF_NAMESPACE_ID::uint8>(tag) == 18)) {
          auto str = _internal_mutable_message();
          ptr = ::PROTOBUF_NAMESPACE_ID::internal::InlineGreedyStringParser(str, ptr, ctx);
          CHK_(::PROTOBUF_NAMESPACE_ID::internal::VerifyUTF8(str, "v1.model.Event.message"));
          CHK_(ptr);
        } else goto handle_unusual;
        continue;
      // string stream_name = 3;
      case 3:
        if (PROTOBUF_PREDICT_TRUE(static_cast<::PROTOBUF_NAMESPACE_ID::uint8>(tag) == 26)) {
          auto str = _internal_mutable_stream_name();
          ptr = ::PROTOBUF_NAMESPACE_ID::internal::InlineGreedyStringParser(str, ptr, ctx);
          CHK_(::PROTOBUF_NAMESPACE_ID::internal::VerifyUTF8(str, "v1.model.Event.stream_name"));
          CHK_(ptr);
        } else goto handle_unusual;
        continue;
      // string stream_type = 4;
      case 4:
        if (PROTOBUF_PREDICT_TRUE(static_cast<::PROTOBUF_NAMESPACE_ID::uint8>(tag) == 34)) {
          auto str = _internal_mutable_stream_type();
          ptr = ::PROTOBUF_NAMESPACE_ID::internal::InlineGreedyStringParser(str, ptr, ctx);
          CHK_(::PROTOBUF_NAMESPACE_ID::internal::VerifyUTF8(str, "v1.model.Event.stream_type"));
          CHK_(ptr);
        } else goto handle_unusual;
        continue;
      // bool notification_enabled = 5;
      case 5:
        if (PROTOBUF_PREDICT_TRUE(static_cast<::PROTOBUF_NAMESPACE_ID::uint8>(tag) == 40)) {
          notification_enabled_ = ::PROTOBUF_NAMESPACE_ID::internal::ReadVarint64(&ptr);
          CHK_(ptr);
        } else goto handle_unusual;
        continue;
      // map<string, string> tags = 6;
      case 6:
        if (PROTOBUF_PREDICT_TRUE(static_cast<::PROTOBUF_NAMESPACE_ID::uint8>(tag) == 50)) {
          ptr -= 1;
          do {
            ptr += 1;
            ptr = ctx->ParseMessage(&tags_, ptr);
            CHK_(ptr);
            if (!ctx->DataAvailable(ptr)) break;
          } while (::PROTOBUF_NAMESPACE_ID::internal::ExpectTag<50>(ptr));
        } else goto handle_unusual;
        continue;
      default: {
      handle_unusual:
        if ((tag & 7) == 4 || tag == 0) {
          ctx->SetLastTag(tag);
          goto success;
        }
        ptr = UnknownFieldParse(tag,
            _internal_metadata_.mutable_unknown_fields<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(),
            ptr, ctx);
        CHK_(ptr != nullptr);
        continue;
      }
    }  // switch
  }  // while
success:
  return ptr;
failure:
  ptr = nullptr;
  goto success;
#undef CHK_
}

::PROTOBUF_NAMESPACE_ID::uint8* Event::_InternalSerialize(
    ::PROTOBUF_NAMESPACE_ID::uint8* target, ::PROTOBUF_NAMESPACE_ID::io::EpsCopyOutputStream* stream) const {
  // @@protoc_insertion_point(serialize_to_array_start:v1.model.Event)
  ::PROTOBUF_NAMESPACE_ID::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  // int64 timestamp = 1;
  if (this->timestamp() != 0) {
    target = stream->EnsureSpace(target);
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::WriteInt64ToArray(1, this->_internal_timestamp(), target);
  }

  // string message = 2;
  if (this->message().size() > 0) {
    ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::VerifyUtf8String(
      this->_internal_message().data(), static_cast<int>(this->_internal_message().length()),
      ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::SERIALIZE,
      "v1.model.Event.message");
    target = stream->WriteStringMaybeAliased(
        2, this->_internal_message(), target);
  }

  // string stream_name = 3;
  if (this->stream_name().size() > 0) {
    ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::VerifyUtf8String(
      this->_internal_stream_name().data(), static_cast<int>(this->_internal_stream_name().length()),
      ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::SERIALIZE,
      "v1.model.Event.stream_name");
    target = stream->WriteStringMaybeAliased(
        3, this->_internal_stream_name(), target);
  }

  // string stream_type = 4;
  if (this->stream_type().size() > 0) {
    ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::VerifyUtf8String(
      this->_internal_stream_type().data(), static_cast<int>(this->_internal_stream_type().length()),
      ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::SERIALIZE,
      "v1.model.Event.stream_type");
    target = stream->WriteStringMaybeAliased(
        4, this->_internal_stream_type(), target);
  }

  // bool notification_enabled = 5;
  if (this->notification_enabled() != 0) {
    target = stream->EnsureSpace(target);
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::WriteBoolToArray(5, this->_internal_notification_enabled(), target);
  }

  // map<string, string> tags = 6;
  if (!this->_internal_tags().empty()) {
    typedef ::PROTOBUF_NAMESPACE_ID::Map< std::string, std::string >::const_pointer
        ConstPtr;
    typedef ConstPtr SortItem;
    typedef ::PROTOBUF_NAMESPACE_ID::internal::CompareByDerefFirst<SortItem> Less;
    struct Utf8Check {
      static void Check(ConstPtr p) {
        ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::VerifyUtf8String(
          p->first.data(), static_cast<int>(p->first.length()),
          ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::SERIALIZE,
          "v1.model.Event.TagsEntry.key");
        ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::VerifyUtf8String(
          p->second.data(), static_cast<int>(p->second.length()),
          ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::SERIALIZE,
          "v1.model.Event.TagsEntry.value");
      }
    };

    if (stream->IsSerializationDeterministic() &&
        this->_internal_tags().size() > 1) {
      ::std::unique_ptr<SortItem[]> items(
          new SortItem[this->_internal_tags().size()]);
      typedef ::PROTOBUF_NAMESPACE_ID::Map< std::string, std::string >::size_type size_type;
      size_type n = 0;
      for (::PROTOBUF_NAMESPACE_ID::Map< std::string, std::string >::const_iterator
          it = this->_internal_tags().begin();
          it != this->_internal_tags().end(); ++it, ++n) {
        items[static_cast<ptrdiff_t>(n)] = SortItem(&*it);
      }
      ::std::sort(&items[0], &items[static_cast<ptrdiff_t>(n)], Less());
      for (size_type i = 0; i < n; i++) {
        target = Event_TagsEntry_DoNotUse::Funcs::InternalSerialize(6, items[static_cast<ptrdiff_t>(i)]->first, items[static_cast<ptrdiff_t>(i)]->second, target, stream);
        Utf8Check::Check(&(*items[static_cast<ptrdiff_t>(i)]));
      }
    } else {
      for (::PROTOBUF_NAMESPACE_ID::Map< std::string, std::string >::const_iterator
          it = this->_internal_tags().begin();
          it != this->_internal_tags().end(); ++it) {
        target = Event_TagsEntry_DoNotUse::Funcs::InternalSerialize(6, it->first, it->second, target, stream);
        Utf8Check::Check(&(*it));
      }
    }
  }

  if (PROTOBUF_PREDICT_FALSE(_internal_metadata_.have_unknown_fields())) {
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormat::InternalSerializeUnknownFieldsToArray(
        _internal_metadata_.unknown_fields<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(::PROTOBUF_NAMESPACE_ID::UnknownFieldSet::default_instance), target, stream);
  }
  // @@protoc_insertion_point(serialize_to_array_end:v1.model.Event)
  return target;
}

size_t Event::ByteSizeLong() const {
// @@protoc_insertion_point(message_byte_size_start:v1.model.Event)
  size_t total_size = 0;

  ::PROTOBUF_NAMESPACE_ID::uint32 cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  // map<string, string> tags = 6;
  total_size += 1 *
      ::PROTOBUF_NAMESPACE_ID::internal::FromIntSize(this->_internal_tags_size());
  for (::PROTOBUF_NAMESPACE_ID::Map< std::string, std::string >::const_iterator
      it = this->_internal_tags().begin();
      it != this->_internal_tags().end(); ++it) {
    total_size += Event_TagsEntry_DoNotUse::Funcs::ByteSizeLong(it->first, it->second);
  }

  // string message = 2;
  if (this->message().size() > 0) {
    total_size += 1 +
      ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::StringSize(
        this->_internal_message());
  }

  // string stream_name = 3;
  if (this->stream_name().size() > 0) {
    total_size += 1 +
      ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::StringSize(
        this->_internal_stream_name());
  }

  // string stream_type = 4;
  if (this->stream_type().size() > 0) {
    total_size += 1 +
      ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::StringSize(
        this->_internal_stream_type());
  }

  // int64 timestamp = 1;
  if (this->timestamp() != 0) {
    total_size += 1 +
      ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::Int64Size(
        this->_internal_timestamp());
  }

  // bool notification_enabled = 5;
  if (this->notification_enabled() != 0) {
    total_size += 1 + 1;
  }

  if (PROTOBUF_PREDICT_FALSE(_internal_metadata_.have_unknown_fields())) {
    return ::PROTOBUF_NAMESPACE_ID::internal::ComputeUnknownFieldsSize(
        _internal_metadata_, total_size, &_cached_size_);
  }
  int cached_size = ::PROTOBUF_NAMESPACE_ID::internal::ToCachedSize(total_size);
  SetCachedSize(cached_size);
  return total_size;
}

void Event::MergeFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) {
// @@protoc_insertion_point(generalized_merge_from_start:v1.model.Event)
  GOOGLE_DCHECK_NE(&from, this);
  const Event* source =
      ::PROTOBUF_NAMESPACE_ID::DynamicCastToGenerated<Event>(
          &from);
  if (source == nullptr) {
  // @@protoc_insertion_point(generalized_merge_from_cast_fail:v1.model.Event)
    ::PROTOBUF_NAMESPACE_ID::internal::ReflectionOps::Merge(from, this);
  } else {
  // @@protoc_insertion_point(generalized_merge_from_cast_success:v1.model.Event)
    MergeFrom(*source);
  }
}

void Event::MergeFrom(const Event& from) {
// @@protoc_insertion_point(class_specific_merge_from_start:v1.model.Event)
  GOOGLE_DCHECK_NE(&from, this);
  _internal_metadata_.MergeFrom<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(from._internal_metadata_);
  ::PROTOBUF_NAMESPACE_ID::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  tags_.MergeFrom(from.tags_);
  if (from.message().size() > 0) {
    _internal_set_message(from._internal_message());
  }
  if (from.stream_name().size() > 0) {
    _internal_set_stream_name(from._internal_stream_name());
  }
  if (from.stream_type().size() > 0) {
    _internal_set_stream_type(from._internal_stream_type());
  }
  if (from.timestamp() != 0) {
    _internal_set_timestamp(from._internal_timestamp());
  }
  if (from.notification_enabled() != 0) {
    _internal_set_notification_enabled(from._internal_notification_enabled());
  }
}

void Event::CopyFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) {
// @@protoc_insertion_point(generalized_copy_from_start:v1.model.Event)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

void Event::CopyFrom(const Event& from) {
// @@protoc_insertion_point(class_specific_copy_from_start:v1.model.Event)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

bool Event::IsInitialized() const {
  return true;
}

void Event::InternalSwap(Event* other) {
  using std::swap;
  _internal_metadata_.Swap<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(&other->_internal_metadata_);
  tags_.Swap(&other->tags_);
  message_.Swap(&other->message_, &::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), GetArena());
  stream_name_.Swap(&other->stream_name_, &::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), GetArena());
  stream_type_.Swap(&other->stream_type_, &::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), GetArena());
  ::PROTOBUF_NAMESPACE_ID::internal::memswap<
      PROTOBUF_FIELD_OFFSET(Event, notification_enabled_)
      + sizeof(Event::notification_enabled_)
      - PROTOBUF_FIELD_OFFSET(Event, timestamp_)>(
          reinterpret_cast<char*>(&timestamp_),
          reinterpret_cast<char*>(&other->timestamp_));
}

::PROTOBUF_NAMESPACE_ID::Metadata Event::GetMetadata() const {
  return GetMetadataStatic();
}


// @@protoc_insertion_point(namespace_scope)
}  // namespace model
}  // namespace v1
PROTOBUF_NAMESPACE_OPEN
template<> PROTOBUF_NOINLINE ::v1::model::Event_TagsEntry_DoNotUse* Arena::CreateMaybeMessage< ::v1::model::Event_TagsEntry_DoNotUse >(Arena* arena) {
  return Arena::CreateMessageInternal< ::v1::model::Event_TagsEntry_DoNotUse >(arena);
}
template<> PROTOBUF_NOINLINE ::v1::model::Event* Arena::CreateMaybeMessage< ::v1::model::Event >(Arena* arena) {
  return Arena::CreateMessageInternal< ::v1::model::Event >(arena);
}
PROTOBUF_NAMESPACE_CLOSE

// @@protoc_insertion_point(global_scope)
#include <google/protobuf/port_undef.inc>