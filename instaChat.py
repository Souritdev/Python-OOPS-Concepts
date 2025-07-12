class instaChat:
  def __init__(self):
    self.username = ''
    self.password = ''
    self.loggedIn = False
    self.menu()
    




  def menu(self):
    user_input = input("""Welcome to our instaChat 👋  !! How would You like to proceed further 🙂?
                       
                       1. Press 1 to signUp
                       2. Press 2 to signIn
                       3. Press 3 to write a post 
                       4. Press 4 to message a friend 
                       5. Press 5 to signOut
                       Enter Your Choice: """)
    if user_input == "1":
        self.signUp()
    elif user_input == "2":
        self.signIn()
    elif user_input == "3":
        self.my_post()
    elif user_input == "4":
        self.sendMessage()
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




  def my_post(self):
      if self.loggedIn == True:
         txt = input("What's On Your Mind 💭  , you can post here--->🥡")
         print(f"Your Content 🔎 has been posted---> {txt}")
      else:
         print("You need to sign in first to post something 📔 ")
      print("\n")
      self.menu()




  def sendMessage(self):
      if self.loggedIn == True:
         txt = input("Enter your message here : ")
         frnd = input("Whom you want to send the message? ")
         print(f"Your message has been delivered succesfully to your friend{frnd}")
      else:
         print("You need to sign in first to post something 📔 ")
      print("\n")
      self.menu()
         




object = instaChat()
