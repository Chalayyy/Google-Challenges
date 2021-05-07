# given 2-10000 "pegs" which are positive integers, find 
# a list of "gears" that will reach each peg and return the size
# of the first gear (as a list representing numerator and 
# denominator)
# We are also given that gear1 is twice the size of gear(n)

# compare each peg to its neighbors
# find the distance between them
# give 2 gear sizes (radius) that combined are smaller than the distance
# make sure gear1 is double gear(n)
#
#
# algebra to find last gear radius
#
# gear1 + gear2 = dis1 -> gear1 = dis1 - gear2
# gear2 + gear3 = dis2 -> gear2 = dis2 - gear3
# ...
# gear(n-1) + gear(n) = dis(n-1) -> gear(n-1) = dis(n-1) - gear(n)
# 
# gear1 = dis1 - (dis2 - gear3) =
# gear1 = dis1 - dis2 + gear3 = 
# gear1 = dis1 - dis2 + (dis3 - gear4)
# gear1 = dis1 - dis2 + dis3 - (dis4 + gear5)
# ...
# 
# 
# odd dis are pos, even dis are neg 
# if n is even, last gear is subtracted
# if n if odd, last gear is added
# 
# n is odd: 2*gear(n) = alt(sum(dis)) + gear(n) ->
# gear(n) = alt(sum(dis))
# 
# n is even = 2*gear(n) = alt(sum(dis)) - gean(n) ->
# 3*gear(n) = alt(sum(dis)) ->
# gear(n) = alt(sum(dis))/3
#
# gear1 = 2*gear(n)
# 
 
def solution(pegs):
	
	from fractions import Fraction
	
	for i in range(0, len(pegs)):
		pegs[i] = float(pegs[i])

	if pegs[1]-pegs[0] == 1:
		# if distance between first two pegs is 1 (ints only)
		# then gear1 must have radius less than one, so n.s.
		return [-1,-1]

	else:
		# create a list of the distances between adj pegs, indexed
		# to the lower-indexed peg
		dis = []
		for i in range(0, len(pegs)-1):
			# there is one more peg than distances between them
			dis.append(pegs[i+1] - pegs[i]) # dis between adj pegs

	for i in range(0, len(dis)):	# make odd distances negative
		if i%2:
			dis[i] *= -1

	
	if len(pegs)%2:		#if n is even or odd to determine equation
		last_gear = sum(dis)
	else:
		last_gear = sum(dis)/3


	gear = []		# list of gear sizes
	gear.append(2*last_gear)		# gear1
	
	for i in range(0, len(dis)):  
		# find all other gears based on previous gear
		gear.append(abs(dis[i]) - gear[i])

	# FOR PYTHON3
	if all(elem > 0 for elem in gear) and gear[-1] == last_gear:
		# check all gears are positive in size and last gear hasn't changed
		sol = gear[0].as_integer_ratio()
		return [sol[0],sol[1]]

	# FOR PYTHON2.7
	#if all(elem > 1 for elem in gear):
	#	sol = Fraction.from_float(gear[0]).limit_denominator()
	#	return sol.numerator, sol.denominator
	else:
		return [-1,-1]
