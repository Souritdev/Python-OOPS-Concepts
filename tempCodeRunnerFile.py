class instaChat:
  def __init__(self):
    self.username = ''
    self.password = ''
    self.loggedIn = False
    self.menu()
    

  def menu(self):
    user_input = input("""Welcome to our instaChat 👋  !! How would You like to proceed further 🙂?
                       1. Press 1 to signUp
                       2. Press 2 to signOut
                       3. Press 3 to write a post 
                       4. Press 4 to message a friend 
                       5. Press 5 to exit""")
    if user_input == "1":
        self.signUp()
    elif user_input == "2":
        pass
    elif user_input == "3":
        pass
    elif user_input == "4":
        pass
    else:
       exit()



  def signUp(self):
     email = input("Enter a valid email-address:--> ")
     password = input("Enter a strong password:---> ")
     self.username = email
     self.password = password
     print("🎉 --> Boom , You have been signed In succesfully")
     print("\n")
     self.menu()


object = instaChat()

    