"""Sieve of Eratosthenes

Given a number n, print all primes smaller than or equal to n. It is also given that n is a small number. 

Example: 

    Input : n =10
    Output : 2 3 5 7 

    Input : n = 20 
    Output: 2 3 5 7 11 13 17 19"""

def SieveOfEratosthenes(n):

	prime = [True for i in range(n+1)]
	p = 2

	while (p * p <= n):
		if (prime[p] == True):
			for i in range(p * p, n+1, p):
				prime[i] = False
		p += 1

	for p in range(2, n+1):
		if prime[p]:
			print (p)

