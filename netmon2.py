import os, time
from icmplib import ping
from getmac import get_mac_address
from mac_vendor_lookup import MacLookup


def mon():
	while True:
		os.system('clear')
		f = open('ips.txt').read().splitlines()
		print('='*40)
		for ips in f:
			host = ping(ips, count=2, interval=.1, timeout=.5, privileged=True)
			if host.is_alive:
				print(f"[Live] {host.address} | sent/recv: {host.packets_sent}/{host.packets_received}  ")
			else:
				print(f"[Dead] {host.address} | sent/recv: {host.packets_sent}/{host.packets_received}  ")
		time.sleep(5)


def saved_scan():
	os.system('rm ips.txt')
	for i in range(1,256):
		try:
			ip = f'192.168.0.{i}'
			host = ping(ip, count=5, interval=.1, timeout=.5,privileged=True)
			if host.is_alive:
				print(f" {host.address} | sent/recv: {host.packets_sent}/{host.packets_received}  ")
				mac = get_mac_address(host.address)
				vend = MacLookup().lookup(mac)
				print(f"{mac} | {vend}\n")
				f = open('ips.txt','a')
				f.write(host.address+'\n')
				f.close()
			else:
				pass
		except:
			pass
	mon()

saved_scan()
# saved scan
# while true scan monitor
# new scan and alert if new
