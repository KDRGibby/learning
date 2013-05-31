import random 

# Reverse Calculator Program - the idea is to allow users to enter a problem they need assitance with and have a computer guide them to the correct answer.
print "****************************"
print "Enter your math problem."
var1 = input("Enter your first variable here: ")
operator = raw_input("Enter your operator here: ")
var2 = input("Enter your second variable here: ")
print "****************************"

#these 2 functions visualize the variables so the user can count how many of each are on the screen.
#at some point in the future, I'll need a better way than just counting to help.
def var1_function(var1):
  count = 0
	while count < var1:
		print "[]",
		count = count + 1

def var2_function(var2):
	count = 0
	while count < var2:
		print "X",
		count = count + 1

# operator function checks to see what operator, like + or -, the user wants to use in the math problem and guides them on how to proceed on the math problem.
def operator_function(operator):
	if operator == "+":
		print "Count the []'s and X's and add them together"
	elif operator == "-":
		print "Count the []'s and then subtract the X's"
	elif operator == "/":
		print "Um, I can't do division right now. Sorry, I'm still learning! ^_^"
	elif operator == "*":
		print "Check out the multiplication table below:"
		#for line in range(1,11):
    	#	for table in range(1,11):
        #		print line * table, '\t',
    	#	print 
	else:
		print "I don't understand your operator, try typing it again."
		#return operator


print var1, " ", operator, " ", var2
print "Hmm, so this is your math problem. Let's see if I can help!"
print "****************************"

print var1_function(var1)
print var2_function(var2)
print operator_function(operator)
print " "
print "Do you think you know the answer?"
print " "
answer = input("What is your answer?: ")
print "****************************"

# here we check the users answer against the computer calculated answer
def right_answer(answer):
	if operator == "+":
		right_answer = var1 + var2
		if right_answer == answer:
			print "That's correct! Great job!"
		else:
			print "No, that's not correct. The answer was:"
			print var1 + var2
			print "Let's try another problem!"

	elif operator == "-":
		right_answer = var1 - var2
		if right_answer == answer:
			print "That's correct! Great job!"
		else:
			print "No, that's not correct."
			print var1 - var2
			print "Let's try another problem!"
	elif operator == "*":
		right_answer = var1 * var2
		if right_answer == answer:
			print "That's correct! Great job!"
		else:
			print "No, that's not correct."
			print var1 * var2
			print "Let's try another problem!"
	elif operator == "/":
		right_answer = var1 / var2
		if right_answer == answer:
			print "That's correct! Great job!"
		else:
			print "No, that's not correct."
			print var1 / var2
			print "Let's try another problem!"

print right_answer(answer)
print "Now let's try a new problem."

num_list = []
num_list2 = []

def find_length(n):
	length_of_var = len(str(n))
	return length_of_var


def random_number_generator(n):
	random_number = 0
	while n > random_number:
		num_list.append(random.randint(0,9))
		random_number = random_number + 1
		

def random_number_generator2(n):
	random_number = 0
	while n > random_number:
		num_list2.append(random.randint(0,9))
		random_number = random_number + 1


find_length(var1)
find_length(var2)

random_number_generator(find_length(var1))
random_number_generator2(find_length(var2))
numList = int(''.join(map(str,num_list)))
numList2 = int(''.join(map(str,num_list2)))

print "****************************"
print numList
print operator
print numList2
print "****************************"

answer = input("Think you know the answer? ")

# discovering the right answer to the new random problem
def right_answer_random(answer):
	if operator == "+":
		right_answer = numList + numList2
		if right_answer == answer:
			print "That's correct! Great job!"
		else:
			print "No, that's not correct. The answer was:"
			print numList + numList2
			print "Let's try another problem!"

	elif operator == "-":
		right_answer = numList - numList2
		if right_answer == answer:
			print "That's correct! Great job!"
		else:
			print "No, that's not correct."
			print numList - numList2
			print "Let's try another problem!"
	elif operator == "*":
		right_answer = numList * numList2
		if right_answer == answer:
			print "That's correct! Great job!"
		else:
			print "No, that's not correct."
			print numList * numList2
			print "Let's try another problem!"
	elif operator == "/":
		right_answer = numList / numList2
		if right_answer == answer:
			print "That's correct! Great job!"
		else:
			print "No, that's not correct."
			print numList / numList2
			print "Let's try another problem!"

print right_answer_random(answer)

