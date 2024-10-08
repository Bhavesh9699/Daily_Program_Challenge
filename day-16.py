def find_gcd(n, m):
    while m != 0:
        n, m = m, n % m
    return n
def find_lcm(n, m):
    gcd_value = find_gcd(n, m)
    lcm_value = abs(n * m) // gcd_value
    return lcm_value
N = 15
M = 20
lcm = find_lcm(N, M)
print(f"LCM of {N} and {M} is {lcm}")
