import pyopenvpn
server_config_file = '/path/to/server/config.ovpn'
server_vpn = pyopenvpn.PyOpenVPN(config_file=server_config_file, verbosity=0)
server_vpn.start()

while True:
    try:
        event = server_vpn.wait_event(100)
        print(event)
    except pyopenvpn.PyOpenVPNException as e:
        print(e)
        break
server_vpn.stop()
