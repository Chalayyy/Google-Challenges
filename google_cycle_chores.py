# an algorithm that given an integer n in base b, will take the digits
# in ascending and descending order, subtract them, and use that as
# the next id. Will find the length of a loop when ids start repeating
# in a cycle

def solution(n, b):

	# empty list of z values that have gone through the algorithm
	
	id_values = []

	#define the algorithm

	def chores(n, b):

		# this id (z) added to list of ids used
		
		id_values.append(n)
		
		# length of id in base b
		
		k = len(n)

		# id values turned to string and sorted

		pre_y = sorted(n)
		pre_x = pre_y[::-1]

		# x and y turned back to ints, but of base 10 

		x = int("".join(pre_x), b)
		y = int("".join(pre_y), b)

		# z calculated
		
		z = x - y 	

		# z converted to base b

		i = k-1	
		z_b =[]	
		while i >=0:
			exp = b**i 		
			digit = z//exp	
			z_b.append(str(digit))
			z = z - (digit*exp)
			i -= 1
		z = "".join(z_b)

		#leading zeroes added back to z if necessary

		z = str(z).zfill(k)

		# recursive call to find next id

		if z in id_values:	
			loop_size = (len(id_values) - id_values.index(z))
			return loop_size
		else:
			return chores(z,b)
		
	return chores(n,b)
