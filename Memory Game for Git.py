import random
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import time
import mysql.connector
# Install pyperclip if you haven't already using: "pip install pyperclip"
import pyperclip

timer = 998.999999999999999
time1 = time.time()

root = Tk(className = ' Currency GK Game')
root.geometry("600x600")
root.configure(bg = '#0000FF')

count = 0
ans_list = []
ans_dict = {}
hint_used = False

global cards, matches

# Shuffle cards
cards = ['£','£','¢','¢','Br','Br','₪','₪','₩','₩','Дин.','Дин.','₨','₨','฿','฿']
random.shuffle(cards)

# Win counter
matches = 0

# Create cards
game_frame = Frame(root)
game_frame.pack(pady = 5)

# Use a hint
def hint():
    global hint_used
    hint_used = True
    hint_list = [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15]
    for hint in hint_list:
        if hint["bg"] != "black":
            a = hint_list.index(hint)
            hint["text"] = cards[a]
            break

# Reset the game
def reset():
    global time1
    time1 = time.time()
    start = 0
    end = 0
    global cards, matches, count, card_list, my_label
    # Reset counters
    matches = 0
    count = 0
    # Reshuffle cards
    cards = ['£','£','¢','¢','Br','Br','₪','₪','₩','₩','Дин.','Дин.','₨','₨','฿','฿']
    random.shuffle(cards)
    # Reset the label
    my_label.config(text = "By: Pranav Goyal", font = ("Times", "15", "bold"))
    # Reset the cards
    card_list = [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15]
    # Color the buttons after winning
    for card in card_list:
        card.config(text = ' ', bg = "SystemButtonFace", state = 'normal')
    elapsed.config(text = '')

# User wins
def win():
    global time2
    time2 = time.time()
    global timer
    timer = time2 - time1
    global elapsed
    # Show time elapsed to the user
    elapsed.config(text = f"Time: {timer:.5f}s")
    # Change the label
    if hint_used == True:
        my_label.config(text = "Hope you learned :)) even though you used a hint :/")
    else:
        my_label.config(text = "Congratulations! Hope you learned :)")
    card_list = [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15]
    # Reminder to login
    win_window = tkinter.Toplevel(root)
    win_window.title("Congrats!")
    error_label = tkinter.Label(win_window, text = "Login to save results")
    error_label.pack()  
    OK_Button = tkinter.Button(win_window, text = "OK", command = win_window.destroy)
    OK_Button.pack()
    # Loop through buts to color them after winning
    for card in card_list:
        card.config(bg = "green2")

# Function for clicking buttons
def but_click(b, num):
    global count, ans_list, ans_dict, matches, card_list, hint_used

    if b["text"] == ' ' and count <= 1 or hint_used == True and count <= 1:
        b["text"] = cards[num]
        # Add number to answer list (to keep track of what cards we have flipped)
        ans_list.append(num)
        # Add number to answer dictionary (to return the actual value on the card)
        ans_dict[b] = cards[num]
        # Increments the counter
        count+=1

    # Determines whether the currencies match or not
    if len(ans_list) == 2:
        if cards[ans_list[0]] == cards[ans_list[1]]:
            my_label.config(text='Match!')
            # Displays the currency name if user matches the symbols
            if cards[ans_list[0]] == '£':
                messagebox.showinfo("Currency", "Falkland Islands (Malvinas) Pound")
            elif cards[ans_list[0]] == '¢':
                messagebox.showinfo("Currency", "Ghana Cedi")
            elif cards[ans_list[0]] == 'Br':
                messagebox.showinfo("Currency", "Belarus Ruble")
            elif cards[ans_list[0]] == '₪':
                messagebox.showinfo("Currency", "Israel Shekel")
            elif cards[ans_list[0]] == '₩':
                messagebox.showinfo("Currency", "Korea (North) Won")
            elif cards[ans_list[0]] == 'Дин.':
                messagebox.showinfo("Currency", "Serbia Dinar")
            elif cards[ans_list[0]] == '₨':
                messagebox.showinfo("Currency", "Seychelles Rupee")
            elif cards[ans_list[0]] == '฿':
                messagebox.showinfo("Currency", "Thailand Baht")
            for x in ans_dict:
                x["state"] = "disabled"
                x["bg"] = "black"
            count = 0
            ans_list = []
            ans_dict = {}
            # Increments the counter keeping track of number of matches
            matches+=1
            # Checks if user has won
            if matches == 8:
                win()
        else:
            count = 0
            ans_list = []
            # Popup box
            messagebox.showinfo("Incorrect!", "Incorrect")
            my_label.config(text = 'No match :(')
            # Resets the cards
            for x in ans_dict:
                x["text"] = ' '

            ans_dict = {}

