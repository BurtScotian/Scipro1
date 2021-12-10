'''
if f(x) has a root in [a,b]
after n iterations the length of interval is 2**(-n) (b - a)
'''

def bisection(f, a, b, epsilon):
    f_a = f(a)
    if f_a * f(b) > 0:
        return None, 0 # error: f does not change sign in [a,b]

    i = 0
    while b - a > epsilon:
        i = i+1
        m = (a + b)/2
        f_m = f(m)
        if f_a * f_m <= 0:
            b = m # root is in left half
        else:
            a = m # root is in right half
            f_a = f_m
    return m, i


def test_bisection():
    def f(x):
        return 2*x -3

    epsilon = 1e05
    x_expected = 1.5
    x, iter = bisection(f, a=0, b=10, epsilon = 1e-5)
    success = abs(x-x_expected) < epsilon
    assert success, f'found x = {x} != 1.5'

# test function
if __name__ == '__main__':
    test_bisection()


