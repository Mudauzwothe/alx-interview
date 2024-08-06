def isWinner(x, nums):
    # Helper function to find all primes up to a certain number n using Sieve of Eratosthenes
    def get_primes(n):
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers
        p = 2
        while p * p <= n:
            if sieve[p]:
                for i in range(p * p, n + 1, p):
                    sieve[i] = False
            p += 1
        return [p for p, is_prime in enumerate(sieve) if is_prime]
    
    # Helper function to determine the winner of the game for a given n
    def determine_winner(n):
        if n < 2:
            return "Ben"  # No primes to pick
        
        primes = get_primes(n)
        remaining = list(range(1, n + 1))
        turn = 0  # Maria starts (0 for Maria, 1 for Ben)
        
        while primes:
            prime = primes[0]
            # Remove prime and its multiples from remaining
            remaining = [num for num in remaining if num % prime != 0]
            # Remove the prime from the list of primes
            primes = [p for p in primes if p != prime]
            # Change turn
            turn = 1 - turn
        
        return "Maria" if turn == 1 else "Ben"
    
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        winner = determine_winner(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

