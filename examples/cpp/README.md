## Content

This directory contains example C++ source code that interacts with Formant Agent.

## Setup

1. Install apt dependencies:
```
sudo apt-get install build-essential autoconf libtool pkg-config automake curl cmake
```

2. Install gRPC using CMake.

Clone the source code:
```
git clone -b $(curl -L https://grpc.io/release) https://github.com/grpc/grpc
cd grpc
git submodule update --init
```

Build and install:
```
cmake .
make
sudo make install
```

3. Clone the Formant repository and navigate to the C++ examples.

```
git clone https://github.com/FormantIO/formant.git
cd formant/examples/cpp
```

4. Generate the C++ gRPC code.
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

2. Run each example to ingest a test datapoint:
```
./send_textdatapoint

./send_numeric_datapoint
```