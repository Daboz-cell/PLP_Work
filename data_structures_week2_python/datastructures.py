my_list=[]

my_list.append('10')
my_list.append('20')
my_list.append('30')
my_list.append('40')
print(my_list)

my_list[1]='15'
print(my_list)

a=['50','60','70']
my_list.extend(a)
print(my_list)

my_list.pop(-1)
print(my_list)

my_list.sort()
print(my_list)

x=my_list.index('30')
print(x)
x=my_list[2]
print(x)