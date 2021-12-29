
import getopt, sys

#Command to run the script, example
#python grep-demo.py -p "Mon Dec 05 18:20:53 2005" -f server.log

# Remove 1st argument from the
# list of command line arguments
argumentList = sys.argv[1:]
 
# Options
options = "hp:f:"
 
# Long options
long_options = ["Pattern", "File"]


pattern = ''
content = ''
try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)
    # print(f'arguments - {arguments}')
    # print(f'values - {values}')

    # checking each argument
    for currentArgument, currentValue in arguments:
        
        if currentArgument in ("-h", "--Help"):
            print ("Use -p for Pattern and -f for passing the name of the file")
            print('Example command: - python grep-demo.py -p "Mon Dec 05 18:20:53 2005" -f server.log')

        elif currentArgument in ("-p", "--pattern"):    
            pattern = currentValue                    
             
        elif currentArgument in ("-f", "--file"):
            content = currentValue            
except getopt.error as err:
    # output error, and return with an error code
    print (str(err))

if pattern == '':
    pattern = 'Mon Dec 05 18:20:53 2005'

if content == '':
    content = 'server.log'


print(f'Pattern - {pattern} : File - {content}')

result = []


#File handling
with open(f'd:/Ganesh/study/Practice/Python/Python-Tutorial/resources/{content}') as rf:
    line = rf.readline()
    # print(type(line))
    while line:
        #print(f'line: {line}', end =" ")
        if pattern in line:
             result.append(line)
        line = rf.readline()

    print('******************************************************************')
    print(f'Here is the result:-')
    print('******************************************************************')
    for record in result:
        print(record, end ="")