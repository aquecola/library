import os

# Установка WireGuard
os.system("sudo add-apt-repository ppa:wireguard/wireguard -y")
os.system("sudo apt-get update")
os.system("sudo apt-get install wireguard -y")

# Создание конфигурационного файла
with open('/etc/wireguard/wg0.conf', 'w') as f:
    f.write('[Interface]\n')
    f.write('PrivateKey = <private_key>\n') # Заменить <private_key> на приватный ключ
    f.write('Address = 10.0.0.1/24\n') # Установить адрес для VPN-интерфейса
    f.write('ListenPort = 51820\n') # Установить порт для прослушивания

    f.write('\n[Peer]\n')
    f.write('PublicKey = <public_key>\n') # Заменить <public_key> на публичный ключ
    f.write('AllowedIPs = 10.0.0.2/32\n') # Установить IP-адрес для удаленного клиента
    f.write('Endpoint = <server_public_ip>:51820\n') # Заменить <server_public_ip> на публичный IP-адрес сервера

# Запуск WireGuard
os.system("sudo systemctl enable wg-quick@wg0")
os.system("sudo systemctl start wg-quick@wg0")