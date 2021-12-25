## Trial-division method
Iterative algorithm that checks at each iteration if $$\inline m$$ divides $$\inline n$$ (up to a given threshold $$\inline T$$). If at some point this is true, that $$\inline m$$ is a divisor of $$\inline n$$.


## Fermat factoring algorithm
It is based on the key fact (by Fermat) that if $$\inline n$$ is odd, then 
$$\inline n = x^2 - y^2 = (x + y) * (x - y)$$
where $$\inline x$$ and $$\inline y$$ are two integer numbers. Obviously, we are looking for (at least) one non-trivial factor, i.e. a factor s.t. $$\inline x - y \neq 1$$ and/or $$\inline x + y \neq n$$.


## Pollard's rho method with Floyd iterations
It is a probabilistic factoring method based on the following idea:
* compute the iterates with the function $$\inline f(x) = x^2 + 1 \\bmod n$)$$;
* randomly choose $$\inline x_0 \\in \\mathbb{Z}$$;
* find a collision on the iterates, i.e. find the two indeces $$\inline (i, j)$$ s.t. $$\inline f^{(i)}(x_0) \\equiv f^{(j)}(x_0) \\bmod n$$;
* one factor of $$\inline n$$ is $\inline d = gcd\\{\\,f^{(i)}(x_0) - f^{(j)}(x_0)\\,,\\, n\\,\\} \\,\\,$ s.t. $\\,\\, 1 < d < n$ (i.e. d is a non-trivial gcd)."