#This programme says hello and asks for my name

print('Hello world!')
print ('What is your name?')    #Asks for the users name
myName = input()
print('it is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('what is your age?')      #ask for the users age
myAge = input()
print('you will be ' + str(int(myAge) + 1) + 'in a year.')
