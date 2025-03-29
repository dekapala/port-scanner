import socket

print("🔍 Escáner de Puertos Básico")
target = input("Ingrese la dirección IP o dominio a escanear: ")

start_port = int(input("Puerto inicial: "))
end_port = int(input("Puerto final: "))

print(f"\nEscaneando {target} del puerto {start_port} al {end_port}...\n")

for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target, port))
    
    if result == 0:
        print(f"✅ Puerto {port} está ABIERTO")
    sock.close()


