def factorial(n):
	 i = 1
	 while n > 1:
		 i = i * n
		 n = n - 1
	 print i

def evenchecker(n):
    e = n % 2
    if (e == 1):
        print "odd"
    else:
        print "even"


def pyg(word):
	new_word = word[1:len(word)] + word[0] + 'ay'
	return new_word

def prime_checker(number):
	x = 2
	check = True
	if type(number) == int:
		while number > x and check == True:
			if number % x == 0:
				check = False
				return 'your number is not prime'
			else:
				x += 1
	if check == True:
		return "your number is prime"

def sqare(number):
    return number**2

def fibonacci_list(number):
	fibonacci_list = []
	if number < -1:
		latest = "Illegitimate number. \
		please enter a positive integer"
	elif number == -1:
		fibonacci_list.append(0)
	elif number == 0:
		fibonacci_list.append(0)
		fibonacci_list.append(1)
	else:
		fibonacci_list.append(0)
		fibonacci_list.append(1)
		second_latest = 0
		latest = 1
		for i in range(number):
			temp = latest
			latest += second_latest
			second_latest = temp
			fibonacci_list.append(latest)
	return fibonacci_list