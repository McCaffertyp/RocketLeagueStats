import sys
import subprocess

try:
    from selenium import webdriver
except ImportError:
    print("Failed to import webdriver from selenium")
    print("Attempting manual install")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip3', 'install', 'selenium'])
    except subprocess.CalledProcessError:
        print("Error running install command `pip3 install selenium`")
finally:
    from selenium import webdriver

from mccaffertyp.rl_stats import RLStats

RLStats(300000).run()