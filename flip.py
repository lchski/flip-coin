import random
import os
import time
import datetime
import argparse

start_time = time.time()

heads = 0
tails = 0
flipped = 0
temp_tail_value = 0
temp_head_value = 0
long_tail_value = 0
long_head_value = 0

parser = argparse.ArgumentParser(description="Simulate a coin flip a certain amount of times and display the results.")
parser.add_argument('--amount', nargs=1, help='Number of times to run the simulation. Example usage: --amount 1000')
parser.add_argument('--log', nargs=1, help='Name of logfile. Example usage: --log log.txt')
parser.add_argument('--verbose', action='store_true', help='To show or not to show visual output. Example usage: --verbose')
args = parser.parse_args()

print("\nThe following is a program that simulates a coin flip a certain amount of times, and displays the results.")

def flip(amount, verbose):
	global flipped, tails, heads, temp_tail_value, temp_head_value, long_tail_value, long_head_value

	if verbose: 
		print('')
	for i in range(amount):
		flip_result = random.choice(['head', 'tail'])
		flipped += 1

		if verbose:
			print(flip_result, end=", ")

		if flip_result == 'head':
			heads += 1
			temp_head_value += 1
			if long_tail_value < temp_tail_value:
				long_tail_value = temp_tail_value

			temp_tail_value = 0
		else:
			tails += 1
			temp_tail_value += 1
			if long_head_value < temp_head_value:
				long_head_value = temp_head_value

			temp_head_value = 0
	if verbose: 
		print('')

def output(amount, log):
	tails_percent = (100 / amount) * tails
	heads_percent = (100 / amount) * heads

	difference = tails - heads if tails > heads else heads - tails if heads > tails else 0 #  probably has a better approach to make it cleaner
	elapsed_time = str(datetime.timedelta(seconds=round(time.time() - start_time, 2)))[::-4]

	log_message = f'Flipped a coin {amount} times.\nTotal execution time: {elapsed_time}.\nTails was flipped {tails} times, or {tails_percent}% of the time.\nHeads was flipped {heads} times, or {heads_percent}% of the time.\nThe difference between the two was {difference}.\nThe longest string of tails in a row was: {long_tail_value}.\nThe longest string of heads in a row was: {long_head_value}.'

	print('\n' + log_message)
	if log:
		# Using append (a) instead of write (w), so that we can stack logs together instead of removing the previous logs
		with open(log, 'a') as log_file:
			log_file.write(log_message + '\n\n')
			print("A log file was published to {}".format(os.getcwd()+'\\' + log))

if __name__ == '__main__':
	# Putting the arguments into one line
	amount = int(args.amount[0]) if args.amount else 1
	log = args.log[0] if args.log else None
	verbose = True if args.verbose else False

	flip(amount, verbose)
	output(amount, log)
