from socket import *
import struct
import sys
import time

def getTime():
    NTP_SERVER = "130.225.96.8"
    TIME1970 = 2208988800L      # Thanks to F.Lundh

    client = socket( AF_INET, SOCK_DGRAM )
    data = '\x1b' + 47 * '\0'
    client.sendto( data, ( NTP_SERVER, 123 ))
    data, address = client.recvfrom( 1024 )
    if data:
        s = struct.unpack( '!12I', data )
        return s[10], s[11]
    return None
