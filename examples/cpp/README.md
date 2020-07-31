## Content

This directory contains example C++ source code that interacts with Formant Agent. It is built to run on Ubuntu Linux 18.04.

## Setup

1. Install apt dependencies:
```
sudo apt-get install build-essential autoconf libtool pkg-config automake curl cmake libjsoncpp-dev
```

2. Install gRPC using CMake.

Clone the source code:
```
git clone -b $(curl -L https://grpc.io/release) https://github.com/grpc/grpc
cd grpc
git submodule update --init
```

Build and install (for cmake version 3.11 and up):
```
cmake .
make
sudo make install
```

For earlier versions of cmake, the grpc project provides a more robust install script here: https://github.com/grpc/grpc/blob/master/test/distrib/cpp/run_distrib_test_cmake.sh

3. Clone the Formant repository to a new location and navigate to the C++ examples.

```
git clone https://github.com/FormantIO/formant.git
cd formant/examples/cpp
```

4. Generate the C++ gRPC code. It is already checked in with the repository, and this step is only necessary if your installed `protoc` version differs substantially from the version used to previously generate the code.
```
protoc -I ../.. --grpc_out=. --plugin=protoc-gen-grpc=`which grpc_cpp_plugin` ../../protos/*/v1/*.proto
protoc -I ../.. --cpp_out=. ../../protos/*/v1/*.proto
```

5. Build the example project.
```
cmake .
make
```

## Running examples

1. Make sure Formant Agent is running.
```
systemctl status formant-agent | grep Active:
```

2. Run each send example to ingest a test datapoint:
```
./send_text_datapoint

./send_bitset_datapoint

./send_numeric_datapoint

./send_file_datapoint

./send_json_datapoint

./send_image_datapoint

./send_localization_datapoint

./send_gps_location_datapoint
```

3. Run the commands listener and then trigger a command from the app:
```
./receive_commands
```

4. Get and print the current custom configuration parameters
```
./get_config_params
```