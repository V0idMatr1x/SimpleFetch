import platform
from pyfiglet import Figlet
from simple_chalk import chalk, green

# Banner
f = Figlet(font='slant')
print(f.renderText('SimpleFetch'))

process = [
    " [ OS ]: ",
    " [ Architecture ]: ",
    " [ Kernel ]: ",
    " [ Host ]: "
]

# System
p_sys = process[0] + str(platform.system())
print(chalk.green.bold(p_sys))

# Release
p_rel = process[2] + str(platform.release())
print(chalk.green.bold(p_rel))

# Node
p_node = process[3] + str(platform.node())
print(chalk.green.bold(p_node))

# Architecture
p_arch = process[1] + str(platform.architecture()) + " " + str(platform.machine())
print(chalk.green.bold(p_arch))


