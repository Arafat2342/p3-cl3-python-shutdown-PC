import os

shutdown = input('Do you wish to shutdown your PC? (Yes / No): ')

if shutdown.lower() == 'no':
    exit()
else:
    os.system("shutdown /s /t 1")