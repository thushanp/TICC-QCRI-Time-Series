from TICC_solver import TICC
import numpy as np
import sys

if __name__ == '__main__':
	fname = "Week4_Mixed[4]_Freq_Wave_Final_Frequency1.csv"
	biclist = []



	
	numclust = 5
	lambvals = 1e-2
	betavals = 150

	# maxiters 1k
	# window size 1

	try:
		ticc = TICC(window_size=1, number_of_clusters=numclust, lambda_parameter=lambvals, beta=betavals, maxIters=1000, threshold=2e-5, 
			write_out_file=False, prefix_string="output_folder/", num_proc=1)

		(cluster_assignment, cluster_MRFs, bic) = ticc.fit(input_file=fname)
		print("what?")

		tup = (numclust, lambvals, betavals, bic)

		biclist.append(tup)

	except: 
		tup = "Fail"
		print(tup)



	# print("what")
	# for numclust in range(3, 10, 1):
	# 	print(fname)
	# 	print("hm")
	# 	# for lambvals in np.linspace(5e-2, 9e-2, 4):
	# 	# 	print("lambs")
	# 	for betavals in range(0, 300, 50):
	# 		try:
	# 			ticc = TICC(window_size=1, number_of_clusters=numclust, lambda_parameter=lambvals, beta=betavals, maxIters=100, threshold=2e-5,
	#        		write_out_file=False, prefix_string="output_folder/", num_proc=1)

	# 			(cluster_assignment, cluster_MRFs, bic) = ticc.fit(input_file=fname)
	# 			print("what?")

	# 			tup = (numclust, lambvals, betavals, bic)

	# 			biclist.append(tup)

	# 			print(tup)

	# 		except:
	# 			print("fail!!!")

	# ticc = TICC(window_size=1, number_of_clusters=8, lambda_parameter=11e-2, beta=600, maxIters=100, threshold=2e-5,
	#         write_out_file=False, prefix_string="output_folder/", num_proc=1)
	# (cluster_assignment, cluster_MRFs, bic) = ticc.fit(input_file=fname)

	np.savetxt('Results.txt', cluster_assignment, fmt='%d', delimiter=',')

	# try:
	# 	print(biclist)
	# except:
	# 	print(tup)
	# np.savetxt('Results2.txt', biclist)

# 7871.73326102 for 8 clusters, 600 beta, lambda param 11e-2, window size 1
# 8029.04661779 for 8 clusters, 400 beta, lambda param 11e-2, window size 1
# 8203.33879978 for 8 clusters, 600 beta, lambda param 10e-2, window size 1
# 184342.471344 for 8 clusters, 600 beta, lambda param 11e-2, window size 5


# ranges: num clusters from 3-15, lambda from 5-14e-2, beta 100 to 1000
# clust 3-10, lambda 5-9, beta 100-500


# BIC Value univariate data: [(4, 0.05, 100, 211.81665000017404)]
# 1st freq data [(4, 0.05, 100, 219.52430593534794)]
# 2nd freq data [(4, 0.05, 100, 187.91306822155377)]


# new params 04 june 18:
# lambda 0.01
# beta 0
# window size 3
