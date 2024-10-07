# Ex-1
def emp(name,age,address,contac_no,gender):
    print(f'name = {name}')
    print(f'age = {age}')
    print(f'address = {address}')
    print(f'contac_no = {contac_no}')
    print(f'gender = {gender}')
    return{'name': name,'age':age,'address': address,'contac_no': contac_no,'gender':gender}

emp1= emp('emp1',24,'address1', 1254698, 'Female')
print(f'emp1 = {emp1}')


# Ex-2

def find_maximum(a,b,c):
    return max(a,b,c)

max_value = find_maximum(9,2,26)
print(max_value)

max_value = find_maximum(9,2,26)
print(f'this is inside function')

print(max_value)