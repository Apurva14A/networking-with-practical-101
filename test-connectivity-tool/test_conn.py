import socket

def is_port_open(host, port):
    try:
        with socket.create_connection((host, port), timeout=5):
            return True
    except:
        return False

    
if __name__ == "__main__":
    host = "localhost"
    port = 80
    if is_port_open(host, port):
        print(f"Port {port} on {host} is open.")
    else:
        print(f"Port {port} on {host} is closed.")
    