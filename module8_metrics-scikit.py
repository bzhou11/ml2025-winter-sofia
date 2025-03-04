import numpy as np 
from sklearn.metrics import precision_score, recall_score


class precison_recall_compute:
	def __init__(self, N):
		self.arrays = np.empty((N, 2))

	def append_point_pair(self, x, y, index):
		self.arrays[index] = [x, y]

	def calculate_precision_recall(self):

		X_true = self.arrays[:, 0]
		Y_predicted = self.arrays[:, 1]

		output_precision = precision_score(X_true, Y_predicted, zero_division=0)
		output_recall = recall_score(X_true, Y_predicted, zero_division=0)
		return output_precision, output_recall

def main():
	user_input_N = int(input("Enter a positive integer N for number of points: "))
	precison_recall_compute_ex = precison_recall_compute(user_input_N)


	for i in range(user_input_N):
		print("\n")
		print("Enter for the " + str(i+1) + " point pair: ")
		user_input_point_pair_x = int(input("Enter x coordinate (press Enter after the number):\n"))
		user_input_point_pair_y = int(input("Enter y coordinate (press Enter after the number):\n"))
		precison_recall_compute_ex.append_point_pair(user_input_point_pair_x, user_input_point_pair_y, i)

	precison, recall = precison_recall_compute_ex.calculate_precision_recall()

	print("precison: " + str(precison) + "\n" + "recall: " + str(recall))


if __name__ == "__main__":
    main()