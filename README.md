# Cryptography
List of algorithms analysed during the 'Cryptography' course from the M.Sc. in ICT Engineering, Università degli Studi di Padova, a.y. 2020/2021.

## Primality test algorithms
**Goal:** state whether a given natural number is prime or composite.

**Content:**
 - [Miller-Rabin's test]()
 - [Akrawal-Kayal-Saxena (AKS) algorithm]()
 - [Eratosthenes' sieve]()

## Factoring algorithms
**Goal:** find (at least) one divisor of a given natural number.

**Content:**
 - [Fermat factoring algorithm](https://github.com/albertomolon/cryptography/blob/master/2-factoring-algorithms/fermat-factoring.py)
 - [Pollard's rho method with Floyd iterations](https://github.com/albertomolon/cryptography/blob/master/2-factoring-algorithms/pollard-rho-floyd-iterations.py)
 - [Trial-division method](https://github.com/albertomolon/cryptography/blob/master/2-factoring-algorithms/trial-division-method.py)

### Prerequisites
It is used [Python 3.x](https://www.python.org/downloads/). Then you also need the following modules:
- ``` mpmath ``` => ``` pip install mpmath ```
- ``` gmpy2 ``` => ``` pip install gmpy2 ```
