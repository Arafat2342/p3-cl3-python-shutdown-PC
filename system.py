import os

shutdown = input('Do you wish to shutdown your PC? (Yes / No): ')

if shutdown.lower() == 'no':
    exit()
elif shutdown.lower() == 'yes':
    os.system("shutdown /s /t 1")
else:
    print('invalid input!')