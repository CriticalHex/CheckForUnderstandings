u_in = input(
    "What are your three favorite bands/musicians? Please use this format: a, b, c: "
)
tup = tuple(u_in.split(", "))
print(tup)
print(tup[1])

u_in = input("What are your 5 favorite foods? Please use this format: a, b, c: ")
lis = list(u_in.split(", "))
print(lis)
print(lis[-1])

u_in = input(
    "What are your 6 favorite video game hero/villain pairs? Please use this format: hero, villain; hero villain: "
)
dic = dict()
for pair in u_in.split("; "):
    hero, villain = pair.split(", ")
    dic[hero] = villain
print(dic)
u_in = input("Enter a key from the previous dictionary: ")
print(dic.get(u_in))
