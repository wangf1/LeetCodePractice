# https://leetcode.com/problems/count-primes/submissions/
class Solution:
    # Sieve of Eratosthenes
    def countPrimes(self, n):
        if n < 3:
            return 0
        primes = [1] * n
        primes[0] = primes[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [0] * len(primes[i * i: n: i])
        return sum(primes)


if __name__ == '__main__':
    result = Solution().countPrimes(10)
    print(result)
