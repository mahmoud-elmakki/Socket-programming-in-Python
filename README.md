# Socket-programming-in-Python
Building a multiconnection client-server application using the main functions and methods in Python’s socket module, and sending messages and data between endpoints.

## Overview
Sockets and the socket API are used to send messages across a network. They provide a form of inter-process communication (IPC). The network can be a logical, local network to the computer, or one that’s physically connected to an external network, with its own connections to other networks. The obvious example is the Internet, which you connect to via your ISP.

## echo client and server

When using the loopback interface (IPv4 address 127.0.0.1 or IPv6 address ::1), data never leaves the host or touches the external network.
![alt text](https://github.com/hotasalah/Socket-programming-in-Python/blob/master/sockets-loopback-interface.44fa30c53c70.jpg)

Running the echo server...
![alt text](https://github.com/hotasalah/Socket-programming-in-Python/blob/master/echo%20server.png)

Running the echo client...
![alttext](https://github.com/hotasalah/Socket-programming-in-Python/blob/master/echo%20client.png)

## Multiconnection client and server

When using an IP address other than 127.0.0.1 or ::1 in the applications, it’s probably bound to an Ethernet interface that’s connected to an external network. This is the gateway to other hosts outside of the localhost.
![alt text](https://github.com/hotasalah/Socket-programming-in-Python/blob/master/sockets-ethernet-interface.aac312541af5.jpg)

Running the multiconnection server...
![alt text](https://github.com/hotasalah/Socket-programming-in-Python/blob/master/multiconnection%20server.png)

Running the multiconnection client...
![alt text](https://github.com/hotasalah/Socket-programming-in-Python/blob/master/multiconnection%20client.png)

## TCP Sockets

Sockets TCP Flow
![alt text](https://github.com/hotasalah/Socket-programming-in-Python/blob/master/sockets-tcp-flow.1da426797e37.jpg)

#### Why using TCP?
The Transmission Control Protocol (TCP):

Is reliable: packets dropped in the network are detected and retransmitted by the sender.

Has in-order data delivery: data is read by your application in the order it was written by the sender

