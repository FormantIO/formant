cmake_minimum_required(VERSION 3.11)

project(formant-examples)

add_compile_options(-std=c++11)

find_package(Threads REQUIRED)
find_package(protobuf CONFIG REQUIRED)
find_package(gRPC CONFIG REQUIRED)

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