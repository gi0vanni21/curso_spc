ladoa = int(input("digite o valor A:"))
ladob = int(input("digite o valor B:"))
ladoc = int(input("digite o valor C:"))

if ladoa == ladob == ladoc:
    print("equilátero")
elif ladoa != ladob and ladob != ladoc and ladoa != ladoc:
    print("escaleno")
if not (ladoa == ladob == ladoc) and (ladoa == ladob or ladob == ladoc or ladoa == ladoc):
    print("isóceles")