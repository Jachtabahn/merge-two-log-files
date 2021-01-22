import os

first_log_path = "/home/dimitri/Documents/log/ubuntu.md"
second_log_path = "/home/dimitri/Documents/log/windows.md"

first_log_file = open(first_log_path)
second_log_file = open(second_log_path)

for first_line, second_line in zip(first_log_file, second_log_file):
	if first_line == second_line:
		print(first_line, end='')
	else:
		break

first_mtime = os.stat(first_log_path).st_mtime
second_mtime = os.stat(second_log_path).st_mtime

if first_mtime <= second_mtime:
	print(first_line, end='')
	for first_line in first_log_file:
		print(first_line, end='')

	print()
	print(second_line, end='')
	for second_line in second_log_file:
		print(second_line, end='')
else:
	print(second_line, end='')
	for second_line in second_log_file:
		print(second_line, end='')

	print()
	print(first_line, end='')
	for first_line in first_log_file:
		print(first_line, end='')
