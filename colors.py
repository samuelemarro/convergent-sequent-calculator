import platform
import subprocess
import sys

import colorama

colorama.init()

def check_cmd():
    return subprocess.check_output('(dir 2>&1 *`|echo CMD);&<# rem #>echo PowerShell', shell=True)

def is_cmd():
    return sys.platform == 'win32' and check_cmd().decode('utf-8').startswith('CMD')

def is_old_windows_cmd():
    return is_cmd() and platform.release() != '10'

class bcolors:
    if is_old_windows_cmd():
        # Disable colors
        HEADER = ''
        OKBLUE = ''
        OKCYAN = ''
        OKGREEN = ''
        WARNING = ''
        FAIL = ''
        ENDC = ''
        BOLD = ''
        UNDERLINE = ''
    else:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKCYAN = '\033[96m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'