# Place the cards
c0 = Button(game_frame, text = ' ', font = ("Helvetica", 20), height = 3, width = 6,
            command = lambda: but_click(c0, 0), relief = "raised")
c1 = Button(game_frame, text = ' ', font = ("Helvetica", 20), height = 3, width = 6,
            command = lambda: but_click(c1, 1), relief = "raised")
c2 = Button(game_frame, text = ' ', font = ("Helvetica", 20), height = 3, width = 6,
            command = lambda: but_click(c2, 2), relief = "raised")
c3 = Button(game_frame, text = ' ', font = ("Helvetica", 20), height = 3, width = 6,
            command = lambda: but_click(c3, 3), relief = "raised")
c4 = Button(game_frame, text = ' ', font = ("Helvetica", 20), height = 3, width = 6,
            command = lambda: but_click(c4, 4), relief = "raised")
c5 = Button(game_frame, text = ' ', font = ("Helvetica", 20), height = 3, width = 6,
            command = lambda: but_click(c5, 5), relief = "raised")
c6 = Button(game_frame, text = ' ', font = ("Helvetica", 20), height = 3, width = 6,
            command = lambda: but_click(c6, 6), relief = "raised")
c7 = Button(game_frame, text = ' ', font = ("Helvetica", 20), height = 3, width = 6,
            command = lambda: but_click(c7, 7), relief = "raised")
c8 = Button(game_frame, text = ' ', font = ("Helvetica", 20), height = 3, width = 6,
            command = lambda: but_click(c8, 8), relief = "raised")
c9 = Button(game_frame, text = ' ', font = ("Helvetica", 20), height = 3, width = 6,
            command = lambda: but_click(c9, 9), relief = "raised")
c10 = Button(game_frame, text = ' ', font = ("Helvetica", 20), height = 3, width = 6,
             command = lambda: but_click(c10, 10), relief = "raised")
c11 = Button(game_frame, text = ' ', font = ("Helvetica", 20), height = 3, width = 6,
             command = lambda: but_click(c11, 11), relief = "raised")
c12 = Button(game_frame, text = ' ', font = ("Helvetica", 20), height = 3, width = 6,
             command = lambda: but_click(c12, 12), relief = "raised")
c13 = Button(game_frame, text = ' ', font = ("Helvetica", 20), height = 3, width = 6,
             command = lambda: but_click(c13, 13), relief = "raised")
c14 = Button(game_frame, text = ' ', font = ("Helvetica", 20), height = 3, width = 6,
             command = lambda: but_click(c14, 14), relief = "raised")
c15 = Button(game_frame, text = ' ', font = ("Helvetica", 20), height = 3, width = 6,
             command = lambda: but_click(c15, 15), relief = "raised")

# Organization
c0.grid(row = 0, column = 0, padx = 20, pady = 5)
c1.grid(row = 0, column = 1, padx = 20, pady = 5)
c2.grid(row = 0, column = 2, padx = 20, pady = 5)
c3.grid(row = 0, column = 3, padx = 20, pady = 5)
c4.grid(row = 1, column = 0, padx = 20, pady = 5)
c5.grid(row = 1, column = 1, padx = 20, pady = 5)
c6.grid(row = 1, column = 2, padx = 20, pady = 5)
c7.grid(row = 1, column = 3, padx = 20, pady = 5)
c8.grid(row = 2, column = 0, padx = 20, pady = 5)
c9.grid(row = 2, column = 1, padx = 20, pady = 5)
c10.grid(row = 2, column = 2, padx = 20, pady = 5)
c11.grid(row = 2, column = 3, padx = 20, pady = 5)
c12.grid(row = 3, column = 0, padx = 20, pady = 5)
c13.grid(row = 3, column = 1, padx = 20, pady = 5)
c14.grid(row = 3, column = 2, padx = 20, pady = 5)
c15.grid(row = 3, column = 3, padx = 20, pady = 5)

