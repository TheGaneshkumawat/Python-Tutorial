# Print welcome message
message = 'Hello World!'

print(message.lower())
print(len(message))
print(message[0:5])
print(message[:5])
print(message[-3:])

#reverse
print("reverse: "+message[::-1])
print("find index: {}{}".format(message.find('World'),' Ganesh'))
print("Concat example: {}{}".format(message.find('World'),' Ganesh'))
index = message.find('World')
name = 'Ganesh'
print(f" example: {message.find('World')} {name}")

#print("help:"+help(str))
print("methods:"+dir(name))

print("Replace: "+message.replace('World','Ganesh'))
print(message.count('l'))