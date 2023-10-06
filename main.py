# Login authenticator project by Keith Poncardas 2023

# import os is not compatible in mobile compiler
import os

user_data_array = [
  {"username": "user1", "password": "password1"}
]

def save_user_data (username, password, array_of_data):
  user_data = {
    "username": username,
    "password": password
  }
  array_of_data.append(user_data)

def check_credentials (username, password, array_of_data):
  for user_data in array_of_data:
    if user_data["username"] == username and user_data["password"] == password:
      print("✅ LOGGED IN SUCCESSFULY! ✅")
      return True
  os.system('cls')
  print("❌ INVALID CREDENTIALS, TRY AGAIN ❌")
  return False

def is_username_exist (input_username, user_data_array):
  for check_usn in user_data_array:
    if check_usn["username"] == input_username:
      print(f"🚫 USERNAME '{input_username}' ALREADY EXIST, TRY AGAIN 🚫")
      return True
  return False

def check_exit (input):
  if input.strip().lower() == 'exit' or input.strip().lower() == "3":
    os.system('cls')
    print("❎ EXIT ❎")
    return True
  return False

def login_func ():
  loop_usn = True
  re_loop = False
  while not re_loop:
    while loop_usn:
      username_input = input("ENTER USERNAME :")
      if username_input.strip() == "":
        os.system('cls')
        print("NO (USN) INPUT, TRY AGAIN")
      elif check_exit(username_input):
        loop_usn = False
        re_loop = not False
      else:
        loop_usn = True
        break
    while loop_usn:
        password_input = input("ENTER PASSWORD :")
        if password_input.strip() == "":
          os.system('cls')
          print("NO (PASS) INPUT, TRY AGAIN")
        elif check_exit(password_input):
          loop_usn = False
          re_loop = not False
        else:
          loop_usn = True
          break
    if loop_usn:
      os.system('cls')
      validate = check_credentials(username_input, password_input, user_data_array)
      re_loop = validate

def signup_func ():
  main_loop = False
  sub_loop = True
  while not main_loop:
    while sub_loop:
      create_username = input("CREATE USERNAME :")
      if create_username.strip() == "":
        os.system('cls')
        print("NO INPUT, TRY AGAIN")
      elif check_exit(create_username):
        main_loop = not False
        sub_loop = not True
      elif is_username_exist(create_username, user_data_array):
        os.system('cls')
      else:
        break
    while sub_loop:
      create_password = input("CREATE PASSWORD :")
      if (create_password.strip() == ""):
        os.system('cls')
        print("NO INPUT, TRY AGAIN")
      elif check_exit(create_password):
        main_loop = not False
        sub_loop = not True
      elif len(create_password) < 5:
        os.system('cls')
        print("🤏 YOUR PASSWORD IS TOO LITTLE, TRY AGAIN 🤏")
      else:
        break
    if sub_loop:
      os.system('cls')
      save_user_data(create_username, create_password, user_data_array)
      print("✅ SIGNED IN SUCCESSFULY! ✅")
      login_func()
      main_loop = not False

loop_count = 1

while True:
  print("⏬ CHOOSE A NUMBER OPTION BELOW ⏬")
  print("[1] LOGIN")
  print("[2] SIGN UP")
  print("[3] EXIT")

  choice = input("ENTER THE NUMBER OF YOUR CHOICE :")

  isInvalid = False

  if choice == "1" or choice.strip().lower() == "login":
    os.system('cls')
    login_func()
    break
  elif choice == "2" or choice.strip().lower() == "signup":
    os.system('cls')
    signup_func()
    break
  elif choice == "3" or choice.strip().lower() == "exit":
    os.system('cls')
    check_exit(choice)
    break
  else:
    isInvalid = True

  if isInvalid:
    if choice.strip() == "":
      os.system('cls')
      print(f"❌ NO INPUT, OVERALL ATTEMPT COUNT {loop_count} ❌")
      loop_count += 1
    else:
      os.system('cls')
      print(f"❌ INVALID INPUT, OVERALL ATTEMPT COUNT {loop_count} ❌")
      loop_count += 1
