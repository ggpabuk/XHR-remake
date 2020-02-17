import subprocess
import time
import json
import os
import sys

argv = sys.argv
debug = False				# Enable debug by default?

with open('conf.json') as target:
	conf = json.load(target)

proc = conf['process']        # Process name
sleep = conf['time_sleep']    # Delay before next check
help_txt = conf['help_text']  # Help text

# Working with startup arguments
try:
	if argv[1] == "--debug":
		debug = True
	elif argv[1] == "-h" or argv[1] == "--help":
		print(help_txt)
		sys.exit()
except IndexError:
	pass


# Main Anti-Cheat process
sign = subprocess.check_output('listdlls.exe {proc}')
while True:
	sign_new = subprocess.check_output('listdlls.exe {proc}')
	if sign_new != sign:
		os.system("taskkill /f /im {proc}")
		break
	elif sign_new != sign and debug:
		os.system("taskkill /f /im {proc}")
		print("Signatures not match")
		break
	else:
		print("Signatures match")

	time.sleep(sleep)

sys.exit()
