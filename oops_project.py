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
                       5. Press 5 to exit
                       Enter Your Choice: """)
    if user_input == "1":
        self.signUp()
    elif user_input == "2":
        self.signIn()
    elif user_input == "3":
        pass
    elif user_input == "4":
        pass
    else:
       exit()



  def signUp(self):
     email = input("Enter a valid email-address --> ")
     password = input("Enter a strong password ---> ")
     self.username = email
     self.password = password
     print("🎉 --> Boom , You have been signed In succesfully")
     print("\n")
     self.menu()


  def signIn(self):
      if self.username == '' and self.password == '':
        print("Please signIn first by pressing 1 from the main menu")
      else:
        uname = input("Enter your username / email-address here: ")
        pwrd = input("Enter the password here: ")
        if self.username == uname and self.password == pwrd:
           print("🎉 --> Boom , You have been signed In succesfully")
           self.loggedIn = True
        else:
           print(".......Please Enter valid credentials.....")
      print("\n")
      self.menu()



  


object = instaChat()
