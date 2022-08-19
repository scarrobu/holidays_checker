# Import modules.
import datetime as dt
import smtplib
from email.mime.text import MIMEText
from tkinter import *

# Create TKinter canvas.
canvas = Tk()
canvas.title("WAS THE HOLIDAY FOUND?")

# MY OWN FUNCTIONS.
# Close TKinter window.
def click():
    canvas.destroy()

# Send e-mail.
def sendMail():
    global number
    while number != 0:
        s=smtplib.SMTP(mail_account, port)
        s.ehlo()
        s.starttls()
        s.login(mail_login_name, mail_login_pass)

        msg = MIMEText(str(message[number-1]))
        msg['subject'] = msg_subject
        msg['from'] = msg_from
        msg['To'] = msg_to

        s.sendmail(str(mail_login_name),([email[number-1]]), msg.as_string())
        print("email sent!")
        number -= 1

# Find type of holiday.
def find():
    if stack == "BIRTHDAY":
        return find2
    elif stack == "DAY OF NAME":
        return find1
    elif stack == "HOLIDAY":
        return find4
    elif stack == "DAY":
        return find5
    else:
        return find3

# Insert text in to e-mail, message to the recipient.
def messageTEXT():
    if stack == "BIRTHDAY":
        return ("All the best to yours today " + str(old) +
                ". We wish you good health and happiness on your birthday.")
    elif stack == "DAY OF NAME":
        return "We wish you all the best for your day of name, good luck and health."
    elif stack == "HOLIDAY":
        return "TODAY IS HOLIDAY."
    elif stack == "DAY":
        return "TODAY IS RESERVED DAY."
    else:
        return find3

# Základné premenné
dateNow = dt.datetime.now()
year, month, day = dateNow.year, dateNow.month, dateNow.day
_day, _month, _year, _name, _holliday = [], [], [], [], [],
mail, data, structure, message, email = [], [], [], [], []

find1 = "Holiday found: DAY OF NAME."
find2 = "Holiday found: BIRTHDAY."
find3 = "Holiday not found! No email to send today!"
find4 = "Holiday found: HOLIDAY."
find5 = "Holiday found: RESERVED DAY"

mail1 = "E-MAIL sent successfully."
mailAmount = ""

stack = ""
age = ""
_nameTk = ""

message1 = "We wish you all the best for your day of name, good luck and health."
message2 = ("All the best to yours today " + str(age) +
           ". We wish you good health and happiness on your birthday.")
message3 = "NO MESSAGE"

# It opens and retrieves the data needed to log in to the e-mail.
with open("mail.txt") as file:
    for line in file:
        account = line.split(",")
        account, passw = account[0], account[1]

# Parameters needed to log in to the account and send an email.
mail_account ="smtp.gmail.com"
port = 25
mail_login_name = account
mail_login_pass = passw
msg_subject = "found HOLIDAY"
msg_from = "pybot-hollidays"
msg_to = "addressee"

# Converts int output to str and adds 0 to the string if i is a single digit.
if day < 10:
    pday = "0" + str(day)
else:
    pday = str(day)
if month < 10:
    pmonth = "0" + str(month)
else:
    pmonth = str(month)

# program logic, open file reads data, compares and evaluates, further controls the program.
with open("data.txt") as file:
    for line in file:
        data = line.split(",")
        _day, _month, _year, _name, _holliday, mail = data[0], data[1], data[2], data[3], data[4], data[5]
        age = int(year) - int(_year)
        age1 = age

        if pday == _day and pmonth == _month:
            structure = _name, _holliday
            global old
            old = age
            _nameTk = _name

            try:
                if structure[1] == 'BIRTHDAY':
                    message.append("Today is " + str(day) + "." + str(month) + " and " +
                                  _holliday + " has " + _name + " and has " + str(age)+" years." +
                                  "\n\nAll the best to yours today " + str(age) +
                                  ". We wish you good health and happiness on your birthday.")
                    email.append(mail)
                    print(find2)
                    stack = structure[1]

                elif structure[1] == 'NAME_DAY':
                    message.append("Today is "+str(day)+"."+str(month)+" and "+_holliday+" has "+_name +"\n\nWe wish you all the best for your day of name, good luck and health.")
                    email.append(mail)
                    print(find1)
                    stack = structure[1]

                elif structure[1] == "HOLIDAY":
                    message.append("Today is "+str(day)+"." +str(month)+" and is "+_name)
                    email.append(mail)
                    print(find4)
                    stack = structure[1]

                elif structure[1] == "DAY":
                    message.append("Today is "+str(day)+"."+str(month)+" and is "+_name)
                    email.append(mail)
                    print(find5)
                    stack = structure[1]

            except IndexError:
                print(find3)
                stack = structure[1]

number = len(message)
str(email)

# The e-mail function calls itself.
sendMail()

# Labels for Tkinter window in windows.
label = Label(canvas, text="RESULT: ", font=("Helvetica", 15))
label.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

conclusion = Label(canvas, text=find(), font=("Helvetica", 15))
conclusion.grid(row=1, column=0, columnspan=5, padx=5, pady=5)

_name = Label(canvas, text=_nameTk, font=("Helvetica", 15))
_name.grid(row=2, column=0, columnspan=5, padx=5, pady=5)

message = Entry(canvas, width=100, borderwidth=2, font=("Helvetica", 12))
message.insert(0, messageTEXT())
message.grid(row=3, column=0, columnspan=5, padx=5, pady=5)

but1 = Button(canvas, text="CLOSE WINDOW!", comman=click, font=("Helvetica", 15))
but1.grid(row=4, column=0, columnspan=5, padx=5, pady=5)

# Loop to keep the window open.
canvas.mainloop()

# End of program.
