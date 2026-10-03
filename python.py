#for i in range(1,7):
#    for j in range(1,7):
#
#        if i==1 or j==1 or j==7 or i==7:
#            print
#        else:
#            print(" ",end=)
#        print()
while True:
    nomre = float(input("nomre bezan:"))

    if nomre>=20:
        print("dorosr bezan dige")
        continue
    if 17<=nomre<18:
        print("A")
    if 18<=nomre<19:
        print("A+")
    if 19<=nomre<20:
        print("A++")

    if 14<=nomre<17:
        print("B")
    if 10<=nomre<14:
        print("C")
    if 0<=nomre<10:
        print("oftadi")

