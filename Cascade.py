#Cascade:

def inv(n):
    bef(n)
    print(n)
    aft(n)

 
def things(n, f, g):
    if (n >= 10):
        f(n//10)
        g(n//10)


bef = lambda n : things(n, bef, print)
aft = lambda n : things(n, print, aft)

print("Cascade")
inv(123456)


