import platform
from getpass import getuser
from importlib.metadata import distributions
from itertools import zip_longest

STYLE="\033[1;33m"
RESET="\033[0m"
LOGO=[]
styled_info=[]

def get_header():
	header=STYLE+getuser()+RESET+"@"+STYLE+platform.node()+RESET
	lenght=len(getuser())+len(platform.node())+1
	sep="-"*lenght

	return header, sep

def get_sys_info():
	packages_count=len(list(distributions()))

	info=[]
	info.append(("Python", platform.python_version()))
	info.append(("Interpreter", platform.python_implementation()))
	info.append(("Architecture", platform.architecture()[0]))
	info.append(("Compiler", platform.python_compiler()))
	info.append(("Packages", str(packages_count)+" (pip)"))

	return info

for name, value in get_sys_info():
	styled_info.append(STYLE+name+RESET+": "+value)

with open("logo.txt", "r", encoding="utf-8") as f:
	for line in f:
		LOGO.append(line.rstrip("\n"))
header, sep = get_header()
TEXT=[header,sep]+styled_info
for logo_line, text_line in zip_longest(LOGO, TEXT, fillvalue=""):
	print(logo_line.ljust(25)+"    "+text_line)

#print(*TEXT, sep='\n')
