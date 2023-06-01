# l= [“01-Jan-20”, “10-Jun-10”, “15-Dec-22”]
l = ["01-Jan-20","10-Jun-10","15-Dec-22"]
# new = [j for i in l for j in i]
# a = set(new)
# print(a)
a = l[0:1][0]
b = []
for i in a:
    b.append(i)
    

print(b)
b.pop(2)
b.pop(5)
b.insert(7,20)
c = b[0:2]
d = "".join(map(str,c))
print(d)
# https://youtu.be/uZt_All0J4o
# https://youtu.be/uZw7F8l89q0
# https://youtu.be/IykLwH6O-go
# https://youtu.be/FHeqsWWi4us