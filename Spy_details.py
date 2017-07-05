from datetime import datetime
#spy class to reiterate the code
class Spy:

#constructor of the class to initialize the values
    def __init__(self, name, salutation, age, rating, word_count):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None
        self.word_count = word_count

#Second class for messaging
class ChatMessage:

    #Constructor of the class
    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me
#Predefined spy
spy = Spy('Holmes', 'Mr.', 24, 2.1,0)
#Predefined friends
friend_one = Spy('Baljinder', 'Mr.', 21, 2.7,0)
friend_two = Spy('Nimrat', 'Ms.', 18, 2.1,0)
friend_three = Spy('Severus', 'Prof.', 33, 3.7,0)
friend_four = Spy('Amritesh','Mr.', 21, 2.2,0)
friend_five = Spy('Elon','Mr.', 44, 4.4,0)

#adding our predefined friends to a list
friends = [friend_one, friend_two, friend_three]
