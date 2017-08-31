r=0
a=[100,60,40,20,10,0]
b=[0.001,0.015,0.03,0.05,0.075,0.1]
i=int(input("inpu12t your earning:"))
for x in range(0,6):
	if i>a[x]:
		r+=(i-a[x])*b[x]
		i=a[x]
else:
	print(r)
	r=0


i=int(input("input again:"))
if i<=10:
	print("bonus is:",0.1*i)
elif i<20:
	print("bonus is:",1+0.075*(i-10))
elif i<40:
	print("bonus is:",1.75+0.05*(i-20))
elif i<60:
	print("bonus is:",2.75+0.03*(i-40))
elif i<100:
	print("bonus is:",3.35+0.015*(i-60))
else:
	print("bonus is:",3.95+0.001*(i-100))


