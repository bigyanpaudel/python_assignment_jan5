new_list=[x for x in range(0,100)
     if all(x % y != 0 for y in range(2, x))]
print(new_list)


f = open('prime_number', 'w')
s = str(new_list)
f.write(s)
f.close()

with open('prime_num', 'w') as fp:
    fp.write(str(new_list))