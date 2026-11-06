num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

#caso 1
if num1 <= num2 and num1 <= num3:
    print(num1)
    if num2 <= num3:
        print(num2)
        print(num3)
    else: 
        print(num3)
        print(num2)
#caso 2
elif num2 < num1 and num2 < num3:
    print(num2)
    if num1 < num3:
        print(num1)
        print(num3)
    else: 
        print(num3)
        print(num1)
#caso 3
elif num3 < num2 and num3 < num1:
    print(num3)
    if num1 < num2:
        print(num1)
        print(num2)
    else: 
        print(num2)
        print(num1)
#caso 4        
elif num1 == num2 and num1 > num3:
    print(num3)
    print(num1)
    print(num2)

#caso 5
elif num1 == num3 and num3 > num2:
    print(num2)
    print(num3)
    print(num1)
#caso 6
elif num2 == num3 and num3 > num1:
    print(num2)
    print(num3)
    print(num1)
#caso 7
elif num1 == num2 and num1 < num3:
    print(num1)
    print(num2)
    print(num3)

#caso 8
elif num1 == num3 and num3 < num2:
    print(num3)
    print(num1)
    print(num2)
#caso 9
elif num2 == num3 and num3 < num1:
    print(num2)
    print(num3)
    print(num1)
#caso 10
else: 
    print(num1)
    print(num2)
    print(num3)
