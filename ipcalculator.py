#!/usr/bin/python

ip = raw_input( "please,input ip address [ d.d.d.d ]: " )
prefix = int ( raw_input( "please , input perfix: " ) )

def ipsplit():
	ipsplit = ip.split ( "." )
	return ipsplit

def ipshift():
	ipshift1 = int ( ipsplit() [0] ) << 24
	ipshift2 = int ( ipsplit() [1] ) << 16
	ipshift3 = int ( ipsplit() [2] ) << 8
	ipshift4 = int ( ipsplit() [3] )
	ipshift = ipshift1 | ipshift2 | ipshift3 | ipshift4
	return ipshift

def prefixshift(prefix):
	prefixshift = ( (2**prefix -1) << ( 32 - prefix ) )
	return prefixshift

def netip():
	netshift = ipshift() & prefixshift(prefix)
	net1 = netshift >> 24
	net2 = (netshift & ( 255 << 16 )) >> 16
	net3 = (netshift & ( 255 << 8 )) >> 8
	net4 = netshift & 255
	return "Network ip = %d.%d.%d.%d/%d" % (net1,net2,net3,net4,prefix)

def hostmin():
	netshift = ipshift() & prefixshift(prefix)
	net1 = netshift >> 24
	net2 = (netshift & ( 255 << 16 )) >> 16
	net3 = (netshift & ( 255 << 8 )) >> 8
	net4 = netshift & 255
	return "Hostmin = %d.%d.%d.%d/%d" % (net1,net2,net3,(net4+1),prefix)

def brodcast():
	b = ( 2**( 32 - prefix ) -1 )
	brodshift = ipshift() | b
	br1 = brodshift >> 24
	br2 = (brodshift & ( 255 << 16 )) >> 16
	br3 = (brodshift & ( 255 << 8 )) >> 8
	br4 = brodshift & 255
	return  "Brodcast = %d.%d.%d.%d" % ( br1, br2, br3, br4, )

def hostmax():
	b = ( 2**( 32 - prefix ) -1 )
	brodshift = ipshift() | b
	br1 = brodshift >> 24
	br2 = (brodshift & ( 255 << 16 )) >> 16
	br3 = (brodshift & ( 255 << 8 )) >> 8
	br4 = brodshift & 255
	return "Hostmax = %d.%d.%d.%d/%d" % (br1,br2,br3,(br4-1), prefix)

def subnet():
	sub = ( (2**prefix -1) << ( 32 - prefix ) )
	sub1 = sub >> 24
	sub2 = (sub & ( 255 << 16 )) >> 16
	sub3 = (sub & ( 255 << 8 )) >> 8
	sub4 = sub & 255
	return  "subnetmask = %d.%d.%d.%d"  %( sub1, sub2, sub3, sub4 )

def us():
	us = ( 2**( 32 - prefix) - 2 )
	return "Every subnet has %d usable IP addresses" %us

def my_print():	
	if prefix < 1 or prefix > 31:
		print "Please input correct prefix"
		exit(1)
	if len(ipsplit()) == 4:
		if 0 <= int(ipsplit()[1]) < 256 and 0 <= int(ipsplit()[2]) < 256 and           0 <= int(ipsplit()[3]) < 256 and 0 <= int(ipsplit()[0]) < 256: 
				print	subnet ()
				print	netip()
				print	hostmin()
				print	hostmax()
				print	brodcast()
				print	us()
		else:
			print "Please input correct ip" 
			exit (1)
	else :
		print "Please input correct ip" 
		exit(1)

def main():
	my_print()

if __name__ == '__main__':
	main()		

# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4 filetype=py            thon
