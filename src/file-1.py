# randomQuizGenerator.py - Creates quizzes with questions and answers in random order, along with the answer key.

import random

import os

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Generate 35 quiz files.





os.chdir('D:\\Ganesh\\study\\Practice\\Python\\Python-Tutorial\\resources\\quiz')

location = os.getcwd()
print(f'location: {location}')
    
for quizNum in range(35):
    # TODO: Create the quiz and answer key files.    
    with open(f'Capital_quiz_{quizNum+1}.txt','w') as quizFile:
        with open(f'Capital_ans_{quizNum+1}.txt','w') as ansFile: 
            quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
            quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
            quizFile.write('\n\n')
            
            ansFile.write('Answers:\n')

            #Get states
            states = list(capitals.keys())
            random.shuffle(states)

            #Write question
            for quesNum in range(50):
                state = states[quesNum]
                capital = capitals[state]
                options = list(capitals.values())
                
                del options[options.index(capital)]            
                options = random.sample(options,3)
                options.append(capital)
                random.shuffle(options)

                #write question
                quizFile.write(f'{(quesNum+1)}. What is the capital of {state}?\n')
                quizFile.write(f'A. {options[0]}\nB. {options[1]}\nC. {options[2]}\nD. {options[3]}\n\n\n')

                ansFile.write(f'{(quesNum+1)}. {capital}\n')
