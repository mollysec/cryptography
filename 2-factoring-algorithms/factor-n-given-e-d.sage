###############################################################
###############################################################
##### SageMath script for factoring 'N' given 'e' and 'd' #####
###############################################################
###############################################################

# https://www.di-mgt.com.au/rsa_factorize_n.html
# https://stackoverflow.com/questions/65050529/factoring-rsa-primes-p-and-q-given-n-e-and-d-sagemath-implementation-i-am-r

def factor(n, e, d):
    b = e * d - 1
    while (b % 2 == 0):
        b = b /2
    else:
        t = int(b)
    a = 2
    while (a < n):
        x = power_mod(a, t, n) - 1
        d = gcd (x,n)
        a += 1
        if (d != 1) and (d != n):
            p = d
            q = n // d
            print(d)
            print(n // d)
            break
end


N = 11854178668350132536998770600021775412418919136267711466659575504833480429106340292308672916005731985811172925720279068992464220293573546887342858910065901
e_A = 65537
d_A = 2454147980105506786425977989549345389561620074780357800626167210119179432413932079707729534686888191626633148799840568097408265451820012752747703117155329
factor(N, e_A, d_A)
