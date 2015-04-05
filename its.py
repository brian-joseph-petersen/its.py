# RFC 868 Time Protocol
from binascii import hexlify
from calendar import timegm
from socket import socket, error, timeout, AF_INET, SOCK_STREAM
from time import gmtime, localtime, strftime
class time():
    def __init__( self ):
        self.strftime, self.date, self.time = None, None, None
        self.year, self.month, self.day = None, None, None
        self.hour, self.minute, self.second = None, None, None
        data, host, service = None, [], socket( AF_INET, SOCK_STREAM )
        host.append( "time-a.timefreq.bldrdoc.gov" )
        host.append( "time-b.timefreq.bldrdoc.gov" )
        host.append( "time-c.timefreq.bldrdoc.gov" )
        for index in xrange( len( host ) ):
            try:
                service.settimeout( 10 )
                service.connect( ( host[index], 37 ) )
                data = service.recv( 32 )
                service.close()
                break
            except error: continue
            except timeout: continue
        if data is None: return
        # 2208988800 seconds corresponds to Thu, 01 Jan 1970 00:00:00 GMT
        # this base will serve until Tue, 19 Jan 2038 03:14:07 GMT
        utc_offset = timegm( gmtime() ) - timegm( localtime() )
        data = gmtime( int( hexlify( data ), 16 ) - ( 2208988800 + utc_offset ) )
        self.strftime = strftime( "%Y-%m-%d %H:%M:%S", data )
        self.date, self.time = self.strftime.split()
        self.year, self.month, self.day = self.date.split( "-" )
        self.hour, self.minute, self.second = self.time.split( ":" )