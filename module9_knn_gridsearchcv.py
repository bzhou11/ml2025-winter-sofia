import numpy as np 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.model_selection import StratifiedKFold


def generate_data_array(N): 
	arrays = np.empty((N, 2))
	for i in range(N): 
		user_input_point_pair_x = float(input("Enter x coordinate (press Enter after the number):\n"))

		user_input_point_pair_y_check = False
		while user_input_point_pair_y_check == False: 
			user_input_point_pair_y = int(input("Enter y coordinate (press Enter after the number):\n"))
			if user_input_point_pair_y >= 0: 
				user_input_point_pair_y_check = True
				break 
			print("The value of y coordinate must be >= 0. ")

		arrays[i] = [user_input_point_pair_x, user_input_point_pair_y]
	return arrays

def main():

	user_input_N_check = False
	while user_input_N_check == False: 
		user_input_N = int(input("Enter a positive integer N for number of points: "))
		if user_input_N >= 2: 
			user_input_N_check = True
			break 
		print("Number of training samples N must be >= 2.")
		

	train_set = generate_data_array(user_input_N)

	user_input_M_check = False

	while user_input_M_check == False: 
		user_input_M = int(input("Enter a positive integer M for number of points: "))
		if user_input_M >= 1: 
			user_input_M_check = True
			break 
		print("Number of testing samples M must be >= 1.")


	test_set = generate_data_array(user_input_M)


	X_train = train_set[:, 0].reshape((user_input_N, 1))
	y_train = train_set[:, 1]
	X_test = test_set[:, 0].reshape((user_input_M, 1))
	y_test = test_set[:, 1]


	knn_pipe = Pipeline([('knn', KNeighborsClassifier())])

	k_neighbor_limit = min(10, user_input_N)


	params = [{'knn__n_neighbors': list(range(1, k_neighbor_limit + 1))}]

	skf = StratifiedKFold(n_splits=2)

	gs_knn = GridSearchCV(knn_pipe, param_grid=params, scoring='accuracy', cv=skf)

	gs_knn.fit(X_train, y_train)

	best_k_from_train = gs_knn.best_params_['knn__n_neighbors']

	if best_k_from_train > user_input_M:
		k_best_val = user_input_M
		print("Best k derived from training set is larger than number of testing samples M, reset best k to M")
	else: 
		k_best_val = best_k_from_train


	best_knn = KNeighborsClassifier(n_neighbors=k_best_val)

	best_knn.fit(X_train, y_train)

	accuracy = accuracy_score(y_test, best_knn.predict(X_test))

	print("Best k: " + str(k_best_val) + ", accuracy score: " + str(accuracy))



if __name__ == "__main__":
    main()