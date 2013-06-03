def optimusPrime():

  my_list = [1,2]
	my_primes = []

	prime_count = 0

	while prime_count < 10:
		last_num = my_list[-1]
		my_list.append(last_num + 1)

		for i in my_list:
			divisibles = 0
			if last_num % i == 0:
				divisibles += 1
				if divisibles < 3:
					prime_count = prime_count + 1
					my_primes.append(i)

	print my_list
	print my_primes

optimusPrime()
