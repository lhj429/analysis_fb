def squares(n=10):
    #results = []
    for i in range(n+1):
        yield i**2

for x in squares():
    print(x)