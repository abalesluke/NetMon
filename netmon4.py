import os, concurrent.futures
from getmac import get_mac_address
from mac_vendor_lookup import MacLookup
from icmplib import ping
from colorama import Fore

live = []
ipz = '192.168.1.'

def check(ip):
    host = ping(ip, count=1, interval=.1, timeout=1.5, privileged=True)
    if host.is_alive:
        return True
    else:
        return False

def mon():
    while True:
        live_hosts = []
        dead_hosts = []
        hosts_list = open('save_host.txt').read().splitlines()
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            for host in hosts_list:
                #mac = get_mac_address(host)
                #vend = MacLookup().lookup(mac)
                checker = executor.submit(check, host)
                isLive = checker.result()
                if isLive:
                    live_hosts.append(f"{host}")
                else:
                    dead_hosts.append(f"{host}")

        os.system('clear')
        print(Fore.BLUE+"="*40)
        print(f"|{Fore.YELLOW}Status{Fore.BLUE}|{Fore.YELLOW} Ip Address{Fore.BLUE} |{Fore.YELLOW} Mac{Fore.BLUE} |{Fore.YELLOW} Vendor{Fore.BLUE}")
        print("="*40)
        for lh in live_hosts:
            print(f"{Fore.BLUE}|[{Fore.GREEN}LIVE{Fore.BLUE}] {Fore.YELLOW}{lh}")
        for dh in dead_hosts:
            print(f"{Fore.BLUE}|[{Fore.RED}DEAD{Fore.BLUE}] {Fore.YELLOW}{dh}")


def ss():
    print("Running save scan!")
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        for ip in range(254):
            host_ip = ipz+str(ip)
            checker = executor.submit(check, host_ip)
            isAlive = checker.result()
            if isAlive:
                live.append(host_ip)

    for host in live:
        f=open('save_host.txt','a')
        f.write(host+'\n')
        print(host)
    mon()

if __name__ == "__main__":
    if(os.path.exists('save_host.txt')is False):
        ss()
    else:
        print('Starting to monitor..')
        mon()


"""
192.168.1.1
192.168.1.2
192.168.1.7
192.168.1.9
192.168.1.13
192.168.1.19
"""
