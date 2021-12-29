import os
from pathlib import Path

print(__name__)


def main():
    adjective = input("Enter an Adjective\n")
    noun = input("Enter an noun\n")
    verb = input("Enter an verb\n")

    with open('d:/Ganesh/study/Practice/Python/Python-Tutorial/resources/text.txt','r') as rf:
        with open('d:/Ganesh/study/Practice/Python/Python-Tutorial/resources/text_new.txt','w') as wf:
            text = rf.read()
            text = text.replace('ADJECTIVE', adjective)
            text = text.replace('NOUN', noun)
            text = text.replace('VERB', verb)
            wf.write(text)

if __name__ == '__main__':
    main()