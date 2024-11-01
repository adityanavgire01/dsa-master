l1 = int(input("enter max num : "))

if l1 <= 1:
    print("max num must be atleast 3  : ", l1)
else:
    for i in range(l1):
        if i%2 != 0:
            print('odd list ->',i)

