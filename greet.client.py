import greet_pb2
import greet_pb2_grpc
import time
import grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel :
        stub = greet_pb2_grpc.GreeterStub(channel)
        print("1. SayHello -Unary")
        print("2. ParrotSayHello -Server Side Streaming")
        rpc_call = input("which rpc would you like to make: ")
        if rpc_call=="1":
           hello_request=greet_pb2.HelloRequest(greeting= "Good Morning ,Guten Morgen,صباح الخير")
           hello_reply=stub.SayHello(hello_request)
           print("sayhello response received")
           print(hello_reply)
        elif rpc_call=="2":
            hello_request= greet_pb2.HelloRequest(greeting = "Good Morning, Guten Morgen, صباح الخير")
            hello_replies=stub.ParrotSayHello(hello_request)
            for hello_reply in hello_replies:
                print("ParrotSaysHello Response Received:")
                print(hello_reply) 
if __name__ == "__main__" :
    run()            