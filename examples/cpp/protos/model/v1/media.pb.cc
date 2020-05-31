// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: protos/model/v1/media.proto

#include "protos/model/v1/media.pb.h"

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
extern PROTOBUF_INTERNAL_EXPORT_protos_2fmodel_2fv1_2fmath_2eproto ::PROTOBUF_NAMESPACE_ID::internal::SCCInfo<2> scc_info_Transform_protos_2fmodel_2fv1_2fmath_2eproto;
namespace v1 {
namespace model {
class ImageDefaultTypeInternal {
 public:
  ::PROTOBUF_NAMESPACE_ID::internal::ExplicitlyConstructed<Image> _instance;
  ::PROTOBUF_NAMESPACE_ID::internal::ArenaStringPtr url_;
  ::PROTOBUF_NAMESPACE_ID::internal::ArenaStringPtr raw_;
} _Image_default_instance_;
class PointCloudDefaultTypeInternal {
 public:
  ::PROTOBUF_NAMESPACE_ID::internal::ExplicitlyConstructed<PointCloud> _instance;
  ::PROTOBUF_NAMESPACE_ID::internal::ArenaStringPtr url_;
  ::PROTOBUF_NAMESPACE_ID::internal::ArenaStringPtr raw_;
} _PointCloud_default_instance_;
class H264VideoFrameDefaultTypeInternal {
 public:
  ::PROTOBUF_NAMESPACE_ID::internal::ExplicitlyConstructed<H264VideoFrame> _instance;
} _H264VideoFrame_default_instance_;
}  // namespace model
}  // namespace v1
static void InitDefaultsscc_info_H264VideoFrame_protos_2fmodel_2fv1_2fmedia_2eproto() {
  GOOGLE_PROTOBUF_VERIFY_VERSION;

  {
    void* ptr = &::v1::model::_H264VideoFrame_default_instance_;
    new (ptr) ::v1::model::H264VideoFrame();
    ::PROTOBUF_NAMESPACE_ID::internal::OnShutdownDestroyMessage(ptr);
  }
  ::v1::model::H264VideoFrame::InitAsDefaultInstance();
}

::PROTOBUF_NAMESPACE_ID::internal::SCCInfo<0> scc_info_H264VideoFrame_protos_2fmodel_2fv1_2fmedia_2eproto =
    {{ATOMIC_VAR_INIT(::PROTOBUF_NAMESPACE_ID::internal::SCCInfoBase::kUninitialized), 0, 0, InitDefaultsscc_info_H264VideoFrame_protos_2fmodel_2fv1_2fmedia_2eproto}, {}};

static void InitDefaultsscc_info_Image_protos_2fmodel_2fv1_2fmedia_2eproto() {
  GOOGLE_PROTOBUF_VERIFY_VERSION;

  {
    void* ptr = &::v1::model::_Image_default_instance_;
    new (ptr) ::v1::model::Image();
    ::PROTOBUF_NAMESPACE_ID::internal::OnShutdownDestroyMessage(ptr);
  }
  ::v1::model::Image::InitAsDefaultInstance();
}

::PROTOBUF_NAMESPACE_ID::internal::SCCInfo<0> scc_info_Image_protos_2fmodel_2fv1_2fmedia_2eproto =
    {{ATOMIC_VAR_INIT(::PROTOBUF_NAMESPACE_ID::internal::SCCInfoBase::kUninitialized), 0, 0, InitDefaultsscc_info_Image_protos_2fmodel_2fv1_2fmedia_2eproto}, {}};

static void InitDefaultsscc_info_PointCloud_protos_2fmodel_2fv1_2fmedia_2eproto() {
  GOOGLE_PROTOBUF_VERIFY_VERSION;

  {
    void* ptr = &::v1::model::_PointCloud_default_instance_;
    new (ptr) ::v1::model::PointCloud();
    ::PROTOBUF_NAMESPACE_ID::internal::OnShutdownDestroyMessage(ptr);
  }
  ::v1::model::PointCloud::InitAsDefaultInstance();
}

::PROTOBUF_NAMESPACE_ID::internal::SCCInfo<1> scc_info_PointCloud_protos_2fmodel_2fv1_2fmedia_2eproto =
    {{ATOMIC_VAR_INIT(::PROTOBUF_NAMESPACE_ID::internal::SCCInfoBase::kUninitialized), 1, 0, InitDefaultsscc_info_PointCloud_protos_2fmodel_2fv1_2fmedia_2eproto}, {
      &scc_info_Transform_protos_2fmodel_2fv1_2fmath_2eproto.base,}};

static ::PROTOBUF_NAMESPACE_ID::Metadata file_level_metadata_protos_2fmodel_2fv1_2fmedia_2eproto[3];
static constexpr ::PROTOBUF_NAMESPACE_ID::EnumDescriptor const** file_level_enum_descriptors_protos_2fmodel_2fv1_2fmedia_2eproto = nullptr;
static constexpr ::PROTOBUF_NAMESPACE_ID::ServiceDescriptor const** file_level_service_descriptors_protos_2fmodel_2fv1_2fmedia_2eproto = nullptr;

