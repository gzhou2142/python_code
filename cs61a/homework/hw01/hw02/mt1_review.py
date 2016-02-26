def num_divisor(n):
	i, count = 1, 0
	while i <= n:
		if n % i == 0:
			count += 1
		i = i + 1

	return count

print(num_divisor(4))

def sum_divisors(n):
	i, sum_ = 1,0
	while i <= n:
		if n % i ==0:
			sum_ = sum_ + i
		i = i +1

	return sum_

print(sum_divisors(4))

def describe(n):
	i, sum_ = 1, 0
	while i < n:
		if n % i == 0:
			sum_ = sum_ + i
		i += 1

	if sum_ < n:
		return "deficient"
	elif sum_ == n:
		return "perfect"
	else:
		return "abundant"

print(describe(4))