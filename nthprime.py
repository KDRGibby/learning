def optimusPrime():

	my_list = [1,2]
	my_primes = []

	prime_count = 0

	# this is supposed to add numbers to my_list until the prime count reaches x numbers.
	while prime_count < 10:
		last_num = my_list[-1]
		my_list.append(last_num + 1)

		#here we check to see if a number in my_list is a prime
		for i in my_list:
			#divisibles counts how many numbers can be evenly divided into x. Primes are only divisible by 2 numbers, itself and 1.
			divisibles = 0
			if last_num % i == 0:
				divisibles += 1
				if divisibles < 3:
					#at this point we should have found a prime and thus we are adding to the prime count and appending the number to my_primes list.
					prime_count = prime_count + 1
					my_primes.append(last_num)

	print my_list
	print my_primes

optimusPrime()

