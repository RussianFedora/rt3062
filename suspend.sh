#!/bin/bash

WLAN=$(cat /sys/class/rfkill/rfkill0/state)

if [ $WLAN -eq 0 ] ; then
	service NetworkManager stop
	sleep 1
	modprobe pciehp pciehp_force=1
	echo 1 > /sys/class/rfkill/rfkill0/state
	sleep 1
	modprobe rt2870sta
	rmmod pciehp
	service NetworkManager start
else
	service NetworkManager stop
	sleep 1
	modprobe pciehp pciehp_force=1
	ifconfig ra0 down
	rmmod rt2870sta
	sleep 1
	echo 0 > /sys/class/rfkill/rfkill0/state
	rmmod pciehp
	service NetworkManager start
fi
