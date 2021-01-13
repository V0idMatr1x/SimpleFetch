import psutil
import platform
from pyfiglet import Figlet
from simple_chalk import chalk, green
import cpuinfo

# Banner
f = Figlet(font='slant')
print(f.renderText('SimpleFetch'))

process = [
    " [ OS ]: ",
    " [ Kernel ]: ",
    " [ Host ]: ",
    " [ CPU Info ]: ",
    " [ CPU Cores ]:",
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

# Function: CPU Info
def fetch_cpu_info():
# CPU Cores
    cores = str(psutil.cpu_count(logical=True))
    cpu_cores = process[4] + f"({cores})"
# CPU Model
    cpu_model = cpuinfo.get_cpu_info()['brand_raw']
    return print(chalk.bold.green(process[3] + cpu_model + str(cpu_cores)))
fetch_cpu_info()

# GPU Info


# Architecture
p_arch = process[5] + str(platform.architecture()) + " " + str(platform.machine())
print(chalk.green.bold(p_arch))










