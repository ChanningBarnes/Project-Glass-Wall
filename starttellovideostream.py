import socket

# Tello drone address and command port
TELLO_IP = "192.168.10.1"
TELLO_PORT = 8889

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(3.0)  # Set timeout for response

def send_command(command):
    try:
        print(f"Sending command: {command}")
        sock.sendto(command.encode(), (TELLO_IP, TELLO_PORT))
        response, _ = sock.recvfrom(1024)  # Receive response
        print(f"Tello Response: {response.decode()}")
    except socket.timeout:
        print("No response from Tello!")

# Send initialization commands
send_command("command")  # Enter SDK mode
send_command("streamon")  # Start video stream

sock.close()
