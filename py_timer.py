import sys
import os
import json
import time


def main(argv=None):

	# Read json
	jsonFile = str(argv[0])
	json_data = open(jsonFile).read()
	data = json.loads(json_data)
			
	# Infinite loop, escape with CTRL+C
	while True:
		
		# Lock current local time
		startLocalTime = time.localtime()

		for service in data['services']:
			if str(time.strftime("%A", startLocalTime)).lower() in str(service['weekday']).lower():				
				if str(time.strftime("%H:%M", startLocalTime)) in str(service['time']).lower():
					if 'last_execution' not in service or str(service['last_execution']) != str(time.strftime("%d-%m %H:%M", startLocalTime)):
						
						try:
							os.system(service['executable']);
							service['last_execution'] = str(time.strftime("%d-%m %H:%M", startLocalTime))
						except:
							print "Failed to run service."
					else:
						print "Skipped service",service['name']

		time.sleep(30)

if __name__ == "__main__":
	main(sys.argv[1:])
	
