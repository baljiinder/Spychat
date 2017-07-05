#This is for importing Spy, spy, ChatMessage from the Spy_details
from spy_details import spy, Spy, ChatMessage, friends
#This is for importing steganography form the steganography
from steganography.steganography import Steganography
#This is for importing datetime from datetime
from datetime import datetime
#This is for importing colored from termcolor
from termcolor import colored
#to contain the previous statuses
STATUS_MESSAGES = ['Available', 'Busy','At school','At the movies','In a meeting','Sleeping', 'Watching movies']

print "Hello! Let\'s get started"
#selection between new or old user
question = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? "
existing = raw_input(question)

#function to add a new status
def add_status():
    updated_status_message = None

    if spy.current_status_message != None:
    #prints your current status
        print 'Your current status message is %s \n' % (spy.current_status_message)
    else:
        #Default message in case of unavailabilty of a current message
        print 'You don\'t have any status message currently \n'
    #Choice to select from older status
    default = raw_input("Do you want to select from the older status (y/n)? ")
    #to set a custom status
    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set? ")
        #to add your status to current status list
        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message
    #to select from previous statuses
    elif default.upper() == 'Y':

        item_position = 1

        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above messages "))

        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print 'The option you chose is not valid! Press either y or n.'

    if updated_status_message:
        print 'Your updated status message is: %s' % (updated_status_message)
    else:
        print 'You current don\'t have a status update'

    return updated_status_message
#function to add a new friend

def add_friend():
    new_friend = Spy('', '', 0, 0.0,0)
    #to add new friend's name and salutation
    new_friend.name = raw_input("Please add your friend's name: ")
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")

    #add friend's age
    new_friend.age = raw_input("Age?")
    new_friend.age = int(new_friend.age)
    #add friend's spy rating
    new_friend.rating = raw_input("Spy rating?")
    new_friend.rating = float(new_friend.rating)
    #validation of name, age and salutation
    if len(new_friend.name)>0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        print 'Friend Added!'
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    return len(friends)

#function to select a friend from the list of friends
def select_a_friend():
    item_number = 0

    for friend in friends:
        print '%d. %s %s aged %d with rating %.2f is online' % (item_number + 1, friend.salutation, friend.name,
                                                                friend.age,
                                                                friend.rating)
        item_number = item_number + 1

    friend_choice = raw_input("Choose from your friends")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position

#function to send a message to a friend
def send_message():
    friend_choice = select_a_friend()
    #taking the image encoding it and appending it to the chats
    original_image = raw_input("What is the name of the image?")
    output_path = "output.jpg"
    text = raw_input("What do you want to say? ")

    print "Your secret message image is ready!"
    if len(text) > 0:
        Steganography.encode(original_image, output_path, text)
        new_chat = ChatMessage(text, True)

        friends[friend_choice].chats.append(new_chat)

        print colored('Your secret message image is ready!', 'yellow')
    else:
        print colored('Please enter any valid message', 'Green')


#function to decode and read a secret message
def read_message():
    sender = select_a_friend()

    output_path = raw_input("What is the name of the file?")

    secret_text = Steganography.decode(output_path)
    #to count the number of words a friend is speaking
    friends[sender].word_count+=len(secret_text.split())
    #to delete the friend if he/she speaks more than 100 words
    if friends[sender].word_count> 100:
        del friends[sender]
        print "Friend deleted for talking too much/Spam"
    else:
        new_chat = ChatMessage(secret_text, False)
    #validation of secret messsage
        friends[sender].chats.append(new_chat)
        if len(secret_text)==0:
            print "No secret message"
            #check for special messages
        elif secret_text.upper()=="SOS" or secret_text.upper()=="Save me":
            print "Message = %s" % secret_text
            print "DANGER"
            print "Your secret message has been saved!"
        else :
            print "Message = %s" % secret_text
            print "Your secret message has been saved!"

#function to read chat history
def read_chat_history():
    read_for = select_a_friend()

    print '\n'

    for chat in friends[read_for].chats:
        #different colours used to print time and name
        if chat.sent_by_me:
            print '[%s] %s said: %s' % (
            colored(chat.time.strftime("%d %B %Y"), 'blue'), colored('You ', 'yellow'), chat.message)
        else:
            print '[%s] %s said: %s' % (
            colored(chat.time.strftime("%d %B %Y"), 'blue'), colored(friends[read_for].name, 'yellow'), chat.message)

#Removing a friend from the existing friend list
def remove_friend():
            friend_choice = select_a_friend()
            friend_choice_position = int(friend_choice)
            del friends[friend_choice_position]
            print 'Friends removed successfully'


#function to start a chat
def start_chat(spy):
    spy.name = spy.salutation + " " + spy.name

    if spy.age > 12 and spy.age < 50:

        print "Authentication complete. Welcome " + spy.name + " age: " \
              + str(spy.age) + " and rating of: " + str(spy.rating) + " Proud to have you onboard"

        show_menu = True
        #loop to show the menu untill our application is terminated
        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Remove a friend \n 7. Close Application \n"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    spy.current_status_message = add_status()
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice == 5:
                    read_chat_history()
                elif menu_choice == 6:
                    remove_friend()
                else:
                    show_menu = False
    else:
        print 'Sorry you are not of the correct age to be a spy'


if existing.upper() == "Y":
    start_chat(spy)
#function to add a new spy
elif existing.upper() == "N":

    spy = Spy('', '', 0, 0.0,0)

    spy.name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")
    #to add the name
    if (spy.name).isalpha()== True:
        spy.salutation = raw_input("Should I call you Mr. or Ms.?: ")
        #to add the age
        spy.age = raw_input("What is your age?")
        spy.age = int(spy.age)
        if spy.age > 12 and spy.age < 50:
        #to add the rating
            spy.rating = raw_input("What is your spy rating?")
            spy.rating = float(spy.rating)
        #message according to the spy rating
            if spy.rating > 4.5:
                print 'Great ace!'
            elif spy.rating > 3.5 and spy.rating <= 4.5:
                print 'You are one of the good ones.'
            elif spy.rating >= 2.5 and spy.rating <= 3.5:
                print 'You can always do better'
            else:
                print 'We can always use somebody to help in the office.'
            start_chat(spy)
        else:
            print 'Sorry you do not fall in the correct age to be a spy'
    else:
        print 'Please add a valid spy name'
else:
    print "Wrong/Invalid input! The program will terminate now."