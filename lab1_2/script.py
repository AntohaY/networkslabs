from socket import *
import struct
import time
from datetime import datetime

NTP_SERVER = "time.google.com"
# this is the unix time for January  1 1970
TIME1970 = 2208988800
# create a client socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
# connect to ntp port
portNumber = 123


def sntp_client():

    # data to be encrypted and sent to ntp server
    data = '\x1b' + 47 * '\0'

    # sending data to ntp
    dt = datetime.now()
    # send data to ntp server through port
    clientSocket.sendto( data.encode('utf-8'), ( NTP_SERVER, portNumber ))
    # receive the data and address
    data, address = clientSocket.recvfrom(1024)
    # received data from NTP
    dt1 = datetime.now()

    # if there is data return do the following
    if data:
        print ('Response received from:', address)

        t_time = struct.unpack( '!12I', data )[10]
        # subtract January 1 1970 to get current date and time
        t_time -= TIME1970
        # print time and date
        print ('Time= ',time.ctime(t_time))
        print ('Sync time : ', dt1-dt)
    # close socket
    clientSocket.close()
# main
if __name__ == '__main__':
    sntp_client()