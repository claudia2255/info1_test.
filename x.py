name = input('What is your name: ')
pretty = input('From 1 to 10, how handsome are you?: ')
gf = input ('From 1 to 10, how much do you think your girlfriend loves you?: ')
msg = 'Hi {name}, welcome to this server. Your input is: you are {pretty} handsome and your girlfriend loves you in scale {gf}.'
msg2 = input('Is this right? Yes or No?: ')
if msg2 == 'yes' or 'Yes':
	print('This input is indeed correct your girlfriend loves you very much and you are very hansome')
elif msg2 == 'no' or 'No':
	print('Well, next time write the truth from the beginning. Your are a selfless bitch. I do not want to code anymore')
else:
    print('Ups! Your input was not correct.')
