#user input age
age = int(input('Enter your age: '))
#output if age<=1 then infant
if age <= 1:
  print('You are an infant.')
#output if age>1 and age<13 then child
elif age > 1 and age < 13:
  print('You are a child.')
#output if age>=13 and age<20 then teenager
elif age >= 13 and age < 20:
  print('You are a teenager')
#output if age>=20 then adult
else:
  print('You are an adult.')