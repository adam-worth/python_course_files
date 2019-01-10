hrs = input("Enter Hours: ")
pay = input("Enter Pay: ")
h = h = float(hrs)
p = float(pay)
try:
    h = float(hrs)
    p = float(pay)
except:
    print('Error, please enter numeric values')
    quit()




def computepay(hours, pay):
    if hours <= 40:
        pay = hours * pay
    else:
        overtime = hours - 40
        overtime_pay = overtime * pay * 1.5
        pay = pay * 40 + overtime_pay

    return pay

print(computepay(h, p))
