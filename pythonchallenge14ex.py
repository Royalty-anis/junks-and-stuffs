def rate(x):
    period = 100
    monthly_rate = 0
    over_time = (x - period)* 25
    if period < x:
        monthly_rate = (20 * period) + over_time
    elif period > x:
        monthly_rate = 20 * x
    return monthly_rate
    return over_time

def your_salary():
    name = input("input your name: ")
    period = int(input("amount of periods: "))
    return f"""
Teacher: {name},
periods: {period}
Gross salary: {rate(period)}
"""
print(your_salary())
