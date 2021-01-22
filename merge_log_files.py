import argparse
import os

def concatenate_lines(earlier_line, earlier_log_file, later_line, later_log_file):
	print(earlier_line, end='')
	for first_line in earlier_log_file:
		print(first_line, end='')

	print()
	print(later_line, end='')
	for second_line in later_log_file:
		print(second_line, end='')

# Parse the two input paths to the two log files.
parser = argparse.ArgumentParser(description='Merge two log files.')
parser.add_argument('first_log_path', type=str, help='the path of the first log file to merge')
parser.add_argument('second_log_path', type=str, help='the path of the second log file to merge')
args = parser.parse_args()

first_log_file = open(args.first_log_path)
second_log_file = open(args.second_log_path)

for first_line, second_line in zip(first_log_file, second_log_file):
	if first_line == second_line:
		print(first_line, end='')
	else:
		break

first_mtime = os.stat(args.first_log_path).st_mtime
second_mtime = os.stat(args.second_log_path).st_mtime

if first_mtime <= second_mtime:
	concatenate_lines(first_line, first_log_file, second_line, second_log_file)
else:
	concatenate_lines(second_line, second_log_file, first_line, first_log_file)