# Bottom-center label
my_label = Label(root, text= '')
my_label.pack(pady = 20)
my_label.config(text = "By: Pranav Goyal", font = ("Times", "15", "bold"))
# Shows the time taken to win
elapsed = Label(root, text = '', font = ("Helvetica", "13"))
elapsed.place(relx = 1, rely = 1, anchor = 'se')

# Create a menu
menubar = Menu(root)
root.config(menu = menubar)

# Create an Options dropdown
options = Menu(menubar, tearoff = False)
menubar.add_cascade(label = "Game Options", menu = options)
options.add_command(label = "Use a Hint", command = hint)
options.add_separator()
options.add_command(label = "Reset Game", command = reset)
options.add_separator()
options.add_command(label = "Exit Game", command = root.destroy)

# Login window
def login_window():
    global timer
    window = tkinter.Toplevel(root)
    window.title("Login")
    canvas = tkinter.Canvas(window, height = 20, width = 100)
    canvas.pack()
    # Space to enter username and password
    username_label = tkinter.Label(window, text = "Username", bg = '#333333', fg = "#FFFFFF",
                                   font = ("Arial", 16))
    username_label.pack()
    username_entry = tkinter.Entry(window, font = ("Arial", 16))
    username_entry.pack()
    password_label = tkinter.Label(window, text = "Password", bg = '#333333', fg = "#FFFFFF",
                                   font = ("Arial", 16))
    password_label.pack()
    password_entry = tkinter.Entry(window, show = "*", font = ("Arial", 16))
    password_entry.pack()
    def login():
        user = username_entry.get()
        pwd = password_entry.get()
        global timer
        # Enters the credentials into SQL database
        if user != '' and pwd != '':
            account.entryconfig("Login", state = "disabled")
            account.entryconfig("Logout", state = "active")

            mydb = mysql.connector.connect(host = '', user = 'root', password = '',
                                           database = 'memory')
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM Leaderboard WHERE user = %s", (user,))
            result = mycursor.fetchone()
            if result:
                old_time = result[2]
                ogpwd = result[1]
                if pwd == ogpwd:
                    # Updates the user's score with a new personal best, if applicable
                    if timer < old_time:
                        mycursor.execute("UPDATE Leaderboard SET time = %s WHERE user = %s",
                                         (timer, user))
                        mydb.commit()
                else:
                    # Error message for incorrect credentials
                    incorrectpwd = tkinter.Toplevel(root)
                    incorrectpwd.title("Error")
                    wrong_label = tkinter.Label(incorrectpwd, text = "Incorrect password")
                    wrong_label.pack()
                    OK_Button = tkinter.Button(incorrectpwd, text = "OK", command = incorrectpwd.destroy)
                    OK_Button.pack()

            else:
                mycursor.execute("INSERT INTO Leaderboard (user, pwd, time) VALUES (%s, %s, %s)",
                                 (user, pwd, timer)) 
                mydb.commit()
            mycursor.close()
            mydb.close()

            window.destroy()
        else:
            # Error message for incorrect credentials
            error_window = tkinter.Toplevel(root)
            error_window.title("Error")
            error_label = tkinter.Label(error_window, text = "Invalid username and/or password")
            error_label.pack()
            OK_Button = tkinter.Button(error_window, text = "OK", command = error_window.destroy)
            OK_Button.pack()
    login_but = tkinter.Button(window, text = "Login", bg = "#FF3399", fg = "#FFFFFF", font = ("Arial", 16), command = login)
    login_but.pack()
    def gen():
        strwindow = tkinter.Toplevel(root)
        strwindow.title("Strong password")
        keyboard = [chr(i) for i in range(32, 127)]
        keyboard.extend([chr(i) for i in range(65, 91)])
        keyboard.extend([chr(i) for i in range(97, 123)])
        keyboard.extend([chr(i) for i in range(48, 58)])
        bestpwd = ''
        for i in range(20):
            j = random.randint(0, len(keyboard) - 1)
            bestpwd = bestpwd + keyboard[j]
        strlabel = tkinter.Label(strwindow, text = "Here is a strong password to use: {}".format(bestpwd))
        strlabel.pack()
        pyperclip.copy(bestpwd)
        OK_Button = tkinter.Button(strwindow, text = "OK", command = strwindow.destroy)
        OK_Button.pack()
    strongpwd_but = tkinter.Button(window, text = "Generate password?", fg = "#2885D8", font = ("Helvetica", 12), command = gen)
    strongpwd_but.pack()
    username_label.pack()
    username_entry.pack()
    password_label.pack()
    password_entry.pack()

