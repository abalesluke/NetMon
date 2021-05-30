import os, socket, sys
try:
	from getmac import get_mac_address
	from getmac import getmac
	from mac_vendor_lookup import MacLookup

except:
	os.system('pip3 install getmac')
	os.system('pip3 install mac_vendor_lookup')

print('started')

for i in range(1, 254):
	ip = f'192.168.0.{i}'
	for port in range(100):
		done = False
		if done == True:
			done = False
			break
		else:
			pass
		try:
			s = socket.socket()
			s.settimeout(.1)
			s.connect((f'{ip}', port))
			sys.stdout.write('\r                               ')
			print(f'\r[Open {port}] {ip} ')
			mac = getmac.get_mac_address(ip=ip, network_request=True)
			print('\r[MAC ] '+mac+'')
			print(f'\r[Vendor] {MacLookup().lookup(mac)}\n')
			done = True
			break
		except:
			sys.stdout.write(f'\r[Scanning] {port} {ip}   ')
			
