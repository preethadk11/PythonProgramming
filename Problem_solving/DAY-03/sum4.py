integer = input("Enter two integer: ")
dividend,divisor=map(int,integer.split(","))
print(f'Quotient:{(dividend/divisor):.2f}\nRemainder:{dividend%divisor}')