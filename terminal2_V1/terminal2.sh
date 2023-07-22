#!/bin/sh

# Execute:
# $ chmod +x terminal2.sh 
# $ ./terminal2.sh

clear
while :
do
	echo "[ctrl+c to quit] Type c to commands list."
	read INPUT_STRING
	clear
	echo ": $INPUT_STRING"
	case $INPUT_STRING in
		f)			firefox http://marocero2016.blogspot.com & ;;
		c)			gedit .apps & ;;
		# ----- Apps Shortcuts:
		t)			gedit & ;; #1
		ter)			gnome-terminal & ;; #2
		bro)			gnome-terminal firefox & ;; #3
		# ----- Commands shortcuts:
		comm)		gedit .Commands & ;; #1
		input)		lshw -short -c multimedia -c input ;; #2
		usb)		lsusb ;; #3
		cal)		cal ;; #4
		'date')		date ;; #5
		top)		top ;; #6
		pci)		lspci ;; #7
		distro)		cat /etc/os-release ;; #8
		disk)		df -h ;; #9
		calc)		python3 ;; #10
		ram)		free ;; #11
		*)			echo COMMAND INVALID! ;;
 	esac
done




