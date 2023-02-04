from cmath import phase
z = complex(input())
x = z.real
y = z.imag
print(abs(complex(x, y)))
print(phase(complex(x, y)))