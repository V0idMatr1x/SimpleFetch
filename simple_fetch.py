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

i_req()

import psutil
import cpuinfo
from pyfiglet import Figlet
from simple_chalk import chalk, green

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

def fetch_CPU_info(brand, cores):
    
    print(chalk.bold.green(process[4] + brand + process[3] + str(cores)))

fetch_CPU_info(
    cpuinfo.get_cpu_info()['brand_raw'], 
    psutil.cpu_count(logical=True)
)

# GPU Info
# Todo: Solve GPU info [ Solved: tmp, Experimental ]. 
# Todo make amd compatible, make a better solution for quering GPU
def fetch_GPU_info(grep_for_gpu): 
    proc = subprocess.Popen(
    [grep_for_gpu], 
    stdout=subprocess.PIPE, shell=True
    )
    
    (out, err) = proc.communicate()
    out = out.decode("utf-8")
    
    GPU_data = str(out)
    # split the string based on the position of the second colon
    split_data = GPU_data.split(":", 2)
    # get last item and get rid of whitespaces
    GPU_model = process[5] + split_data[len(split_data)-1].strip()
    print(chalk.green.bold(GPU_model))

fetch_GPU_info("lspci | grep -i --color ''01:00.0")

# Architecture
p_arch = process[6] + str(platform.architecture()) + " " + str(platform.machine())
print(chalk.green.bold(p_arch))
