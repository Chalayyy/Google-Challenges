"""
This code is designed to take a list (size 2-2000) of positive integers l (values 1-999999)
and counts the number of "lucky triples" (li, lj, lk) where li is a factor of lj which is a factor of lk 
where the list indices meet the requirement i < j < k. 
We find the factors (and number of factors) of each value in the list has as we progress through the list
For each factor found, we add the number of factors it has to our number of lucky triples.
For example, suppose we have [1,2,3,4,5,6,7,8,9,10,11,12] and we are on the value 12.
We add the number of non-self factors of 1,2,3,4,& 6 (0+1+1+2+3 = 7) to our lucky triple count
This is because if j is a factor of k, then any factor of j will create a lucky triple with j and k
"""


def solution(l):

	k_factors = [0 for value in l] 	# stores the number of factors for each value
	lucky_triple_count = 0 			# how many lucky triples exist

	for k in range(1,len(l)):		# start at 2nd term since first term can't have any previous factors
		for j in range(0, k):		# look at terms from the first up to k-1 (any term that might be a factor)
			if l[k]%l[j] == 0:		# determine if j is a factor of k
				k_factors[k] +=1	# add 1 to the kth index
				lucky_triple_count += k_factors[j] # count is increased by the number of factors of the factor

	return lucky_triple_count		# return count



