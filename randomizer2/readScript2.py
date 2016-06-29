import subprocess
import sys

inputFile1 = 'randomScriptAX.py'
inputFile2 = 'randomScriptBY.py'
inputFile3 = 'randomScriptCZ.py'

try:
	response = subprocess.Popen(['python', inputFile1], stdout=subprocess.PIPE)
	output = response.stdout.read(1)
	response.kill()
except KeyboardInterrupt:
	raise Exception("Keyboard Interrupt Occurred. Application has stopped.")
except:
	print "Unable to open %s." % inputFile1
	sys.exit(11)

if output == 'A':
	try:
		counter1 = 0
		falseOut = 'Xs'
		while True:
			response2 = subprocess.Popen(['python', inputFile2], stdout=subprocess.PIPE)
			output2 = response2.stdout.read(1)
			response2.kill()
			if output2 == 'B':
				break
			else:
				counter1 = counter1 + 1
	except:
		print "Unable to open %s." % inputFile2
		sys.exit(11)

elif output == 'X':
	try:
		counter1 = 0
		falseOut = 'Bs'
		while True:
			response2 = subprocess.Popen(['python', inputFile2], stdout = subprocess.PIPE)
			output2 = response2.stdout.read(1)
			response2.kill()
			if output2 == 'Y':
				break
			else:
				counter1 = counter1 + 1
	except:
		print "Unable to open %s." % inputFile2
		sys.exit(12)

if output2 == 'B':
	try:
		counter2 = 0
		falseOut2 = 'Zs'
		while True:
			response3 = subprocess.Popen(['python', inputFile3], stdout=subprocess.PIPE)
			output3 = response3.stdout.read(1)
			response3.kill()
			if output3 == 'C':
				break
			else:
				counter2 = counter2 + 1
	except:
		print "Unable to open %s." % inputFile3
		sys.exit(13)
elif output2 == 'Y':
	try:
		counter2 = 0
		falseOut2 = 'Cs'
		while True:
			response3 = subprocess.Popen(['python', inputFile3], stdout=subprocess.PIPE)
			output3 = response3.stdout.read(1)
			response3.kill()
			if output3 == 'Z':
				break
			else:
				counter2 = counter2 + 1
	except:
		print "Unable to open %s." % inputFile3
		sys.exit(13)

print output, "\n", output2, "\n", output3
print "I got", counter1, falseOut, "before I got a", output2
print "I got", counter2, falseOut2, "before I got a", output3
