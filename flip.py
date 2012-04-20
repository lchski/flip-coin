import random, os, time, datetime, argparse

starttime = time.time()

heads = 0
tails = 0
flipped = 0
i = 0
tempTailValue = 0
tempHeadValue = 0
longTailValue = 0
longHeadValue = 0

parser = argparse.ArgumentParser(description="Simulate a coin flip a certain amount of times and display the results.")
parser.add_argument('-n', nargs=1)
parser.add_argument('-l', nargs=1)
parser.add_argument('-o', nargs=1)
args = parser.parse_args()

print("The following is a program that simulates a coin flip a certain amount of times, and displays the results.")

if args.n is None:
	repeat = float(input("Enter the amount of times you would like the coin to be flipped: "))
else:
	repeat = float(args.n[0])

if args.l is None:
	logfileyesno = input("Would you like to save a logfile? Y/N: ")
	if logfileyesno.lower() == "y":
		logfilename = input("Log file filename: ")
	else:
		logfilename = ("unused.")
else:
	logfileyesno = "y"
	logfilename = args.l[0]

if args.o is None:
	outputyesno = input("Would you like to visually output the result of each toss? Y/N: ")
else:
	outputyesno = args.o[0]

print()

while i < repeat:
	flip = random.randrange(2)
	flipped = flipped+1
	i=i+1
	if flip == 0:
		heads = heads+1
		tempHeadValue = tempHeadValue+1
		if longTailValue < tempTailValue:
			longTailValue = tempTailValue
			tempTailValue = 0
		else:
			tempTailValue = 0
	else:
		tails = tails+1
		tempTailValue = tempTailValue+1
		if longHeadValue < tempHeadValue:
			longHeadValue = tempHeadValue
			tempHeadValue = 0
		else:
			tempHeadValue = 0
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
seconds = round(time.time()-starttime,2)
estimate = seconds/repeat

print("\n\n")
print("Flipped a coin", repeat, "times.")
print("Total execution time:", elapsedtime)
print("Tails was flipped", tails, "times, or", tailspercent, "% of the time.")
print("Heads was flipped", heads, "times, or", headspercent, "% of the time.")
print("The difference between the two was", difference, ".")
print("The longest string of tails in a row was:", longTailValue)
print("The longest string of heads in a row was:", longHeadValue)
print("The amount of time taken to flip each coin on average was", estimate)

if logfileyesno.lower() == "y":
	logfile = open(os.getcwd()+'/'+logfilename, 'w')
	logfile.write("Flipped a coin " + str(repeat) + " times.\n")
	logfile.write("Total execution time: " + str(elapsedtime) + "\n")
	logfile.write("Tails was flipped " + str(tails) + " times, or " + str(tailspercent) + "% of the time.\n")
	logfile.write("Heads was flipped " + str(heads) + " times, or " + str(headspercent) + "% of the time.\n")
	logfile.write("The difference between the two was " + str(difference) + ".\n")
	logfile.write("The longest string of tails in a row was " + str(longTailValue) + ".\n")
	logfile.write("The longest string of heads in a row was " + str(longHeadValue) + ".\n")
	logfile.close()
	print("A logfile was published to ", os.getcwd()+'/'+logfilename)
else:
	print("The logfile function was", logfilename)