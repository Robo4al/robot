#!/bin/bash

porta=/dev/ttyUSB0

velocidade=115200

arquivos=("boot.py" "main.py" "ftp.py" "ftp_thread.py" "uftpd.py")

x=0
while [ $x != ${#arquivos[@]} ]
do
	echo "Copiando o arquivo \""${arquivos[$x]}"\"."
	ampy -p $porta put ./${arquivos[$x]} ${arquivos[$x]}
	let "x = x +1"
done

echo "Reiniciando o ESP32..."
ampy -p $porta reset --repl

echo "Iniciando..."
screen $porta $velocidade
