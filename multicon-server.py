import socket
import selectors
import types
import sys


sel = selectors.DefaultSelector()


def accept_wrapper(sock):

	conn, addr = sock.accept()
	print("accepted connection from: ", addr)

	conn.setblocking(False)

	data = types.SimpleNamespace(addr=addr, inb=b'', outb = b'')

	events = selectors.EVENT_READ | selectors.EVENT_WRITE

	sel.register(conn, events, data=data)


def service_connection(key, mask):

	sock = key.fileobj
	data = key.data

	if mask & selectors.EVENT_READ:
		recv_data = sock.recv(1024)

		if recv_data:
			data.outb += recv_data

		else:
			print("closing connection to: ", data.addr)
			sel.unregister(sock)
			sock.close()

	if mask & selectors.EVENT_WRITE:

		if data.outb:

			print("echoing: ", repr(data.outb), "to connection: ", data.addr)
			sent = sock.send(data.outb)
			data.outb = data.outb[sent:]



if len(sys.argv) != 3:
	print("usage: ", sys.argv[0], "<host> <port>")
	sys.exit(1)

host, port = sys.argv[1], int(sys.argv[2])


lisock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

lisock.bind((host, port))

lisock.listen()
print("listening on: ", (host, port))

lisock.setblocking(False)

sel.register(lisock, selectors.EVENT_READ, data=None)

try:
	while True:
		event = sel.select(timeout=None)

		for key, mask in event:

			if key.data is None:
				accept_wrapper(key.fileobj)
			else:
				service_connection(key, mask)

except KeyboardInterrupt:
	print("caught keyboard interrupt")

finally:
	sel.close()
