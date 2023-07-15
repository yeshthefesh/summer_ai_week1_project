# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk
class SocialNetwork:
    def __init__(self):
        self.list_of_people = [] # this instance variable is initialized to an empty list when social network is created, 
                                 # you can save objects of people on the network in this list
        
    ## For more challenge try this
    def save_social_media(self):
        # function to save social media to a file on disk 
        # hint: look up how to use python's inbuil json module to turn objects to json
        # you can write this json unto a file on disk
        pass

    ## For more challenge try this
    def reload_social_media(self):
        # function to load saved social media from file on disk 
        # hint: load a the json file from disk and look up how to recreate the list of people objects.
        pass

    def  create_account(self):
        #implement function that creates account here
        print("Creating ...")
        name = input("What is your name?\n")
        age = input("How old are you?\n")
        self.list_of_people.append(Person(name,age))

    def access_account(self):
        if len(self.list_of_people) > 0:
            print("The accounts that you can access are:")
            for i,account in enumerate(self.list_of_people):
                print(i+1,account.id)
            choice = input("Which account would you like to access? (choose a number): ")
            if int(choice)-1 in range(len(self.list_of_people)):
                current_account = self.list_of_people[int(choice)-1]
                print("You are now accessing",str(current_account.id))
            else:
                print("The account you have chosen is not one of the ones listed.")
        else:
            print("You have not created any accounts yet.")
        return current_account

class Person:
    def __init__(self, name, age):
        self.id = name
        self.year = age
        self.friendlist = []
        self.messages = []

    def add_friend(self,network):
        print("List of users:")
        for i,user in enumerate(network.list_of_people):
            print(i+1,user.id)
        chosen = input("Who would you like to add?\n")
        new_friend = network.list_of_people[int(chosen)-1]
        if new_friend in self.friendlist:
            print("That person is already your friend.")
        elif new_friend == self:
            print("You cannot add yourself.")
        else:
            self.friendlist.append(new_friend)
            print(f"You have added {new_friend.id}.")

    def send_message(self,current_account):
        print("List of friends:")
        for i,friend in enumerate(self.friendlist):
            print(i+1,friend.id)
        chosen = input("Who would you like to send a message to?\n")
        message = input("What is your message?\n")
        self.friendlist[int(chosen)-1].messages.append(current_account.id+": "+message)
        print("You have sent a message to",self.friendlist[int(chosen)-1].id)
