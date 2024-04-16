def cientificos(ss, vv):
    masa = []
    for i in range(len(ss)):
        masa.append(int(ss[i]) * int(vv[i]))
    return masa

s = ["1000", "760", "1200"]
v = ["300", "600", "9000"]

print(cientificos(s,v))