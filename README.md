# holidays_checker
each day checks holidays and birthdays, them send me a e-mail

**TASK:**
I need to write this script after I forgot a family member's birthday. The goal was simple: write an script that would remind me of holidays, run it as soon as I turn on my PC in the morning.

**SOLUTION:**
The program will go through the .txt file in the folder that contains all the information about the family member's holidays entered by me, then it will send an email about the current holidays, and at the same time it will write a message in a simple window.

**USAGE:**
Uses data.txt to read date of holidays and then mail.txt to acces in to mail bot to send message to a specific email. It is necessary to have .txt files with data and mail in the folder with the main.py file (use reletive paths).

**CAVEAT:**
To start the program, I use WIN Task Scheduler set to windows startUp, so that if the computer is restarted, the program will start again, and if the computer does not turn on at all that day, the program will not start itself.

At the same time, with this setting, it is necessary to let the program run and end it with the "CLOSE WINDOW" button, pressing "x" would change the program in task scheduler to disabled and it would not start again.

**NOTE:**
For sending mail you need have created e-mail, i use one from google. You need to use 2FA and set new APP password (mail , my PC, generate) and follow the instructions.
