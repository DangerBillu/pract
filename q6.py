def srch():
    stack = []
    with open("rain.txt", "r") as f:
        s = f.read()
    d = s.split()
    for i in range(1, len(d), 2):
        stack.append(float(d[i]))
    stack.sort()
    q = stack.pop()
    for i in range(1, len(d), 2):
        if float(d[i]) == q:
            print("The town with the highest rainfall is", d[i-1], "with", q, "mm of rain.")

srch()

def Lessrain():
    f= open("rain.txt", "r")
    s = f.read()
    d = s.split()
    less_rain = []
    for i in range(0, len(d), 2):
        town = d[i]
        rainfall = float(d[i+1])
        if rainfall < 34:
            less_rain.append(f"{town} {rainfall}")
    print(less_rain)
    f = open("lessrain.txt", "w")
    for record in less_rain:
        f.write(record + "\n")

Lessrain()