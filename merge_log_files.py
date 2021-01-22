

first_log_path = "/home/dimitri/Documents/log/ubuntu.md"
second_log_path = "/home/dimitri/Documents/log/windows.md"

first_log_file = open(first_log_path)
second_log_file = open(second_log_path)

for line_number, (first_line, second_line) in enumerate(zip(first_log_file, second_log_file)):
	if first_line != second_line:
		print(line_number, first_line, second_line)
		break
