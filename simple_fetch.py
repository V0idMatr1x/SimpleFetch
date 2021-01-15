import os
import platform
import sys
import subprocess
import pkg_resources

# Auto-Installer
def i_req():
    
    required= []
    with open('requirements.txt','r') as f:
        required = [line for line in f.readlines()]
    
    installed = [pkg.key for pkg in pkg_resources.working_set]
    missing = [item for item in required if item not in installed]

    if missing:
        python = sys.executable
        subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

# Possible solution is to os.system(pip check for required deps if found ignore the installation script)

i_req()

import psutil
import cpuinfo
from pyfiglet import Figlet
from simple_chalk import chalk, green
"""
# Todo (IN PROGRESS)
Auto installer needs a medium for detecting if 
dependencies are already present on the users system, 
and if so, ignore the installation message + script
"""



# Banner
f = Figlet(font='slant')
print(f.renderText('SimpleFetch'))

process = [
    " [ OS ]: ",
    " [ Kernel ]: ",
    " [ Host ]: ",
    " [ CPU Cores ]: ",
    " [ CPU Info ]: ",
    " [ GPU Model ]: ",
    " [ Architecture ]: ",
]

# System
p_sys = process[0] + str(platform.system())
print(chalk.green.bold(p_sys))

# Release
p_rel = process[1] + str(platform.release())
print(chalk.green.bold(p_rel))

# Node
p_node = process[2] + str(platform.node())
print(chalk.green.bold(p_node))

def fetch_CPU_info(): # Function: CPU Info
# CPU Cores
    cores = str(psutil.cpu_count(logical=True))
    cpu_cores = process[3] + f"({cores})"
# CPU Model
    cpu_model = cpuinfo.get_cpu_info()['brand_raw']
    return print(chalk.bold.green(process[4] + cpu_model + str(cpu_cores)))
fetch_CPU_info()

# GPU Info
# Todo: Solve GPU info [ Solved: tmp, Experimental ]. 
# Todo: /Brain Storm/ Simple, Creative new features.
# Todo: Begin testing Experimental GPU features.
# Todo make amd compatible, will require some conditions to coordinate events
def fetch_GPU_info(): # Experiemental Function: temp method for quering GPU
    proc = subprocess.Popen(["lspci | grep -i --color ''01:00.0"], stdout=subprocess.PIPE, shell=True)
    
    (out, err) = proc.communicate()

    out = out.decode("utf-8")
    
    GPU_data = str(out)
    # split the string based on the position of the second colon
    split_data = GPU_data.split(":", 2)
    # get last item and get rid of whitespaces
    GPU_model = process[5] + split_data[len(split_data)-1].strip() 
    return print(chalk.green.bold(GPU_model))
fetch_GPU_info()

# Architecture
p_arch = process[6] + str(platform.architecture()) + " " + str(platform.machine())
print(chalk.green.bold(p_arch))

