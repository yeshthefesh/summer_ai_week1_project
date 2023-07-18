#Various import Statements can go here
from  social_network_classes import SocialNetwork,Person
import social_network_ui



#Create instance of main social network object
ai_social_network = SocialNetwork()

#The line below is a python keyword to specify which 
if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    last_menu = None
    choice = social_network_ui.mainMenu()
    accessed = False

    while True: 
        if choice == "1":
            print("\nYou are now in the create account menu")
            ai_social_network.create_account()

        elif choice == "2":
            inner_menu_choice = social_network_ui.manageAccountMenu()
            #Handle inner menu here
            while True:
                if inner_menu_choice == "7":
                    break
                else:
                    inner_menu_choice = social_network_ui.manageAccountMenu()
                    if inner_menu_choice == "1":
                        if not accessed:
                            print("You have to access an account first.")
                            break
                        print("Your current account details:")
                        print("Name: ",current_account.id)
                        print("Age: ",current_account.year)
                        current_account.id = input("New name: ")
                        current_account.year = input("New age: ")
                    elif inner_menu_choice == "2":
                        if not accessed:
                            print("You have to access an account first.")
                            break
                        current_account.add_friend(ai_social_network)
                    elif inner_menu_choice == "3":
                        if not accessed:
                            print("You have to access an account first.")
                            break
                        print("Your friends are:")
                        for friend in current_account.friendlist:
                            print(friend.id)
                    elif inner_menu_choice == "4":
                        if not accessed:
                            print("You have to access an account first.")
                            break
                        current_account.send_message(current_account)
                    elif inner_menu_choice == "5":
                        if not accessed:
                            print("You have to access an account first.")
                            break
                        print("Your messages:")
                        for message in current_account.messages:
                            print(message)
                    elif inner_menu_choice == "6":
                        current_account.block(ai_social_network)

        elif choice == "3":
            current_account = ai_social_network.access_account()
            accessed = True

        elif choice == "4":
            print("Thank you for visiting. Goodbye.")
            break

        else:
            print("Your input is invalid. Try Again!")
        
        #restart menu
        choice = social_network_ui.mainMenu()



        
