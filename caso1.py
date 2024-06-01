from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    net = Mininet( topo=None,
        build=False,
        ipBase='10.0.0.0/8'
        )

    info( '*** Adding controller\n' )
    info( '*** Add switches\n')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch, failMode='standalone')
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch, failMode='standalone')
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch, failMode='standalone')
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch, failMode='standalone')
    s5 = net.addSwitch('s5', cls=OVSKernelSwitch, failMode='standalone')
    s6 = net.addSwitch('s6', cls=OVSKernelSwitch, failMode='standalone')
    s7 = net.addSwitch('s7', cls=OVSKernelSwitch, failMode='standalone')
    s8 = net.addSwitch('s8', cls=OVSKernelSwitch, failMode='standalone')
    s9 = net.addSwitch('s9', cls=OVSKernelSwitch, failMode='standalone')
    s10 = net.addSwitch('s10', cls=OVSKernelSwitch, failMode='standalone')
    s11 = net.addSwitch('s11', cls=OVSKernelSwitch, failMode='standalone')
    s12 = net.addSwitch('s12', cls=OVSKernelSwitch, failMode='standalone')

    r0 = net.addHost('r0', cls=Node, ip='192.168.100.6/29')
    r0.cmd('sysctl -w net.ipv4.ip_forward=1')

    r1 = net.addHost('r1', cls=Node, ip='192.168.100.1/29')
    r1.cmd('sysctl -w net.ipv4.ip_forward=1')
    r2 = net.addHost('r2', cls=Node, ip='192.168.100.9/29')
    r2.cmd('sysctl -w net.ipv4.ip_forward=1')
    r3 = net.addHost('r3', cls=Node, ip='192.168.100.17/29')
    r3.cmd('sysctl -w net.ipv4.ip_forward=1')
    r4 = net.addHost('r4', cls=Node, ip='192.168.100.25/29')
    r4.cmd('sysctl -w net.ipv4.ip_forward=1')
    r5 = net.addHost('r5', cls=Node, ip='192.168.100.33/29')
    r5.cmd('sysctl -w net.ipv4.ip_forward=1')
    r6 = net.addHost('r6', cls=Node, ip='192.168.100.41/29')
    r6.cmd('sysctl -w net.ipv4.ip_forward=1')
    

    info( '*** Add hosts\n')
    h1 = net.addHost('h1', cls=Host, ip='10.0.1.254', defaultRoute='10.0.1.1')
    h2 = net.addHost('h2', cls=Host, ip='10.0.2.254', defaultRoute='10.0.2.1')
    h3 = net.addHost('h3', cls=Host, ip='10.0.3.254', defaultRoute='10.0.3.1')
    h4 = net.addHost('h4', cls=Host, ip='10.0.4.254', defaultRoute='10.0.4.1')
    h5 = net.addHost('h5', cls=Host, ip='10.0.5.254', defaultRoute='10.0.5.1')
    h6 = net.addHost('h6', cls=Host, ip='10.0.6.254', defaultRoute='10.0.6.1')

    info( '*** Add links\n')
    
    net.addLink(s3, r0, intfName1="r0-eth1", params2={'ip':'192.168.100.6/29'})
    net.addLink(s4, r0, intfName1="r0-eth2", params2={'ip':'192.168.100.14/29'})
    net.addLink(s7, r0, intfName1="r0-eth3", params2={'ip':'192.168.100.22/29'})
    net.addLink(s8, r0, intfName1="r0-eth4", params2={'ip':'192.168.100.30/29'})
    net.addLink(s11, r0, intfName1="r0-eth5", params2={'ip':'192.168.100.38/29'})
    net.addLink(s12, r0, intfName1="r0-eth6", params2={'ip':'192.168.100.46/29'})

    net.addLink(s3, r1, intfName1='s3-eth2', intfName2='r1-eth1', params2={'ip':'192.168.100.1/29'})
    net.addLink(s4, r2, intfName1='s4-eth2', intfName2='r2-eth1', params2={'ip':'192.168.100.9/29'})
    net.addLink(s7, r3, intfName1='s7-eth2', intfName2='r3-eth1', params2={'ip':'192.168.100.17/29'})
    net.addLink(s8, r4, intfName1='s8-eth2', intfName2='r4-eth1', params2={'ip':'192.168.100.25/29'})
    net.addLink(s11, r5, intfName1='s11-eth2', intfName2='r5-eth1', params2={'ip':'192.168.100.33/29'})
    net.addLink(s12, r6, intfName1='s12-eth2', intfName2='r6-eth1', params2={'ip':'192.168.100.41/29'})
    
    net.addLink(r1, s1, intfName1="r1-eth2", params1={'ip':'10.0.1.1/24'})
    net.addLink(r2, s2, intfName1="r2-eth2", params1={'ip':'10.0.2.1/24'})
    net.addLink(r3, s5, intfName1="r3-eth2", params1={'ip':'10.0.3.1/24'})
    net.addLink(r4, s6, intfName1="r4-eth2", params1={'ip':'10.0.4.1/24'})
    net.addLink(r5, s9, intfName1="r5-eth2", params1={'ip':'10.0.5.1/24'})
    net.addLink(r6, s10, intfName1="r6-eth2", params1={'ip':'10.0.6.1/24'})
    
    net.addLink(h1, s1)
    net.addLink(h2, s2)
    net.addLink(h3, s5)
    net.addLink(h4, s6)
    net.addLink(h5, s9)
    net.addLink(h6, s10)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s1').start([])
    net.get('s2').start([])
    net.get('s3').start([])
    net.get('s4').start([])
    net.get('s5').start([])
    net.get('s6').start([])
    net.get('s7').start([])
    net.get('s8').start([])
    net.get('s9').start([])
    net.get('s10').start([])
    net.get('s11').start([])
    net.get('s12').start([])

    info( '*** Post configure switches and hosts\n')
    r0_cmd = "ip route add 10.0.1.0/24 via 192.168.100.1 && \
              ip route add 10.0.2.0/24 via 192.168.100.9 && \
              ip route add 10.0.3.0/24 via 192.168.100.17 && \
              ip route add 10.0.4.0/24 via 192.168.100.25 && \
              ip route add 10.0.5.0/24 via 192.168.100.33 && \
              ip route add 10.0.6.0/24 via 192.168.100.41"
    
    r0.cmd(r0_cmd)

    h1_cmd = "ip route add default via 10.0.1.1"
    h1.cmd(h1_cmd)
    networks = range(1, 7)
    for nets in networks:
        if nets == 1:
            continue
        r1_cmd = f"ip route add 10.0.{nets}.0/24 via 192.168.100.6" 
        r1.cmd(r1_cmd)
        h1_cmd = f"ip route add 10.0.{nets}.0/24 via 10.0.1.1"
        h1.cmd(h1_cmd)   
    networkswan = range(0,41,8)
    for netwan in networkswan:
        if netwan == 0:
            continue
        r1_cmd = f"ip route add 192.168.100.{netwan}/29 via 192.168.100.6" 
        r1.cmd(r1_cmd)
        h1_cmd = f"ip route add 192.168.100.{netwan}/29 via 10.0.1.1"
        h1.cmd(h1_cmd)

    h2_cmd = "ip route add default via 10.0.2.1"
    h2.cmd(h2_cmd)
    networks = range(1, 7)
    for nets in networks:
        if nets == 2:
            continue
        r2_cmd = f"ip route add 10.0.{nets}.0/24 via 192.168.100.14" 
        r2.cmd(r2_cmd)
        h2_cmd = f"ip route add 10.0.{nets}.0/24 via 10.0.2.1"
        h2.cmd(h2_cmd)   
    networkswan = range(0,41,8)
    for netwan in networkswan:
        if netwan == 8:
            continue
        r2_cmd = f"ip route add 192.168.100.{netwan}/29 via 192.168.100.14" 
        r2.cmd(r2_cmd)
        h2_cmd = f"ip route add 192.168.100.{netwan}/29 via 10.0.2.1"
        h2.cmd(h2_cmd)

    h3_cmd = "ip route add default via 10.0.3.1"
    h3.cmd(h3_cmd)
    networks = range(1, 7)
    for nets in networks:
        if nets == 3:
            continue
        r3_cmd = f"ip route add 10.0.{nets}.0/24 via 192.168.100.22" 
        r3.cmd(r3_cmd)
        h3_cmd = f"ip route add 10.0.{nets}.0/24 via 10.0.3.1"
        h3.cmd(h3_cmd)   
    networkswan = range(0,41,8)
    for netwan in networkswan:
        if netwan == 16:
            continue
        r3_cmd = f"ip route add 192.168.100.{netwan}/29 via 192.168.100.22" 
        r3.cmd(r3_cmd)
        h3_cmd = f"ip route add 192.168.100.{netwan}/29 via 10.0.3.1"
        h3.cmd(h3_cmd)

    h4_cmd = "ip route add default via 10.0.4.1"
    h4.cmd(h4_cmd)
    networks = range(1, 7)
    for nets in networks:
        if nets == 4:
            continue
        r4_cmd = f"ip route add 10.0.{nets}.0/24 via 192.168.100.30" 
        r4.cmd(r4_cmd)
        h4_cmd = f"ip route add 10.0.{nets}.0/24 via 10.0.4.1"
        h4.cmd(h4_cmd)   
    networkswan = range(0,41,8)
    for netwan in networkswan:
        if netwan == 24:
            continue
        r4_cmd = f"ip route add 192.168.100.{netwan}/29 via 192.168.100.30" 
        r4.cmd(r4_cmd)
        h4_cmd = f"ip route add 192.168.100.{netwan}/29 via 10.0.4.1"
        h4.cmd(h4_cmd)

    h5_cmd = "ip route add default via 10.0.5.1"
    h5.cmd(h5_cmd)
    networks = range(1, 7)
    for nets in networks:
        if nets == 5:
            continue
        r5_cmd = f"ip route add 10.0.{nets}.0/24 via 192.168.100.38" 
        r5.cmd(r5_cmd)
        h5_cmd = f"ip route add 10.0.{nets}.0/24 via 10.0.5.1"
        h5.cmd(h5_cmd)   
    networkswan = range(0,41,8)
    for netwan in networkswan:
        if netwan == 32:
            continue
        r5_cmd = f"ip route add 192.168.100.{netwan}/29 via 192.168.100.38" 
        r5.cmd(r5_cmd)
        h5_cmd = f"ip route add 192.168.100.{netwan}/29 via 10.0.5.1"
        h5.cmd(h5_cmd)
        
    h6_cmd = "ip route add default via 10.0.6.1"
    h6.cmd(h6_cmd)
    networks = range(1, 7)
    for nets in networks:
        if nets == 6:
            continue
        r6_cmd = f"ip route add 10.0.{nets}.0/24 via 192.168.100.46" 
        r6.cmd(r6_cmd)
        h6_cmd = f"ip route add 10.0.{nets}.0/24 via 10.0.6.1"
        h6.cmd(h6_cmd)   
    networkswan = range(0,41,8)
    for netwan in networkswan:
        if netwan == 40:
            continue
        r6_cmd = f"ip route add 192.168.100.{netwan}/29 via 192.168.100.46" 
        r6.cmd(r6_cmd)
        h6_cmd = f"ip route add 192.168.100.{netwan}/29 via 10.0.6.1"
        h6.cmd(h6_cmd)
        

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()
