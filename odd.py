def odd_or_even(n):
    if n % 2 == 0:
        return"even"
    else:
        return"odd"
    num = int(input("enter a number"))
    print(odd_or_even(num))