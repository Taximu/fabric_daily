import os
from threading import local
import time
import logging

from fabric.api import *
from fabric.operations import reboot
from fabric.contrib.files import append
from fabric.context_managers import shell_env
from fabric.decorators import hosts, parallel, serial

logging.basicConfig(level=logging.ERROR)
para_log = logging.getLogger('paramiko.transport')
para_log.setLevel(logging.ERROR)

def install_packages():
    """Installs extra packages on the system."""
    local('apt-get install -y mc htop vim lynx byobu nethogs', warn=True)
    local('apt-get install -y nload iptraf acpi sl r-base ranger', warn=True)
    local('apt-get install -y mplayer', warn=True)
    local('lm-sensors', warn=True)

def autoremove_packages():
    """Auto removes packages."""
    local('apt-get autoremove -y', warn=True)

def update_system():
    """Update system."""
    local('apt-get -y update', warn=True)
    local('apt-get -y dist-upgrade', warn=True)

def watch_star_wars():
    """Watch Star Wars in ASCII."""
    local('telnet towel.blinkenlights.nl', warn=True)

def configure_net():
    """Configures network interface."""
    local('ifconfig eth0 0.0.0.0', warn=True) #change 0.0.0.0 to your ip_address
    local('route add default gateway 0.0.0.1', warn=True) #change 0.0.0.1 to your default gateway ip_address

def install_wego():
    """Installs weather application."""
    local('apt-get install golang')
    local('mkdir ~/workspace')
    local("echo 'export GOPATH=\"$HOME/workspace\"' >> ~/.bashrc")
    local('source ~/.bashrc')
    local('go get github.com/schachmat/wego')
    local("echo 'export PATH=\"$PATH:$GOPATH/bin\"' >> ~/.bashrc")
    local('source ~/.bashrc')
