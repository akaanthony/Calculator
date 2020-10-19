print('Welcome to the vennus calculater')
print('Addition is +')
print('Subtraction is -')
print('Multiplication is *')
print('Division is /')
xe=input('Enter a operater ')
num_1=float(input('Enter your first number: '))
num_2=float(input('Enter your second number: '))


if xe == '+':
  print('Your answer is', num_1 + num_2,)
elif xe == '-':
  print('Your answer is', num_1 - num_2,)
elif xe == '/':
  print('Your answer is', num_1 / num_2,)
elif xe == '*':
  print('Your answer is', num_1 * num_2,)
else:
  print('You entered a invalid operator')

while True:
  yz = input("Would you like to complete another equation? ").lower()
  if yz == 'yes':
    xe=input('Enter a operater ')
    num_1=float(input('Enter your first number: '))
    num_2=float(input('Enter your second number: '))
    if xe == '+':
      print('Your answer is', num_1 + num_2,)
    elif xe == '-':
      print('Your answer is', num_1 - num_2,)
    elif xe == '/':
      print('Your answer is', num_1 / num_2,)
    elif xe == '*':
      print('Your answer is', num_1 * num_2,)
    else:
      print('You entered a invalid operator')

  elif yz == 'no':
    print('Thanks so much for usuing venus calculater')
    quit()



