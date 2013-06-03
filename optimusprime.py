def optimus_prime(x):
  range_check = x + 1
	my_range = range(1,range_check)

	divisibles = 0
	
	for i in my_range:
		if x % i == 0:
			divisibles = divisibles + 1

	if divisibles < 3:
		print "Prime"
	else:
		print "Not Prime"




optimus_prime(3571)
optimus_prime(11)
optimus_prime(4)
optimus_prime(144)
optimus_prime(3572)
optimus_prime(999981)
optimus_prime(999979)
