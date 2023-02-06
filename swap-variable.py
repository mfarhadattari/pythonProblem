# To swap two variables: the value of the first variable will become the value of the second variable. On the other hand, the value of the second variable will become the value of the first variable.

firstName = 'Mohammad'
secondName = 'Farhad'
print(firstName + secondName)

temp = firstName
firstName = secondName 
secondName = temp
print(firstName + secondName)