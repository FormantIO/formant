cmake_minimum_required(VERSION 3.10)

project(formant-examples)

add_compile_options(-std=c++11)

find_package(Threads REQUIRED)
find_package(protobuf CONFIG REQUIRED)
find_package(gRPC CONFIG REQUIRED)
find_package(Boost)

IF (Boost_FOUND)
    INCLUDE_DIRECTORIES(${Boost_INCLUDE_DIR})
    ADD_DEFINITIONS( "-DHAS_BOOST" )
ENDIF()

include_directories(.)
include_directories(protos)

file(
  GLOB
  INCLUDES
  protos/*/v1/*
)

add_executable(
  send_text_datapoint 
  send_text_datapoint.cpp
  ${INCLUDES}
)
target_link_libraries(
  send_text_datapoint 
  gRPC::grpc++
  protobuf::libprotobuf
)

add_executable(
  send_numeric_datapoint 
  send_numeric_datapoint.cpp
  ${INCLUDES}
)
target_link_libraries(
  send_numeric_datapoint 
  gRPC::grpc++
  protobuf::libprotobuf
)

add_executable(
  send_file_datapoint 
  send_file_datapoint.cpp
  ${INCLUDES}
)
target_link_libraries(
  send_file_datapoint 
  gRPC::grpc++
  protobuf::libprotobuf
)

add_executable(
  receive_commands 
  receive_commands.cpp
  ${INCLUDES}
)
target_link_libraries(
  receive_commands 
  gRPC::grpc++
  protobuf::libprotobuf
)

add_executable(
  formant_client_example 
  formant_client_example.cpp
  ${INCLUDES}
)
target_link_libraries(
  formant_client_example 
  gRPC::grpc++
  protobuf::libprotobuf
)

add_executable(
  get_config_params
  get_config_params.cpp
  ${INCLUDES}
)
target_link_libraries(
  get_config_params 
  gRPC::grpc++
  protobuf::libprotobuf
)

add_executable(
  send_json_datapoint
  send_json_datapoint.cpp
  ${INCLUDES}
)
target_link_libraries(
  send_json_datapoint 
  gRPC::grpc++
  protobuf::libprotobuf
)

add_executable(
  send_bitset_datapoint
  send_bitset_datapoint.cpp
  ${INCLUDES}
)
target_link_libraries(
  send_bitset_datapoint 
  gRPC::grpc++
  protobuf::libprotobuf
)

add_executable(
  send_image_datapoint
  send_image_datapoint.cpp
  ${INCLUDES}
)
target_link_libraries(
  send_image_datapoint 
  gRPC::grpc++
  protobuf::libprotobuf
)

add_executable(
  send_gps_location_datapoint
  send_gps_location_datapoint.cpp
  ${INCLUDES}
)
target_link_libraries(
  send_gps_location_datapoint
  gRPC::grpc++
  protobuf::libprotobuf
)

add_executable(
  send_localization_datapoint
  send_localization_datapoint.cpp
  ${INCLUDES}
)
target_link_libraries(
  send_localization_datapoint
  gRPC::grpc++
  protobuf::libprotobuf
)

add_executable(
  send_event
  send_event.cpp
  ${INCLUDES}
)
target_link_libraries(
  send_event
  gRPC::grpc++
  protobuf::libprotobuf
)

add_executable(
  send_receive_intervention_request
  send_receive_intervention_request.cpp
  ${INCLUDES}
)
target_link_libraries(
  send_receive_intervention_request
  gRPC::grpc++
  protobuf::libprotobuf
)

add_executable(
  formant_agent_client
  formant_agent_client.cpp
  ${INCLUDES}
)
target_link_libraries(
  formant_agent_client
  gRPC::grpc++
  protobuf::libprotobuf
)
