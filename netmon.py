import os
from getmac import get_mac_address
from getmac import getmac
from mac_vendor_lookup import MacLookup

while True:
 host = '192.168.0.'
 print("="*55)
 print("        MAC          |        Vendor                   ")
 print("="*55)
 for i in range(1, 254):
  client = host+str(i)
  mac = getmac.get_mac_address(ip=client, network_request=True)
  try:
   if mac == "00:00:00:00:00:00":
    pass
   else:
   	os.system(f'echo {mac} >> mac.txt')
   	vendor = MacLookup().lookup(mac)
   	print(f' {mac}  :|: {vendor}  ')

  except:
   pass
