import sys
import os
import json
import time
import logging

def main(argv=None):

	# Read json
	jsonFile = str(argv[0])
	jsonData = open(jsonFile).read()
	data = json.loads(jsonData)

	# Set logger
	logging.basicConfig(filename='py_timer.log', filemode='w', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
	logging.info('Scheduler started')

	# Infinite loop, escape with CTRL+C
	while True:
		
		# Lock current local time
		startLocalTime = time.localtime()

		for service in data['services']:
			if str(time.strftime("%A", startLocalTime)).lower() in str(service['weekday']).lower():				
				if str(time.strftime("%H:%M", startLocalTime)) in str(service['time']):
					if 'last_execution' not in service or str(service['last_execution']) != str(time.strftime("%d-%m %H:%M", startLocalTime)):
						
						try:
							logging.info('Start running service %s', service['name'])
							os.system(service['executable']);
							service['last_execution'] = str(time.strftime("%d-%m %H:%M", startLocalTime))
						except:
							logging.error('Cannot execute service % ', service['name'])
		time.sleep(30)

if __name__ == "__main__":
	main(sys.argv[1:])
	
