import sys

tax_list = [1500, 4500, 9000, 35000, 55000, 80000]
base_list = [0, 105, 555, 1005, 2755, 5505, 13505]
rate_list = [0.03, 0.1, 0.2, 0.25, 0.3, 0.35, 0.45]
try:
	income = int(sys.argv[1])
except Exception:
	print("Parameter Error")
if income > 3500:
	n= income - 3500
	tax_list.append(n)
	tax_list.sort()
	i = tax_list.index(n)
	tax = n * rate_list[i] - base_list[i]
else:
	tax = 0
print(format(tax, ".2f"))


	

