""" Core component for connections checks """
import socket
import time
import collections

Server = collections.namedtuple('Server', 'host port')

def check_connection(server, port):
    """ Checks connection to server on given port """
    try:
        sock = socket.create_connection((server, port), timeout=5)
    except socket.error:
        return False
    else:
        sock.close()
    return True


def load_servers(filepath):
    """ Loads host and port as Server tuple from given file"""
    ret = []
    with open(filepath, 'r') as f:
        for line in f.readlines():
            tokens = line.strip().split(':')
            if len(tokens) >= 1:
                host = tokens[0]
                port = int(tokens[1]) if len(tokens) >= 2 else 80
                ret.append(Server(host, port))
    return ret


if __name__ == "__main__":
    for srv in load_servers('server.list'):
        tstart = time.perf_counter()
        status = 'OK' if check_connection(srv.host, srv.port) else 'Failed'
        tstop = time.perf_counter()
        print('{0: >20}:{1: <5} -- {2: .3f}s -- {3}'.format(
            srv.host, srv.port, tstop - tstart, status))
