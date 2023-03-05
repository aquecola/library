import os

# Установка OpenVPN
os.system("sudo apt-get update")
os.system("sudo apt-get install openvpn")

# Создание конфигурационного файла
with open('/etc/openvpn/client.conf', 'w') as f:
    f.write('client\n')
    f.write('dev tun\n')
    f.write('proto udp\n')
    f.write('remote example.com 1194\n')
    f.write('resolv-retry infinite\n')
    f.write('nobind\n')
    f.write('persist-key\n')
    f.write('persist-tun\n')
    f.write('ca ca.crt\n')
    f.write('cert client.crt\n')
    f.write('key client.key\n')
    f.write('comp-lzo\n')
    f.write('verb 3\n')

# Запуск OpenVPN
os.system("sudo openvpn /etc/openvpn/client.conf")