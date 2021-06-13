#!/usr/bin/python3

import pickle
import os
import sys
import time
import datetime


def print_slow(str, delay = 0.1):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(delay)
    print("\n")


def reset_console():
    print("\n")
    os.system('cls||clear')


def fprint(str, delay = 0):
    print("\n" + str)
    time.sleep(delay)


def sprint(str, delay = 0):
    print(str)
    time.sleep(delay)


data = {"reminders":[],}


def load():
    with open('data/data.pickle', 'rb') as handle:
        saved_data = pickle.load(handle)
        data.update(saved_data)


def save():
    with open('data/data.pickle', 'wb') as handle:
        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)


def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!")
    elif hour>=12 and hour<18:
        print("Good Afternoon!")   
    else:
        print("Good Evening!")  


def add_reminders():
    fprint("Sure! Enter your reminder.")
    r = input("\n> ")
    data["reminders"].append(r)
    save()
    fprint("Alright. I have that saved.")
    fprint("If you want to enter something else, enter 'a' again.")
    fprint("To return to the main menu, enter 'm'.")
    while True:
        a = input("\n> ")
        if a == 'a':
            add_reminders()
        elif a == 'm':
            welcome()
        else:
            fprint("Invalid command. Try again.")


def clear_reminders():
    os.system('clear')
    data["reminders"].clear()
    save()
    fprint("Okay. I deleted your reminders.")
    fprint("Enter 'm' to return to the main menu.")
    while True:
        a = input("\n> ")
        if a == 'm':
            welcome()
        else:
            fprint("Invalid command. Try again.")


def delete_reminders():
    os.system('clear')
    index = -1
    for items in data["reminders"]:
        index += 1
        fprint(f'{index} - ' + items)
    fprint("Enter the ID of the reminder you want to delete.")
    fprint("Or enter 'back' to go back.")
    while True:
        a = input("\n> ")
        if a == "back":
            welcome()
        elif a.isdigit():
            if 0 <= int(a) < len(data["reminders"]):
                del data["reminders"][int(a)]
                save()
                welcome()
            else:
                fprint("Not a valid ID. Try again.")
        else:
            fprint("Invalid command. Try again.")


def welcome():
    os.system('clear')
    load()
    wish_me()
    if len(data["reminders"]) == 0:
        fprint("You don't have any reminders today.")
    else:
        fprint("Here are your reminders:")
        index = -1
        for items in data["reminders"]:
            index += 1
            fprint(f'{index} - ' + items)
    fprint("How may I assist you today?")
    fprint("Type 'd' to delete your reminders, 'c' to clear your reminders,")
    fprint("'a' to add your reminders, or or 'e' to exit.")
    while True:
        a = input("\n> ")
        if a == 'd':
            delete_reminders()
        elif a == 'c':
            clear_reminders()
        elif a == 'a':
            add_reminders()
        elif a == 'e':
            sys.exit()
        else:
            fprint("Invalid command. Try again.")


welcome()