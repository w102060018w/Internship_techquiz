###################################################################################
# Pairs: Count the number of pairs from input-list whose difference is K. 
# Input: N integers, and the value K, which 2 <= N <= 10^5 ; 0 < K < 10^9.
# Example : K=5 array=[1, 5, 7, 2, 2, 7] will return 4 (we count each occurrence)
###################################################################################


import sys
import os
import numpy as np
import math
from collections import Counter

def CheckLastIdx(Matrix,idx):
	if math.isnan(Matrix[idx][1]):
		return 1
	elif math.isnan(Matrix[idx][2]):
		return 2
	else:
		print("Index out of bound, something wrong happened in comparison process")


if __name__ == '__main__' :
	# input
	K = 5
	lst = [1, 5, 7, 2, 2, 7]

	# prepare to start finding pairs
	dic_DuplicateN = dict(Counter(lst)) # count the number of duplucates of each elements, and save it into dictionary.
	N = len(lst)
	M = len(set(lst)) # remove duplicate elements.
	Mat = np.nan*np.empty([M,3])
	Mat[:,0] = list(set(lst))

	# Check constraint
	if N < 2 or N > pow(10,5) or K <= 0 or K >= pow(10,9):
		print("The value of N or K does not satisfy with problem settings")
	
	# start finding pairs
	pairN = 0
	for i,ele in enumerate(Mat[:,0]):
		n1 = dic_DuplicateN.get(Mat[i][0]) # get its duplicate amount

		# check already find a pair or not
		exist = 0
		if math.isnan(Mat[i,1]):
			possiblePair1 = ele+K
			possiblePair2 = ele-K
			
		else:
			exist = 1
			dif = Mat[i,1]-ele
			possiblePair = ele+(-dif)

		# only search backward, since we only care about combination instead of permutation
		for j in range(i+1,M):
			if not exist :
				# put pairs into corresponding index
				if Mat[j,0] == possiblePair1 or Mat[j,0] == possiblePair2 :
					Mat[i][1] = Mat[j,0]
					Mat[j][CheckLastIdx(Mat,j)] = ele
					# count pairs N		
					n2 = dic_DuplicateN.get(Mat[i][1])
					pairN += n1*n2
			else:
				if Mat[j,0] == possiblePair :
					Mat[i][2] = Mat[j,0]
					Mat[j][CheckLastIdx(Mat,j)] = ele
					# count pairs N
					n2 = dic_DuplicateN.get(Mat[i][2])
					pairN += n1*n2

# Output
print('pariN = '+str(pairN))



