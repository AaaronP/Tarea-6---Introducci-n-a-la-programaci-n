# {3,2,6,2} => 3x^3 + 2x^2 + 6x + 2
def factores(coe, const):
    cerosCoe = []
    cerosConst = []

    for i in range(1, coe + 1):
        if coe % i == 0:
            cerosCoe += i
            cerosCoe += -i
    for i in range(1, const + 1):
        if const % i == 0:
            cerosConst += i
            cerosConst += -i

    print(cerosCoe, cerosConst)

    return (cerosCoe, cerosConst)


def polinomio(A):
    cCoe, cConst = factores(A[0], A[-1])

    for x in range(5):
        print(3 * (x)**3 + 2 * (x)**2 + 6 * (x) + 2)



polinomio([3, 2, 6, 2])


def sol_polinomio(A):
    pass
