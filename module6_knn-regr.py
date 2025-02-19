import numpy as np 

class knn_reg:
	def __init__(self, N):
		self.arrays = np.empty((N, 2))

	def append_point_pair(self, x, y, index):
		self.arrays[index] = [x, y]

	def calculate_output_Y(self, X, k, N):
		if k <= N:
			x_distances = np.abs(self.arrays[:, 0] - X)
			k_nearest_neighbors_indices = np.argsort(x_distances)[:k]
			Y = np.mean(self.arrays[k_nearest_neighbors_indices, 1])
			return "output Y: " + str(Y)
		else: 
			return "error, k should be less than or equal to N"


def main():
	user_input_N = int(input("Enter a positive integer N for number of points: "))
	user_input_k = int(input("Enter a positive integer k for the number of nearest neighbors: "))

	knn_reg_ex = knn_reg(user_input_N)

	for i in range(user_input_N):
		print("\n")
		print("Enter for the " + str(i+1) + " point pair: ")
		user_input_point_pair_x = float(input("Enter x coordinate (press Enter after the number):\n"))
		user_input_point_pair_y = float(input("Enter y coordinate (press Enter after the number):\n"))
		knn_reg_ex.append_point_pair(user_input_point_pair_x, user_input_point_pair_y, i)

	user_input_X = float(input("Enter input X to obtain result Y of k-nn regression: "))

	output_Y = knn_reg_ex.calculate_output_Y(user_input_X, user_input_k, user_input_N)

	print(output_Y)


if __name__ == "__main__":
    main()