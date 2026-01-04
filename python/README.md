## Build

```
python -m grpc_tools.protoc \
  -I. \
  --python_out=. \
  --grpc_python_out=. \
  hello.proto
```


## Server

```
$ uv run python server.py
gRPC server started on port 50051
```

## Client

```
$ uv run python client.py
Hello, John doe!
```
