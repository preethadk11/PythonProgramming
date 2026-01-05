data={'person':{'name':'alice','age':30}}
print(f'alice age is {data['person']['age']}')
data['person']['profession']='doctor'
print(data)
data['person'].pop('name')
print(data)