import random, os, time, datetime

starttime = time.time()
heads = 0
tails = 0
flipped = 0
i = 0

print("The following is a program that simulates a coin flip a certain amount of times, and displays the results.")
repeat = float(input("Enter the amount of times you would like the coin to be flipped: "))
logfileyesno = input("Would you like to save a logfile? Y/N: ")
print()
if logfileyesno.lower() == "y":
	logfilename = input("Log file filename: ")
else:
	logfilename = ("unused.")
outputyesno = input("Would you like to output the result of each toss? Y/N: ")

while i < repeat:
	flip = random.randrange(2)
	flipped = flipped+1
	i=i+1
	if flip == 0:
		heads = heads+1
	else:
		tails = tails+1
	if outputyesno.lower() == "y":
		print(flip, end=" ")
tailspercent = (100/repeat)*tails
headspercent = (100/repeat)*heads
if tails > heads:
	difference = tails - heads
elif heads > tails:
	difference = heads - tails
else:
	difference = 0

elapsedtime = str(datetime.timedelta(seconds=round(time.time()-starttime,2)))
elapsedtime = elapsedtime[:-4]

print()
print()
print("Flipped a coin", repeat, "times.")
print("Total execution time:", elapsedtime)
print("Tails was flipped", tails, "times, or", tailspercent, "% of the time.")
print("Tails was flipped", heads, "times, or", headspercent, "% of the time.")
print("The difference between the two was", difference, ".")

if logfileyesno.lower() == "y":
	logfile = open(os.getcwd()+'/'+logfilename, 'w')
	logfile.write("Flipped a coin " + str(repeat) + " times.\n")
	logfile.write("Total execution time: " + str(elapsedtime) + "\n")
	logfile.write("Tails was flipped " + str(tails) + " times, or " + str(tailspercent) + "% of the time.\n")
	logfile.write("Heads was flipped " + str(heads) + " times, or " + str(headspercent) + "% of the time.\n")
	logfile.write("The difference between the two was " + str(difference) + ".\n")
	logfile.close()
	print("A logfile was published to ", os.getcwd()+'/'+logfilename)
else:
	print("The logfile function was", logfilename)