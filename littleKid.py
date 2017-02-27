name = str()
age = str()
print('What is your name?')
name = input()
print('what is your age?')
age = input()
int(age)

if name == 'Alice':
    print('Hi, Alice.')
elif age < int(12):
    print('You are not Alice, kiddo.')
else:
    print('You are neither Alice or a little kid.')
    
