import syft as sy
import Const


def activate_server_hook(torch):
    return sy.TorchHook(torch)


def generate_client_hook(torch, server):
    return sy.TorchHook(torch, local_worker=server)


def make_remote_client(host, hook, id, port):
    from syft.workers.websocket_client import WebsocketClientWorker
    return WebsocketClientWorker(host=host, hook=hook, id=id, port=port)


def make_socket_server(host, hook, id, port, log_msgs=True, verbose=True):
    from syft.workers.websocket_server import WebsocketServerWorker
    return WebsocketServerWorker(host=host, hook=hook, id=id, port=port,
                                 log_msgs=log_msgs, verbose=verbose)


def main():
    import torch
    server_hook = activate_server_hook(torch)
    server = make_socket_server(host=Const.server_host,
                                hook=server_hook,
                                id=Const.server_id,
                                port=Const.server_port)

    client_hook = generate_client_hook(torch=torch, server=server)
    client = make_remote_client(host=Const.client_host,
                                hook=client_hook,
                                id=Const.client_id,
                                port=Const.client_port)

    client_hook.local_worker.add_worker(client)

    # server.start()
    # server.list_objects()
    # server.objects_count()


if __name__ == "__main__":
    main()
