import os
import psutil
import platform
import cpuinfo
from pyfiglet import Figlet
from simple_chalk import chalk, green
import subprocess


# Banner
f = Figlet(font='slant')
print(f.renderText('SimpleFetch'))

process = [
    " [ OS ]: ",
    " [ Kernel ]: ",
    " [ Host ]: ",
    " [ CPU Info ]: ",
    " [ CPU Cores ]:",
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
    cpu_cores = process[4] + f"({cores})"
# CPU Model
    cpu_model = cpuinfo.get_cpu_info()['brand_raw']
    return print(chalk.bold.green(process[3] + cpu_model + str(cpu_cores)))
fetch_CPU_info()

# GPU Info
#Todo: Solve GPU info.
#Todo: /Brain Storm/ Simple, Creative new features.
#Todo: Find out how Neofetch serves GPU info and try to replicate it.

def fetch_GPU_info():
    proc = subprocess.Popen(["lspci | grep -i --color ''01:00.0"], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    print(str(out))

def fetch_GPU_info():



# output grep command
GPU = "01:00.0 VGA compatible controller: NVIDIA Corporation TU106M [GeForce RTX 2070 Mobile] (rev a1)"

# split the string based on the position of the second colon
split_GPU = GPU.split(":",2)
# get last item and get rid of whitespaces
model_gpu = split_GPU[len(split_GPU)-1].strip()

# display it
print(model_gpu)





# Architecture
p_arch = process[5] + str(platform.architecture()) + " " + str(platform.machine())
print(chalk.green.bold(p_arch))


