# Fabric script to execute daily tasks

import os
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
    with settings(warn_only=True):
    	local('sudo apt-get install -y python')
    	local('sudo apt-get install -y python-pip')
    	local('sudo pip install typetrainer')
        local('apt-get install -y mc htop vim lynx byobu nethogs')
        local('apt-get install -y nload iptraf acpi sl r-base ranger')
        local('add-apt-repository ppa:webupd8team/sublime-text-2')
        local('apt-get update')
        local('apt-get install -y sublime-text')
        local('add-apt-repository "deb http://archive.canonical.com/ $(lsb_release -sc) partner"')
        local('apt-get update')
        local('apt-get install -y skype')
        local('wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -')
        local("sh -c 'echo \"deb http://dl.google.com/linux/chrome/deb/ stable main\" >> /etc/apt/sources.list.d/google.list'")
        local('apt-get update')
        local('apt-get install -y google-chrome-stable')
        local('wget http://download.teamviewer.com/download/teamviewer_i386.deb')
        local('dpkg -i teamviewer_i386.deb')	
        local('apt-get -f install')
        local('rm -rf teamviewer_i386.deb')
        local('apt-get update -qq')
        local('apt-get install -y mplayer')
        local('lm-sensors')
        local('apt-get install texlive-full')
        local('apt-get install texlive-fonts-recommended latex-beamer texpower texlive-pictures texlive-latex-extra texpower-examples imagemagick')

def autoremove_packages():
    """Auto removes packages."""
    with settings(warn_only=True):
        local('apt-get autoremove -y')

def update_system():
    """Update system."""
    local('apt-get -y update')
    local('apt-get -y dist-upgrade')

def watch_star_wars():
    """Watch Star Wars in ASCII."""
    local('telnet towel.blinkenlights.nl')

def configure_net():
    """Configures network interface."""
    with settings(warn_only=True):
        local('ifconfig eth0 0.0.0.0') #change 0.0.0.0 to your ip_address
	local('route add default gateway 0.0.0.1') #change 0.0.0.1 to your default gateway ip_address

def install_wego():
    """Installs weather application."""
    local('apt-get install golang')
    local('mkdir ~/workspace')
    local("echo 'export GOPATH=\"$HOME/workspace\"' >> ~/.bashrc")
    local('source ~/.bashrc')
    local('go get github.com/schachmat/wego')
    local("echo 'export PATH=\"$PATH:$GOPATH/bin\"' >> ~/.bashrc")
    local('source ~/.bashrc')
