# Socket-programming-in-Python
Building a multiconnection client-server application using the main functions and methods in Python’s socket module, and sending messages and data between endpoints.

## Overview
Sockets and the socket API are used to send messages across a network. They provide a form of inter-process communication (IPC). The network can be a logical, local network to the computer, or one that’s physically connected to an external network, with its own connections to other networks. The obvious example is the Internet, which you connect to via your ISP.

## echo client and server

Running the echo server...
![alt text](https://github.com/hotasalah/Socket-programming-in-Python/blob/master/echo%20server.png)

Running the echo client...
![alttext](https://github.com/hotasalah/Socket-programming-in-Python/blob/master/echo%20client.png)

## Multiconnection client and server

Running the multiconnection server...
![alt text](https://github.com/hotasalah/Socket-programming-in-Python/blob/master/multiconnection%20server.png)

Running the multiconnection client...
![alt text](https://github.com/hotasalah/Socket-programming-in-Python/blob/master/multiconnection%20client.png)

## TCP Sockets

Why using TCP? The Transmission Control Protocol (TCP):

Is reliable: packets dropped in the network are detected and retransmitted by the sender.

Has in-order data delivery: data is read by your application in the order it was written by the sender

