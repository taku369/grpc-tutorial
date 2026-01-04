## Server

```
$ cargo run --bin hello-server
   Compiling hello v0.1.0 (/Users/tfujino/programming/grpc-tutorial/rust/hello)
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 3.79s
     Running `target/debug/hello-server`
gRPC server listening on [::1]:50051
```

## Client

```
$ cargo run --bin hello-client
   Compiling hello v0.1.0 (/Users/tfujino/programming/grpc-tutorial/rust/hello)
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 2.00s
     Running `target/debug/hello-client`
RESPONSE="Hello, Jane doe!"
```

## Trouble shooting
https://github.com/tokio-rs/prost/issues/1264#issuecomment-2806894506

```
[dependencies]
protoc-gen-tonic = { version = "0.4" }
```

で動いた
