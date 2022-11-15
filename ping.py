#import beepy as beep
import os
import platform    # For getting the operating system name
import subprocess  # For executing a shell command

def check_ping(site):
    hostname = site
    response = os.system("ping -c 1 " + hostname+ " -t")
    # and then check the response...
    if response == 0:
        pingstatus = "Network Active"
    else:
        pingstatus = "Network Error"
    return pingstatus



def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    #param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', '-c', '1', host,'-t']

    return subprocess.call(command) == 0
if __name__ == '__main__':
    ping("google.com")