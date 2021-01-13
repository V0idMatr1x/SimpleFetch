import psutil
import platform
from pyfiglet import Figlet
from simple_chalk import chalk, green
from datetime import datetime

# Banner
f = Figlet(font='slant')
print(f.renderText('SimpleFetch'))

process = [
    " [ OS ]: ",
    " [ Kernel ]: ",
    " [ Host ]: ",
    " [ CPU Cores ]: ",
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

# CPU Cores
cores = str(psutil.cpu_count(logical=True))
cpu_cores = process[3] + f"({cores})"
print(chalk.green.bold(cpu_cores))

# Architecture
p_arch = process[4] + str(platform.architecture()) + " " + str(platform.machine())
print(chalk.green.bold(p_arch))




