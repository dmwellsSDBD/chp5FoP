def funcA(a, b):
    print("Starting funcA")
    print(funcB(a, b))
    print(funcB(b, a))
    print("Ending funcA")
    
def funcB(x, y):
    print("  In funcB")
    return funcC(x) + y

def funcC(val):
    print("   In funcC")
    return 2 * val

funcA(10, 20)
funcA(15, 20)