import csv
import numpy as np
def load_data(input_path):
	rows = []
	with open(input_path, 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		for row in reader:
			rows.append(row)
	labels = [int(row[1]) for row in rows[1:]]
	rows = [[float(num) for num in row[2:]] for row in rows[1:]]
	return np.array(rows), np.array(labels)