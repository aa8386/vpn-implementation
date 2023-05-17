import pyopenvpn
client_config_file = '/path/to/client/config.ovpn'
client_vpn = pyopenvpn.PyOpenVPN(config_file=client_config_file, verbosity=0)
client_vpn.start()

while True:
    try:
        event = client_vpn.wait_event(100)
        print(event)
    except pyopenvpn.PyOpenVPNException as e:
        print(e)
        break
client_vpn.stop()
