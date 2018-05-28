from TICC_solver import TICC
import numpy as np
import sys

if __name__ == '__main__':
	fname = "Syn_TimeSeries_Plot.csv"
	biclist = []

	print("what")
	for numclust in range(3, 10, 1):
		print("hm")
		for lambvals in np.linspace(5e-2, 9e-2, 4):
			print("lambs")
			for betavals in range(100, 500, 100):
				
				try:
					ticc = TICC(window_size=1, number_of_clusters=numclust, lambda_parameter=lambvals, beta=betavals, maxIters=100, threshold=2e-5,
		       		write_out_file=False, prefix_string="output_folder/", num_proc=1)

					(cluster_assignment, cluster_MRFs, bic) = ticc.fit(input_file=fname)
					print("what?")

					tup = (numclust, lambvals, betavals, bic)

					biclist.append(tup)

					print(tup)

				except:
					print(tup)

	# ticc = TICC(window_size=1, number_of_clusters=8, lambda_parameter=11e-2, beta=600, maxIters=100, threshold=2e-5,
	#         write_out_file=False, prefix_string="output_folder/", num_proc=1)
	# (cluster_assignment, cluster_MRFs, bic) = ticc.fit(input_file=fname)

	# np.savetxt('Results.txt', cluster_assignment, fmt='%d', delimiter=',')

	np.savetxt('Results2.txt', biclist)

# 7871.73326102 for 8 clusters, 600 beta, lambda param 11e-2, window size 1
# 8029.04661779 for 8 clusters, 400 beta, lambda param 11e-2, window size 1
# 8203.33879978 for 8 clusters, 600 beta, lambda param 10e-2, window size 1
# 184342.471344 for 8 clusters, 600 beta, lambda param 11e-2, window size 5


# ranges: num clusters from 3-15, lambda from 5-14e-2, beta 100 to 1000
# clust 3-10, lambda 5-9, beta 100-500

# (6, 0.080000000000000002, 500, 5399.4858801522178)