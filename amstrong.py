g=int(input('enter the no: '))
def is_armstrong_number(num):
    digits = list(map(int, str(num)))
    return num == sum([d**len(digits) for d in digits])

print(f"Is {g} an Armstrong Number?", is_armstrong_number(g))