const ::PROTOBUF_NAMESPACE_ID::uint32 TableStruct_protos_2fmodel_2fv1_2fmedia_2eproto::offsets[] PROTOBUF_SECTION_VARIABLE(protodesc_cold) = {
  ~0u,  // no _has_bits_
  PROTOBUF_FIELD_OFFSET(::v1::model::Image, _internal_metadata_),
  ~0u,  // no _extensions_
  PROTOBUF_FIELD_OFFSET(::v1::model::Image, _oneof_case_[0]),
  ~0u,  // no _weak_field_map_
  PROTOBUF_FIELD_OFFSET(::v1::model::Image, content_type_),
  offsetof(::v1::model::ImageDefaultTypeInternal, url_),
  offsetof(::v1::model::ImageDefaultTypeInternal, raw_),
  PROTOBUF_FIELD_OFFSET(::v1::model::Image, data_),
  ~0u,  // no _has_bits_
  PROTOBUF_FIELD_OFFSET(::v1::model::PointCloud, _internal_metadata_),
  ~0u,  // no _extensions_
  PROTOBUF_FIELD_OFFSET(::v1::model::PointCloud, _oneof_case_[0]),
  ~0u,  // no _weak_field_map_
  offsetof(::v1::model::PointCloudDefaultTypeInternal, url_),
  offsetof(::v1::model::PointCloudDefaultTypeInternal, raw_),
  PROTOBUF_FIELD_OFFSET(::v1::model::PointCloud, world_to_local_),
  PROTOBUF_FIELD_OFFSET(::v1::model::PointCloud, data_),
  ~0u,  // no _has_bits_
  PROTOBUF_FIELD_OFFSET(::v1::model::H264VideoFrame, _internal_metadata_),
  ~0u,  // no _extensions_
  ~0u,  // no _oneof_case_
  ~0u,  // no _weak_field_map_
  PROTOBUF_FIELD_OFFSET(::v1::model::H264VideoFrame, index_),
  PROTOBUF_FIELD_OFFSET(::v1::model::H264VideoFrame, flags_),
  PROTOBUF_FIELD_OFFSET(::v1::model::H264VideoFrame, frame_data_),
};
static const ::PROTOBUF_NAMESPACE_ID::internal::MigrationSchema schemas[] PROTOBUF_SECTION_VARIABLE(protodesc_cold) = {
  { 0, -1, sizeof(::v1::model::Image)},
  { 9, -1, sizeof(::v1::model::PointCloud)},
  { 18, -1, sizeof(::v1::model::H264VideoFrame)},
};

static ::PROTOBUF_NAMESPACE_ID::Message const * const file_default_instances[] = {
  reinterpret_cast<const ::PROTOBUF_NAMESPACE_ID::Message*>(&::v1::model::_Image_default_instance_),
  reinterpret_cast<const ::PROTOBUF_NAMESPACE_ID::Message*>(&::v1::model::_PointCloud_default_instance_),
  reinterpret_cast<const ::PROTOBUF_NAMESPACE_ID::Message*>(&::v1::model::_H264VideoFrame_default_instance_),
};

const char descriptor_table_protodef_protos_2fmodel_2fv1_2fmedia_2eproto[] PROTOBUF_SECTION_VARIABLE(protodesc_cold) =
  "\n\033protos/model/v1/media.proto\022\010v1.model\032"
  "\032protos/model/v1/math.proto\"Z\n\005Image\022!\n\014"
  "content_type\030\001 \001(\tR\013contentType\022\022\n\003url\030\002"
  " \001(\tH\000R\003url\022\022\n\003raw\030\003 \001(\014H\000R\003rawB\006\n\004data\""
  "w\n\nPointCloud\022\022\n\003url\030\001 \001(\tH\000R\003url\022\022\n\003raw"
  "\030\002 \001(\014H\000R\003raw\0229\n\016world_to_local\030\003 \001(\0132\023."
  "v1.model.TransformR\014worldToLocalB\006\n\004data"
  "\"[\n\016H264VideoFrame\022\024\n\005index\030\001 \001(\005R\005index"
  "\022\024\n\005flags\030\002 \001(\005R\005flags\022\035\n\nframe_data\030\003 \001"
  "(\014R\tframeDataB+Z)github.com/FormantIO/ge"
  "nproto/go/v1/modelb\006proto3"
  ;
static const ::PROTOBUF_NAMESPACE_ID::internal::DescriptorTable*const descriptor_table_protos_2fmodel_2fv1_2fmedia_2eproto_deps[1] = {
  &::descriptor_table_protos_2fmodel_2fv1_2fmath_2eproto,
};
static ::PROTOBUF_NAMESPACE_ID::internal::SCCInfoBase*const descriptor_table_protos_2fmodel_2fv1_2fmedia_2eproto_sccs[3] = {
  &scc_info_H264VideoFrame_protos_2fmodel_2fv1_2fmedia_2eproto.base,
  &scc_info_Image_protos_2fmodel_2fv1_2fmedia_2eproto.base,
  &scc_info_PointCloud_protos_2fmodel_2fv1_2fmedia_2eproto.base,
};
static ::PROTOBUF_NAMESPACE_ID::internal::once_flag descriptor_table_protos_2fmodel_2fv1_2fmedia_2eproto_once;
static bool descriptor_table_protos_2fmodel_2fv1_2fmedia_2eproto_initialized = false;
const ::PROTOBUF_NAMESPACE_ID::internal::DescriptorTable descriptor_table_protos_2fmodel_2fv1_2fmedia_2eproto = {
  &descriptor_table_protos_2fmodel_2fv1_2fmedia_2eproto_initialized, descriptor_table_protodef_protos_2fmodel_2fv1_2fmedia_2eproto, "protos/model/v1/media.proto", 426,
  &descriptor_table_protos_2fmodel_2fv1_2fmedia_2eproto_once, descriptor_table_protos_2fmodel_2fv1_2fmedia_2eproto_sccs, descriptor_table_protos_2fmodel_2fv1_2fmedia_2eproto_deps, 3, 1,
  schemas, file_default_instances, TableStruct_protos_2fmodel_2fv1_2fmedia_2eproto::offsets,
  file_level_metadata_protos_2fmodel_2fv1_2fmedia_2eproto, 3, file_level_enum_descriptors_protos_2fmodel_2fv1_2fmedia_2eproto, file_level_service_descriptors_protos_2fmodel_2fv1_2fmedia_2eproto,
};

