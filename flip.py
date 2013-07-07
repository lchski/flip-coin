import random, os, time, datetime, argparse

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

def askHowManyTimesToRepeat():
    timesToRepeat = int(input("Enter the amount of times you would like the coin to be flipped: "))
    return timesToRepeat

def askToLogOrNot():
    logFileYesOrNo = input("Would you like to save a logfile? Y/N: ")
    if logFileYesOrNo.lower() == "y":
        logFileName = input("Log file filename: ")
    else:
        logFileName = "n"
    return logFileName

def askToShowVisualOutput():
    visualOutputYesOrNo = input("Would you like to visually output the result of each toss? Y/N: ").lower()
    return visualOutputYesOrNo

def flip(times):
	global flipped, tails, heads, tempTailValue, tempHeadValue, longTailValue, longHeadValue
	for i in range(times):
		flip = random.randrange(2)
		flipped += 1
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
		if visualOutputYesOrNo == "y":
			print(flip, end=" ")

def outputAnalysis():
	tailspercent = (100/timesToRepeat)*tails
	headspercent = (100/timesToRepeat)*heads
	if tails > heads:
		difference = tails - heads
	elif heads > tails:
	    difference = heads - tails
	else:
	    difference = 0

	elapsedtime = str(datetime.timedelta(seconds=round(time.time()-starttime, 2)))
	elapsedtime = elapsedtime[:-4]

	print("\n\n")
	print("Flipped a coin", timesToRepeat, "times.")
	print("Total execution time:", elapsedtime)
	print("Tails was flipped", tails, "times, or", tailspercent, "% of the time.")
	print("Heads was flipped", heads, "times, or", headspercent, "% of the time.")
	print("The difference between the two was", difference, ".")
	print("The longest string of tails in a row was:", longTailValue)
	print("The longest string of heads in a row was:", longHeadValue)

def outputLogFile():
	if logFileName.lower() != "n":
		logfile = open(os.getcwd()+'/'+logFileName, 'w')
		logfile.write("Flipped a coin " + str(timesToRepeat) + " times.\n")
		logfile.write("Total execution time: " + str(elapsedtime) + "\n")
		logfile.write("Tails was flipped " + str(tails) + " times, or " + str(tailspercent) + "% of the time.\n")
		logfile.write("Heads was flipped " + str(heads) + " times, or " + str(headspercent) + "% of the time.\n")
		logfile.write("The difference between the two was " + str(difference) + ".\n")
		logfile.write("The longest string of tails in a row was " + str(longTailValue) + ".\n")
		logfile.write("The longest string of heads in a row was " + str(longHeadValue) + ".\n")
		logfile.write("The amount of time taken to flip each coin on average was " + str(estimate) + ".\n")
		logfile.close()
		print("A logfile was published to ", os.getcwd()+'/'+logFileName)
	else:
		print("No log created.")

if args.n == None:
    timesToRepeat = askHowManyTimesToRepeat()
else:
    timesToRepeat = int(args.n[0])

if args.l == None:
    logFileName = askToLogOrNot()
elif args.l[0].lower() != "no" or args.l[0].lower() != "n":
    logFileName = args.l[0]
else:
    logFileName = "n"

if args.o == None:
    visualOutputYesOrNo = askToShowVisualOutput()
else:
    visualOutputYesOrNo = args.o[0].lower()

starttime = time.time()
flip(timesToRepeat)
outputAnalysis()
outputLogFile()
