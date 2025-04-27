L = [1,2,3,4,5]
L2 = [7,8,9]
L.append(6)
L.clear()
L.extend(L2)

LS = ["Hola", "mundo", "mundo"]
print(LS.count("mundo"))
print(LS.index("Hola"))

LS.insert(-1,20)

LS.pop()
LS.pop(0)
LS.remove("mundo")

LS.reverse()

L.sort()