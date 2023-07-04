x = [1, 2, 3, 4, 5, 6, 7]

print(x[2])
print(len(x))
y = len(x)

d = y + x[2]
print(d)

print(x[1:4])

for i in x:
    print(i)

country = ("Italy", "Ukraine", "USA", "Poland", "China")
print(country)
select_country = input("Please select country: ")
print(country.index(select_country))
sel_country = country.index(select_country)
if sel_country == 2:
    print("You Pendos! ))))))))))")
elif sel_country == 1:
    print("You Coool!!!")
else:
    print("Nu take...")