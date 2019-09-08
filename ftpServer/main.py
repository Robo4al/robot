# wifi_ssid = "nomeDaRede"
# wifi_passwd = "senha"
# my_timezone = "CET-1CEST"

# import network
# import machine
# import time

# sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
# sta_if.connect(wifi_ssid, wifi_passwd)

# time.sleep(6)
# sta_if.ifconfig()


# print("A rede foi iniciada...")
# while not sta_if.isconnected():
#       pass

# print('Configurações da rede: ', sta_if.ifconfig())
# time.sleep(26)


import network
ap = network.WLAN(network.AP_IF)
ap.config(essid='ESP-AP')
ap.active(True)
print("Rede Wifi.")


print("Iniciando o FTP...")
import uftpd

print("Concluido.")