def compooundinterest(principal, rate, time):
    amount = principal *(pow((1+rate/100),time))
    ci = amount - principal
    print("Compound interet is", ci)

compooundinterest(10000, 10.25, 5)