# Reactivates the login button
def logout():
    account.entryconfig("Login", state = "active")
    account.entryconfig("Logout", state = "disabled")

# Allows user to view the leaderboard
def scores():
    mydb = mysql.connector.connect(host = '', user = 'root', password = '', database = 'memory')
    mycursor = mydb.cursor()
    mycursor.execute("SELECT user, time FROM Leaderboard ORDER BY time")
    myrecords = mycursor.fetchall()
    if myrecords:
        print("Leaderboard:")
        print("{:<30} {:<10}".format("Username", "Time (seconds)"))
        print("-" * 45)
        for x in myrecords:
            username, time = x
            print("{:<30} {:<10.5f}".format(username, time))
    else:
        print("Leaderboard is empty")

# Allows user to delete their score from the leaderboard
def delete():
    window1 = tkinter.Toplevel(root)
    window1.title("Delete Score")
    window1_label = tkinter.Label(window1, text = '''Are you sure
                    you want to delete your score?                   ''', bg = '#333333', fg = "#FFFFFF",
                                  font = ("Arial", 14), justify="center")
    window1_label.pack()
    canvas = tkinter.Canvas(window1, height = 20, width = 100)
    canvas.pack()
    def permaban():
        window2 = tkinter.Toplevel(root)
        window2.title("Enter credentials")
        canvas = tkinter.Canvas(window1, height = 20, width = 100)
        canvas.pack()
        username_label = tkinter.Label(window2, text = "Username", bg = '#333333', fg = "#FFFFFF",
                                    font = ("Arial", 16))
        username_label.pack()
        username_entry = tkinter.Entry(window2, font = ("Arial", 16))
        username_entry.pack()
        password_label = tkinter.Label(window2, text = "Password", bg = '#333333', fg = "#FFFFFF",
                                    font = ("Arial", 16))
        password_label.pack()
        password_entry = tkinter.Entry(window2, show = "*", font = ("Arial", 16))
        password_entry.pack()
        def enter():
            user = username_entry.get()
            pwd = password_entry.get()
            mydb = mysql.connector.connect(host = '', user = 'root', password = '', database = 'memory')
            mycursor = mydb.cursor()
            mycursor.execute("SELECT user, pwd FROM Leaderboard WHERE user = %s", (user,))
            result = mycursor.fetchone()
            if result:
                if result[1] == pwd:
                    mycursor.execute("DELETE FROM Leaderboard WHERE user = %s", (user,))
                    mydb.commit()
                    window2.destroy()
                else:
                    error_window = tkinter.Toplevel(root)
                    error_window.title("Error")
                    error_label = tkinter.Label(error_window, text = "Incorrect password")
                    error_label.pack()
                    OK_Button = tkinter.Button(error_window, text = "OK", command = error_window.destroy)
                    OK_Button.pack()
            else:
                error_window = tkinter.Toplevel(root)
                error_window.title("Error")
                error_label = tkinter.Label(error_window, text = "User doesn't exist")
                error_label.pack()
                OK_Button = tkinter.Button(error_window, text = "OK", command = error_window.destroy)
                OK_Button.pack()

        enter_but = tkinter.Button(window2, text = "Enter", bg = "#FF3399", fg = "#FFFFFF",
                                  font = ("Arial", 16), command = enter)
        enter_but.pack()
        window1.destroy()
    yes = tkinter.Button(window1, text = "Yes", bg = "#FF3399", fg = "#FFFFFF", font = ("Arial", 12),
                         command = permaban)
    yes.pack()
    no = tkinter.Button(window1, text = "No", bg = "#FF3399", fg = "#FFFFFF", font = ("Arial", 12),
                        command = window1.destroy)
    no.pack()

# Create a login dropdown
account = Menu(menubar, tearoff = False)
menubar.add_cascade(label = "Account", menu = account)
account.add_command(label = "Login", command = lambda: login_window())
account.add_command(label = "Logout", command = lambda: logout())
account.add_command(label = "Delete a Score", command = delete)
account.entryconfig("Logout", state = "disabled")

# Dropdown to view the leaderboard
leaderboard = Menu(menubar, tearoff = False)
menubar.add_cascade(label = "Scores", menu = leaderboard)
leaderboard.add_command(label = "View the Leaderboard", command = scores)

# Keeps the GUI responsive
root.mainloop()