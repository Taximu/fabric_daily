# 📘 [Fabric](https://www.fabfile.org/) Script for home .deb package management.

A simple Python Fabric script to automate daily system management tasks like package installation, system updates, network configuration, and fun utilities.


## 🔧 Features
- **Install Packages:** Add essential tools like nethogs, ranger and more.
- **Update System:** Perform `apt-get update` and system upgrades.
- **Network Config:** Manage network interface settings.
- **ASCII Star Wars:** Watch Star Wars in ASCII format.
- **Wego Installation:** Install a weather app using Golang.

## 💡 Usage
Run task functions using Fabric CLI:
```bash
fab install_packages
fab update_system
fab watch_star_wars
```

Automated script to perform daily tasks on deb based packages. 
## Setup for development
    cd /root && git clone https://github.com/Taximu/fabric_daily.git && sudo apt-get install -y fabric
## Setup for testing
    cd root/fabric_daily && sudo fab <function_name>
## To see available functions:
    fab --list
