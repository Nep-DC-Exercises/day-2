name = input('What is your name? ')
print('Hello, ' + name)

# UPPER
name_upper = input('WHAT IS YOUR NAME? ').upper()
print('HELLO, ' + name_upper)
name_length = len(name_upper)
print(f'Your name has {name_length} characters.')


# MADLIB

print('Please fill in the blanks below: ')
print('____(name)____\'s favorite subject in school is ____(subject)____.')

madlib_name = input('What is the name? ')
madlib_subject = input('What is subject? ')

print(f'{madlib_name}\'s favorite subject in school is {madlib_subject}.')