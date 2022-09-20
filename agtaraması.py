import scapy.all as scapy
import sys

ip_adresi = str(input("İp adresini girinz : "))
subnet_mask = int(input("Subnet mask degerini giriniz : "))

try:
    ARP_request_line = scapy.ARP(pdst=f"{ip_adresi}/{subnet_mask}")
    Brodcast_stream_ = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    Proccess_result_ = Brodcast_stream_ / ARP_request_line

    (answered_list, unanswered_list) = scapy.srp(Proccess_result_, timeout=1)
    print(answered_list.summary())

except Exception as E:
    print(E)
    sys.exit()

except KeyboardInterrupt:
    print("'CTRL + C' basıldı")




#if subnet_mask < 1 or subnet_mask > 32:
#    print("tekrar griniz")
#    exit()
#else:


        # presult = answered_list.summary()

        # print(presult)