// Force running AddDescriptors() at dynamic initialization time.
static bool dynamic_init_dummy_protos_2fmodel_2fv1_2fmedia_2eproto = (  ::PROTOBUF_NAMESPACE_ID::internal::AddDescriptors(&descriptor_table_protos_2fmodel_2fv1_2fmedia_2eproto), true);
namespace v1 {
namespace model {

// ===================================================================

void Image::InitAsDefaultInstance() {
  ::v1::model::_Image_default_instance_.url_.UnsafeSetDefault(
      &::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
  ::v1::model::_Image_default_instance_.raw_.UnsafeSetDefault(
      &::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
}
class Image::_Internal {
 public:
};

Image::Image()
  : ::PROTOBUF_NAMESPACE_ID::Message(), _internal_metadata_(nullptr) {
  SharedCtor();
  // @@protoc_insertion_point(constructor:v1.model.Image)
}
Image::Image(const Image& from)
  : ::PROTOBUF_NAMESPACE_ID::Message(),
      _internal_metadata_(nullptr) {
  _internal_metadata_.MergeFrom(from._internal_metadata_);
  content_type_.UnsafeSetDefault(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
  if (!from._internal_content_type().empty()) {
    content_type_.AssignWithDefault(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), from.content_type_);
  }
  clear_has_data();
  switch (from.data_case()) {
    case kUrl: {
      _internal_set_url(from._internal_url());
      break;
    }
    case kRaw: {
      _internal_set_raw(from._internal_raw());
      break;
    }
    case DATA_NOT_SET: {
      break;
    }
  }
  // @@protoc_insertion_point(copy_constructor:v1.model.Image)
}

void Image::SharedCtor() {
  ::PROTOBUF_NAMESPACE_ID::internal::InitSCC(&scc_info_Image_protos_2fmodel_2fv1_2fmedia_2eproto.base);
  content_type_.UnsafeSetDefault(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
  clear_has_data();
}

Image::~Image() {
  // @@protoc_insertion_point(destructor:v1.model.Image)
  SharedDtor();
}

void Image::SharedDtor() {
  content_type_.DestroyNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
  if (has_data()) {
    clear_data();
  }
}

void Image::SetCachedSize(int size) const {
  _cached_size_.Set(size);
}
const Image& Image::default_instance() {
  ::PROTOBUF_NAMESPACE_ID::internal::InitSCC(&::scc_info_Image_protos_2fmodel_2fv1_2fmedia_2eproto.base);
  return *internal_default_instance();
}


void Image::clear_data() {
// @@protoc_insertion_point(one_of_clear_start:v1.model.Image)
  switch (data_case()) {
    case kUrl: {
      data_.url_.DestroyNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
      break;
    }
    case kRaw: {
      data_.raw_.DestroyNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
      break;
    }
    case DATA_NOT_SET: {
      break;
    }
  }
  _oneof_case_[0] = DATA_NOT_SET;
}


void Image::Clear() {
// @@protoc_insertion_point(message_clear_start:v1.model.Image)
  ::PROTOBUF_NAMESPACE_ID::uint32 cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  content_type_.ClearToEmptyNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
  clear_data();
  _internal_metadata_.Clear();
}

const char* Image::_InternalParse(const char* ptr, ::PROTOBUF_NAMESPACE_ID::internal::ParseContext* ctx) {
#define CHK_(x) if (PROTOBUF_PREDICT_FALSE(!(x))) goto failure
  while (!ctx->Done(&ptr)) {
    ::PROTOBUF_NAMESPACE_ID::uint32 tag;
    ptr = ::PROTOBUF_NAMESPACE_ID::internal::ReadTag(ptr, &tag);
    CHK_(ptr);
    switch (tag >> 3) {
      // string content_type = 1[json_name = "contentType"];
      case 1:
        if (PROTOBUF_PREDICT_TRUE(static_cast<::PROTOBUF_NAMESPACE_ID::uint8>(tag) == 10)) {
          auto str = _internal_mutable_content_type();
          ptr = ::PROTOBUF_NAMESPACE_ID::internal::InlineGreedyStringParser(str, ptr, ctx);
          CHK_(::PROTOBUF_NAMESPACE_ID::internal::VerifyUTF8(str, "v1.model.Image.content_type"));
          CHK_(ptr);
        } else goto handle_unusual;
        continue;
      // string url = 2[json_name = "url"];
      case 2:
        if (PROTOBUF_PREDICT_TRUE(static_cast<::PROTOBUF_NAMESPACE_ID::uint8>(tag) == 18)) {
          auto str = _internal_mutable_url();
          ptr = ::PROTOBUF_NAMESPACE_ID::internal::InlineGreedyStringParser(str, ptr, ctx);
          CHK_(::PROTOBUF_NAMESPACE_ID::internal::VerifyUTF8(str, "v1.model.Image.url"));
          CHK_(ptr);
        } else goto handle_unusual;
        continue;
      // bytes raw = 3[json_name = "raw"];
      case 3:
        if (PROTOBUF_PREDICT_TRUE(static_cast<::PROTOBUF_NAMESPACE_ID::uint8>(tag) == 26)) {
          auto str = _internal_mutable_raw();
          ptr = ::PROTOBUF_NAMESPACE_ID::internal::InlineGreedyStringParser(str, ptr, ctx);
          CHK_(ptr);
        } else goto handle_unusual;
        continue;
      default: {
      handle_unusual:
        if ((tag & 7) == 4 || tag == 0) {
          ctx->SetLastTag(tag);
          goto success;
        }
        ptr = UnknownFieldParse(tag, &_internal_metadata_, ptr, ctx);
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

::PROTOBUF_NAMESPACE_ID::uint8* Image::_InternalSerialize(
    ::PROTOBUF_NAMESPACE_ID::uint8* target, ::PROTOBUF_NAMESPACE_ID::io::EpsCopyOutputStream* stream) const {
  // @@protoc_insertion_point(serialize_to_array_start:v1.model.Image)
  ::PROTOBUF_NAMESPACE_ID::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  // string content_type = 1[json_name = "contentType"];
  if (this->content_type().size() > 0) {
    ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::VerifyUtf8String(
      this->_internal_content_type().data(), static_cast<int>(this->_internal_content_type().length()),
      ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::SERIALIZE,
      "v1.model.Image.content_type");
    target = stream->WriteStringMaybeAliased(
        1, this->_internal_content_type(), target);
  }

  // string url = 2[json_name = "url"];
  if (_internal_has_url()) {
    ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::VerifyUtf8String(
      this->_internal_url().data(), static_cast<int>(this->_internal_url().length()),
      ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::SERIALIZE,
      "v1.model.Image.url");
    target = stream->WriteStringMaybeAliased(
        2, this->_internal_url(), target);
  }

  // bytes raw = 3[json_name = "raw"];
  if (_internal_has_raw()) {
    target = stream->WriteBytesMaybeAliased(
        3, this->_internal_raw(), target);
  }

  if (PROTOBUF_PREDICT_FALSE(_internal_metadata_.have_unknown_fields())) {
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormat::InternalSerializeUnknownFieldsToArray(
        _internal_metadata_.unknown_fields(), target, stream);
  }
  // @@protoc_insertion_point(serialize_to_array_end:v1.model.Image)
  return target;
}

size_t Image::ByteSizeLong() const {
// @@protoc_insertion_point(message_byte_size_start:v1.model.Image)
  size_t total_size = 0;

  ::PROTOBUF_NAMESPACE_ID::uint32 cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  // string content_type = 1[json_name = "contentType"];
  if (this->content_type().size() > 0) {
    total_size += 1 +
      ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::StringSize(
        this->_internal_content_type());
  }

  switch (data_case()) {
    // string url = 2[json_name = "url"];
    case kUrl: {
      total_size += 1 +
        ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::StringSize(
          this->_internal_url());
      break;
    }
    // bytes raw = 3[json_name = "raw"];
    case kRaw: {
      total_size += 1 +
        ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::BytesSize(
          this->_internal_raw());
      break;
    }
    case DATA_NOT_SET: {
      break;
    }
  }
  if (PROTOBUF_PREDICT_FALSE(_internal_metadata_.have_unknown_fields())) {
    return ::PROTOBUF_NAMESPACE_ID::internal::ComputeUnknownFieldsSize(
        _internal_metadata_, total_size, &_cached_size_);
  }
  int cached_size = ::PROTOBUF_NAMESPACE_ID::internal::ToCachedSize(total_size);
  SetCachedSize(cached_size);
  return total_size;
}

void Image::MergeFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) {
// @@protoc_insertion_point(generalized_merge_from_start:v1.model.Image)
  GOOGLE_DCHECK_NE(&from, this);
  const Image* source =
      ::PROTOBUF_NAMESPACE_ID::DynamicCastToGenerated<Image>(
          &from);
  if (source == nullptr) {
  // @@protoc_insertion_point(generalized_merge_from_cast_fail:v1.model.Image)
    ::PROTOBUF_NAMESPACE_ID::internal::ReflectionOps::Merge(from, this);
  } else {
  // @@protoc_insertion_point(generalized_merge_from_cast_success:v1.model.Image)
    MergeFrom(*source);
  }
}

void Image::MergeFrom(const Image& from) {
// @@protoc_insertion_point(class_specific_merge_from_start:v1.model.Image)
  GOOGLE_DCHECK_NE(&from, this);
  _internal_metadata_.MergeFrom(from._internal_metadata_);
  ::PROTOBUF_NAMESPACE_ID::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  if (from.content_type().size() > 0) {

    content_type_.AssignWithDefault(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), from.content_type_);
  }
  switch (from.data_case()) {
    case kUrl: {
      _internal_set_url(from._internal_url());
      break;
    }
    case kRaw: {
      _internal_set_raw(from._internal_raw());
      break;
    }
    case DATA_NOT_SET: {
      break;
    }
  }
}

void Image::CopyFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) {
// @@protoc_insertion_point(generalized_copy_from_start:v1.model.Image)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

void Image::CopyFrom(const Image& from) {
// @@protoc_insertion_point(class_specific_copy_from_start:v1.model.Image)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

bool Image::IsInitialized() const {
  return true;
}

void Image::InternalSwap(Image* other) {
  using std::swap;
  _internal_metadata_.Swap(&other->_internal_metadata_);
  content_type_.Swap(&other->content_type_, &::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(),
    GetArenaNoVirtual());
  swap(data_, other->data_);
  swap(_oneof_case_[0], other->_oneof_case_[0]);
}

::PROTOBUF_NAMESPACE_ID::Metadata Image::GetMetadata() const {
  return GetMetadataStatic();
}


// ===================================================================

void PointCloud::InitAsDefaultInstance() {
  ::v1::model::_PointCloud_default_instance_.url_.UnsafeSetDefault(
      &::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
  ::v1::model::_PointCloud_default_instance_.raw_.UnsafeSetDefault(
      &::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
  ::v1::model::_PointCloud_default_instance_._instance.get_mutable()->world_to_local_ = const_cast< ::v1::model::Transform*>(
      ::v1::model::Transform::internal_default_instance());
}
class PointCloud::_Internal {
 public:
  static const ::v1::model::Transform& world_to_local(const PointCloud* msg);
};

const ::v1::model::Transform&
PointCloud::_Internal::world_to_local(const PointCloud* msg) {
  return *msg->world_to_local_;
}
void PointCloud::clear_world_to_local() {
  if (GetArenaNoVirtual() == nullptr && world_to_local_ != nullptr) {
    delete world_to_local_;
  }
  world_to_local_ = nullptr;
}
PointCloud::PointCloud()
  : ::PROTOBUF_NAMESPACE_ID::Message(), _internal_metadata_(nullptr) {
  SharedCtor();
  // @@protoc_insertion_point(constructor:v1.model.PointCloud)
}
PointCloud::PointCloud(const PointCloud& from)
  : ::PROTOBUF_NAMESPACE_ID::Message(),
      _internal_metadata_(nullptr) {
  _internal_metadata_.MergeFrom(from._internal_metadata_);
  if (from._internal_has_world_to_local()) {
    world_to_local_ = new ::v1::model::Transform(*from.world_to_local_);
  } else {
    world_to_local_ = nullptr;
  }
  clear_has_data();
  switch (from.data_case()) {
    case kUrl: {
      _internal_set_url(from._internal_url());
      break;
    }
    case kRaw: {
      _internal_set_raw(from._internal_raw());
      break;
    }
    case DATA_NOT_SET: {
      break;
    }
  }
  // @@protoc_insertion_point(copy_constructor:v1.model.PointCloud)
}

void PointCloud::SharedCtor() {
  ::PROTOBUF_NAMESPACE_ID::internal::InitSCC(&scc_info_PointCloud_protos_2fmodel_2fv1_2fmedia_2eproto.base);
  world_to_local_ = nullptr;
  clear_has_data();
}

PointCloud::~PointCloud() {
  // @@protoc_insertion_point(destructor:v1.model.PointCloud)
  SharedDtor();
}

void PointCloud::SharedDtor() {
  if (this != internal_default_instance()) delete world_to_local_;
  if (has_data()) {
    clear_data();
  }
}

void PointCloud::SetCachedSize(int size) const {
  _cached_size_.Set(size);
}
const PointCloud& PointCloud::default_instance() {
  ::PROTOBUF_NAMESPACE_ID::internal::InitSCC(&::scc_info_PointCloud_protos_2fmodel_2fv1_2fmedia_2eproto.base);
  return *internal_default_instance();
}


void PointCloud::clear_data() {
// @@protoc_insertion_point(one_of_clear_start:v1.model.PointCloud)
  switch (data_case()) {
    case kUrl: {
      data_.url_.DestroyNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
      break;
    }
    case kRaw: {
      data_.raw_.DestroyNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
      break;
    }
    case DATA_NOT_SET: {
      break;
    }
  }
  _oneof_case_[0] = DATA_NOT_SET;
}


void PointCloud::Clear() {
// @@protoc_insertion_point(message_clear_start:v1.model.PointCloud)
  ::PROTOBUF_NAMESPACE_ID::uint32 cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  if (GetArenaNoVirtual() == nullptr && world_to_local_ != nullptr) {
    delete world_to_local_;
  }
  world_to_local_ = nullptr;
  clear_data();
  _internal_metadata_.Clear();
}

const char* PointCloud::_InternalParse(const char* ptr, ::PROTOBUF_NAMESPACE_ID::internal::ParseContext* ctx) {
#define CHK_(x) if (PROTOBUF_PREDICT_FALSE(!(x))) goto failure
  while (!ctx->Done(&ptr)) {
    ::PROTOBUF_NAMESPACE_ID::uint32 tag;
    ptr = ::PROTOBUF_NAMESPACE_ID::internal::ReadTag(ptr, &tag);
    CHK_(ptr);
    switch (tag >> 3) {
      // string url = 1[json_name = "url"];
      case 1:
        if (PROTOBUF_PREDICT_TRUE(static_cast<::PROTOBUF_NAMESPACE_ID::uint8>(tag) == 10)) {
          auto str = _internal_mutable_url();
          ptr = ::PROTOBUF_NAMESPACE_ID::internal::InlineGreedyStringParser(str, ptr, ctx);
          CHK_(::PROTOBUF_NAMESPACE_ID::internal::VerifyUTF8(str, "v1.model.PointCloud.url"));
          CHK_(ptr);
        } else goto handle_unusual;
        continue;
      // bytes raw = 2[json_name = "raw"];
      case 2:
        if (PROTOBUF_PREDICT_TRUE(static_cast<::PROTOBUF_NAMESPACE_ID::uint8>(tag) == 18)) {
          auto str = _internal_mutable_raw();
          ptr = ::PROTOBUF_NAMESPACE_ID::internal::InlineGreedyStringParser(str, ptr, ctx);
          CHK_(ptr);
        } else goto handle_unusual;
        continue;
      // .v1.model.Transform world_to_local = 3[json_name = "worldToLocal"];
      case 3:
        if (PROTOBUF_PREDICT_TRUE(static_cast<::PROTOBUF_NAMESPACE_ID::uint8>(tag) == 26)) {
          ptr = ctx->ParseMessage(_internal_mutable_world_to_local(), ptr);
          CHK_(ptr);
        } else goto handle_unusual;
        continue;
      default: {
      handle_unusual:
        if ((tag & 7) == 4 || tag == 0) {
          ctx->SetLastTag(tag);
          goto success;
        }
        ptr = UnknownFieldParse(tag, &_internal_metadata_, ptr, ctx);
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

::PROTOBUF_NAMESPACE_ID::uint8* PointCloud::_InternalSerialize(
    ::PROTOBUF_NAMESPACE_ID::uint8* target, ::PROTOBUF_NAMESPACE_ID::io::EpsCopyOutputStream* stream) const {
  // @@protoc_insertion_point(serialize_to_array_start:v1.model.PointCloud)
  ::PROTOBUF_NAMESPACE_ID::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  // string url = 1[json_name = "url"];
  if (_internal_has_url()) {
    ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::VerifyUtf8String(
      this->_internal_url().data(), static_cast<int>(this->_internal_url().length()),
      ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::SERIALIZE,
      "v1.model.PointCloud.url");
    target = stream->WriteStringMaybeAliased(
        1, this->_internal_url(), target);
  }

  // bytes raw = 2[json_name = "raw"];
  if (_internal_has_raw()) {
    target = stream->WriteBytesMaybeAliased(
        2, this->_internal_raw(), target);
  }

  // .v1.model.Transform world_to_local = 3[json_name = "worldToLocal"];
  if (this->has_world_to_local()) {
    target = stream->EnsureSpace(target);
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::
      InternalWriteMessage(
        3, _Internal::world_to_local(this), target, stream);
  }

  if (PROTOBUF_PREDICT_FALSE(_internal_metadata_.have_unknown_fields())) {
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormat::InternalSerializeUnknownFieldsToArray(
        _internal_metadata_.unknown_fields(), target, stream);
  }
  // @@protoc_insertion_point(serialize_to_array_end:v1.model.PointCloud)
  return target;
}

size_t PointCloud::ByteSizeLong() const {
// @@protoc_insertion_point(message_byte_size_start:v1.model.PointCloud)
  size_t total_size = 0;

  ::PROTOBUF_NAMESPACE_ID::uint32 cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  // .v1.model.Transform world_to_local = 3[json_name = "worldToLocal"];
  if (this->has_world_to_local()) {
    total_size += 1 +
      ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::MessageSize(
        *world_to_local_);
  }

  switch (data_case()) {
    // string url = 1[json_name = "url"];
    case kUrl: {
      total_size += 1 +
        ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::StringSize(
          this->_internal_url());
      break;
    }
    // bytes raw = 2[json_name = "raw"];
    case kRaw: {
      total_size += 1 +
        ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::BytesSize(
          this->_internal_raw());
      break;
    }
    case DATA_NOT_SET: {
      break;
    }
  }
  if (PROTOBUF_PREDICT_FALSE(_internal_metadata_.have_unknown_fields())) {
    return ::PROTOBUF_NAMESPACE_ID::internal::ComputeUnknownFieldsSize(
        _internal_metadata_, total_size, &_cached_size_);
  }
  int cached_size = ::PROTOBUF_NAMESPACE_ID::internal::ToCachedSize(total_size);
  SetCachedSize(cached_size);
  return total_size;
}

void PointCloud::MergeFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) {
// @@protoc_insertion_point(generalized_merge_from_start:v1.model.PointCloud)
  GOOGLE_DCHECK_NE(&from, this);
  const PointCloud* source =
      ::PROTOBUF_NAMESPACE_ID::DynamicCastToGenerated<PointCloud>(
          &from);
  if (source == nullptr) {
  // @@protoc_insertion_point(generalized_merge_from_cast_fail:v1.model.PointCloud)
    ::PROTOBUF_NAMESPACE_ID::internal::ReflectionOps::Merge(from, this);
  } else {
  // @@protoc_insertion_point(generalized_merge_from_cast_success:v1.model.PointCloud)
    MergeFrom(*source);
  }
}

void PointCloud::MergeFrom(const PointCloud& from) {
// @@protoc_insertion_point(class_specific_merge_from_start:v1.model.PointCloud)
  GOOGLE_DCHECK_NE(&from, this);
  _internal_metadata_.MergeFrom(from._internal_metadata_);
  ::PROTOBUF_NAMESPACE_ID::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  if (from.has_world_to_local()) {
    _internal_mutable_world_to_local()->::v1::model::Transform::MergeFrom(from._internal_world_to_local());
  }
  switch (from.data_case()) {
    case kUrl: {
      _internal_set_url(from._internal_url());
      break;
    }
    case kRaw: {
      _internal_set_raw(from._internal_raw());
      break;
    }
    case DATA_NOT_SET: {
      break;
    }
  }
}

void PointCloud::CopyFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) {
// @@protoc_insertion_point(generalized_copy_from_start:v1.model.PointCloud)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

void PointCloud::CopyFrom(const PointCloud& from) {
// @@protoc_insertion_point(class_specific_copy_from_start:v1.model.PointCloud)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

bool PointCloud::IsInitialized() const {
  return true;
}

void PointCloud::InternalSwap(PointCloud* other) {
  using std::swap;
  _internal_metadata_.Swap(&other->_internal_metadata_);
  swap(world_to_local_, other->world_to_local_);
  swap(data_, other->data_);
  swap(_oneof_case_[0], other->_oneof_case_[0]);
}

::PROTOBUF_NAMESPACE_ID::Metadata PointCloud::GetMetadata() const {
  return GetMetadataStatic();
}


// ===================================================================

void H264VideoFrame::InitAsDefaultInstance() {
}
class H264VideoFrame::_Internal {
 public:
};

H264VideoFrame::H264VideoFrame()
  : ::PROTOBUF_NAMESPACE_ID::Message(), _internal_metadata_(nullptr) {
  SharedCtor();
  // @@protoc_insertion_point(constructor:v1.model.H264VideoFrame)
}
H264VideoFrame::H264VideoFrame(const H264VideoFrame& from)
  : ::PROTOBUF_NAMESPACE_ID::Message(),
      _internal_metadata_(nullptr) {
  _internal_metadata_.MergeFrom(from._internal_metadata_);
  frame_data_.UnsafeSetDefault(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
  if (!from._internal_frame_data().empty()) {
    frame_data_.AssignWithDefault(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), from.frame_data_);
  }
  ::memcpy(&index_, &from.index_,
    static_cast<size_t>(reinterpret_cast<char*>(&flags_) -
    reinterpret_cast<char*>(&index_)) + sizeof(flags_));
  // @@protoc_insertion_point(copy_constructor:v1.model.H264VideoFrame)
}

void H264VideoFrame::SharedCtor() {
  ::PROTOBUF_NAMESPACE_ID::internal::InitSCC(&scc_info_H264VideoFrame_protos_2fmodel_2fv1_2fmedia_2eproto.base);
  frame_data_.UnsafeSetDefault(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
  ::memset(&index_, 0, static_cast<size_t>(
      reinterpret_cast<char*>(&flags_) -
      reinterpret_cast<char*>(&index_)) + sizeof(flags_));
}

H264VideoFrame::~H264VideoFrame() {
  // @@protoc_insertion_point(destructor:v1.model.H264VideoFrame)
  SharedDtor();
}

void H264VideoFrame::SharedDtor() {
  frame_data_.DestroyNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
}

void H264VideoFrame::SetCachedSize(int size) const {
  _cached_size_.Set(size);
}
const H264VideoFrame& H264VideoFrame::default_instance() {
  ::PROTOBUF_NAMESPACE_ID::internal::InitSCC(&::scc_info_H264VideoFrame_protos_2fmodel_2fv1_2fmedia_2eproto.base);
  return *internal_default_instance();
}


void H264VideoFrame::Clear() {
// @@protoc_insertion_point(message_clear_start:v1.model.H264VideoFrame)
  ::PROTOBUF_NAMESPACE_ID::uint32 cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  frame_data_.ClearToEmptyNoArena(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited());
  ::memset(&index_, 0, static_cast<size_t>(
      reinterpret_cast<char*>(&flags_) -
      reinterpret_cast<char*>(&index_)) + sizeof(flags_));
  _internal_metadata_.Clear();
}

const char* H264VideoFrame::_InternalParse(const char* ptr, ::PROTOBUF_NAMESPACE_ID::internal::ParseContext* ctx) {
#define CHK_(x) if (PROTOBUF_PREDICT_FALSE(!(x))) goto failure
  while (!ctx->Done(&ptr)) {
    ::PROTOBUF_NAMESPACE_ID::uint32 tag;
    ptr = ::PROTOBUF_NAMESPACE_ID::internal::ReadTag(ptr, &tag);
    CHK_(ptr);
    switch (tag >> 3) {
      // int32 index = 1[json_name = "index"];
      case 1:
        if (PROTOBUF_PREDICT_TRUE(static_cast<::PROTOBUF_NAMESPACE_ID::uint8>(tag) == 8)) {
          index_ = ::PROTOBUF_NAMESPACE_ID::internal::ReadVarint(&ptr);
          CHK_(ptr);
        } else goto handle_unusual;
        continue;
      // int32 flags = 2[json_name = "flags"];
      case 2:
        if (PROTOBUF_PREDICT_TRUE(static_cast<::PROTOBUF_NAMESPACE_ID::uint8>(tag) == 16)) {
          flags_ = ::PROTOBUF_NAMESPACE_ID::internal::ReadVarint(&ptr);
          CHK_(ptr);
        } else goto handle_unusual;
        continue;
      // bytes frame_data = 3[json_name = "frameData"];
      case 3:
        if (PROTOBUF_PREDICT_TRUE(static_cast<::PROTOBUF_NAMESPACE_ID::uint8>(tag) == 26)) {
          auto str = _internal_mutable_frame_data();
          ptr = ::PROTOBUF_NAMESPACE_ID::internal::InlineGreedyStringParser(str, ptr, ctx);
          CHK_(ptr);
        } else goto handle_unusual;
        continue;
      default: {
      handle_unusual:
        if ((tag & 7) == 4 || tag == 0) {
          ctx->SetLastTag(tag);
          goto success;
        }
        ptr = UnknownFieldParse(tag, &_internal_metadata_, ptr, ctx);
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

::PROTOBUF_NAMESPACE_ID::uint8* H264VideoFrame::_InternalSerialize(
    ::PROTOBUF_NAMESPACE_ID::uint8* target, ::PROTOBUF_NAMESPACE_ID::io::EpsCopyOutputStream* stream) const {
  // @@protoc_insertion_point(serialize_to_array_start:v1.model.H264VideoFrame)
  ::PROTOBUF_NAMESPACE_ID::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  // int32 index = 1[json_name = "index"];
  if (this->index() != 0) {
    target = stream->EnsureSpace(target);
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::WriteInt32ToArray(1, this->_internal_index(), target);
  }

  // int32 flags = 2[json_name = "flags"];
  if (this->flags() != 0) {
    target = stream->EnsureSpace(target);
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::WriteInt32ToArray(2, this->_internal_flags(), target);
  }

  // bytes frame_data = 3[json_name = "frameData"];
  if (this->frame_data().size() > 0) {
    target = stream->WriteBytesMaybeAliased(
        3, this->_internal_frame_data(), target);
  }

  if (PROTOBUF_PREDICT_FALSE(_internal_metadata_.have_unknown_fields())) {
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormat::InternalSerializeUnknownFieldsToArray(
        _internal_metadata_.unknown_fields(), target, stream);
  }
  // @@protoc_insertion_point(serialize_to_array_end:v1.model.H264VideoFrame)
  return target;
}

size_t H264VideoFrame::ByteSizeLong() const {
// @@protoc_insertion_point(message_byte_size_start:v1.model.H264VideoFrame)
  size_t total_size = 0;

  ::PROTOBUF_NAMESPACE_ID::uint32 cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  // bytes frame_data = 3[json_name = "frameData"];
  if (this->frame_data().size() > 0) {
    total_size += 1 +
      ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::BytesSize(
        this->_internal_frame_data());
  }

  // int32 index = 1[json_name = "index"];
  if (this->index() != 0) {
    total_size += 1 +
      ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::Int32Size(
        this->_internal_index());
  }

  // int32 flags = 2[json_name = "flags"];
  if (this->flags() != 0) {
    total_size += 1 +
      ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::Int32Size(
        this->_internal_flags());
  }

  if (PROTOBUF_PREDICT_FALSE(_internal_metadata_.have_unknown_fields())) {
    return ::PROTOBUF_NAMESPACE_ID::internal::ComputeUnknownFieldsSize(
        _internal_metadata_, total_size, &_cached_size_);
  }
  int cached_size = ::PROTOBUF_NAMESPACE_ID::internal::ToCachedSize(total_size);
  SetCachedSize(cached_size);
  return total_size;
}

void H264VideoFrame::MergeFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) {
// @@protoc_insertion_point(generalized_merge_from_start:v1.model.H264VideoFrame)
  GOOGLE_DCHECK_NE(&from, this);
  const H264VideoFrame* source =
      ::PROTOBUF_NAMESPACE_ID::DynamicCastToGenerated<H264VideoFrame>(
          &from);
  if (source == nullptr) {
  // @@protoc_insertion_point(generalized_merge_from_cast_fail:v1.model.H264VideoFrame)
    ::PROTOBUF_NAMESPACE_ID::internal::ReflectionOps::Merge(from, this);
  } else {
  // @@protoc_insertion_point(generalized_merge_from_cast_success:v1.model.H264VideoFrame)
    MergeFrom(*source);
  }
}

void H264VideoFrame::MergeFrom(const H264VideoFrame& from) {
// @@protoc_insertion_point(class_specific_merge_from_start:v1.model.H264VideoFrame)
  GOOGLE_DCHECK_NE(&from, this);
  _internal_metadata_.MergeFrom(from._internal_metadata_);
  ::PROTOBUF_NAMESPACE_ID::uint32 cached_has_bits = 0;
  (void) cached_has_bits;

  if (from.frame_data().size() > 0) {

    frame_data_.AssignWithDefault(&::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(), from.frame_data_);
  }
  if (from.index() != 0) {
    _internal_set_index(from._internal_index());
  }
  if (from.flags() != 0) {
    _internal_set_flags(from._internal_flags());
  }
}

void H264VideoFrame::CopyFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) {
// @@protoc_insertion_point(generalized_copy_from_start:v1.model.H264VideoFrame)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

void H264VideoFrame::CopyFrom(const H264VideoFrame& from) {
// @@protoc_insertion_point(class_specific_copy_from_start:v1.model.H264VideoFrame)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

bool H264VideoFrame::IsInitialized() const {
  return true;
}

void H264VideoFrame::InternalSwap(H264VideoFrame* other) {
  using std::swap;
  _internal_metadata_.Swap(&other->_internal_metadata_);
  frame_data_.Swap(&other->frame_data_, &::PROTOBUF_NAMESPACE_ID::internal::GetEmptyStringAlreadyInited(),
    GetArenaNoVirtual());
  swap(index_, other->index_);
  swap(flags_, other->flags_);
}

::PROTOBUF_NAMESPACE_ID::Metadata H264VideoFrame::GetMetadata() const {
  return GetMetadataStatic();
}


// @@protoc_insertion_point(namespace_scope)
}  // namespace model
}  // namespace v1
PROTOBUF_NAMESPACE_OPEN
template<> PROTOBUF_NOINLINE ::v1::model::Image* Arena::CreateMaybeMessage< ::v1::model::Image >(Arena* arena) {
  return Arena::CreateInternal< ::v1::model::Image >(arena);
}
template<> PROTOBUF_NOINLINE ::v1::model::PointCloud* Arena::CreateMaybeMessage< ::v1::model::PointCloud >(Arena* arena) {
  return Arena::CreateInternal< ::v1::model::PointCloud >(arena);
}
template<> PROTOBUF_NOINLINE ::v1::model::H264VideoFrame* Arena::CreateMaybeMessage< ::v1::model::H264VideoFrame >(Arena* arena) {
  return Arena::CreateInternal< ::v1::model::H264VideoFrame >(arena);
}
PROTOBUF_NAMESPACE_CLOSE

// @@protoc_insertion_point(global_scope)
#include <google/protobuf/port_undef.inc>