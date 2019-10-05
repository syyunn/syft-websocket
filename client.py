import torch

import syft as sy
from syft.workers import websocket_client as wsc
from syft.workers.websocket_server import WebsocketServerWorker


hook = sy.TorchHook(torch)

server1_kwargs = {
    "id": 'mbp1',
    "host": 'localhost',
    "port": '8001',
    "hook": hook,
    "verbose": True,
}

server1 = WebsocketServerWorker(**server1_kwargs)


server2_kwargs = {
    "id": 'mbp2',
    "host": 'localhost',
    "port": '8002',
    "hook": hook,
    "verbose": True,
}

server2 = WebsocketServerWorker(**server2_kwargs)

server3_kwargs = {
    "id": 'mbp3',
    "host": 'localhost',
    "port": '8003',
    "hook": hook,
    "verbose": True,
}

server3 = WebsocketServerWorker(**server3_kwargs)



tensor = torch.tensor([2.], requires_grad=True)
# target = torch.tensor([[0.], [0.]], requires_grad=True)

server2.load_data(tensor)
print(list(server2._objects.keys())[0])

server2_tensor = server2.get_obj(list(server2._objects.keys())[0])
print("server2 tensor: ", server2_tensor)

x = server2_tensor.share(server1, server2, crypto_provider=server3)

print("shared x: ", x)

print(server1._objects)
print(server2._objects)
print(list(server2._objects))

for key in list(server2._objects):
    print("each: ", server2._objects[key])
    server2._objects[key].get()



# # print(x)
# print(x.get())
#
# print(server1._objects)
# print(server2._objects)


# kwargs_websocket = {"hook": hook,
#                     "verbose": True,
#                     "host": "127.0.0.1"}

# mbp2 = wsc.WebsocketClientWorker(id="mbp2",
#                                  port=8002,
#                                  **kwargs_websocket)
# print(mbp2.list_objects_remote())
#
# mbp1 = wsc.WebsocketClientWorker(id="mbp",
#                                  port=8001,
#                                  **kwargs_websocket)
#
#
# print(mbp1.list_objects_remote())
# # print(mbp2.list_objects_remote())

# res = server1.request_obj(list(server2._objects.keys())[0], server2)

######################### SANE BLOCK : WORKS FINE #####################
# print(server1._objects)
# print(server2._objects)
# print(server2.get_obj(list(server2._objects.keys())[0]).send(server1))
# print(server1._objects)
# print(server2._objects)
######################### SANE BLOCK : WORKS FINE #####################



if __name__ == "__main__":
    pass
