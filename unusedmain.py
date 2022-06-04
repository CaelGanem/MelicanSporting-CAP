
while running == 1:
  with open('data/accepted.txt') as f:
    accepted = f.read()
  accepted = (accepted.split(", "))
  with open('data/blacklist.txt') as f:
    blacklist = f.read()
  blacklist = (blacklist.split(", "))
  with open('data/admin.txt') as f:
    admin = f.read()
  admin = (admin.split(", "))

  print('What do you want to do?\n1. Get a ball\n2. return a ball\n3. admin')
  choice = input('')
  with open('templates/logs.txt') as f:
      oldlogs = f.read()
      oldlogs = (str(oldlogs))

    
  if choice == ('1'):
    print('What is your name?')
    name = input('')
    clearConsole()

    
    if name in accepted:
      if name in blacklist:
        print('You have a valid id, but are blacklisted')
        with open ('templates/logs.txt', 'w') as f:
          f.write(name + ' was delined access (blacklist)\n' + oldlogs)
      else:
        print("Accepted!")
        with open ('templates/logs.txt', 'w') as f:
          f.write(name + ' was given access\n' + oldlogs)
    else:
      print("Sorry, you can't access this")
      with open ('templates/logs.txt', 'w') as f:
        f.write(name + ' was declined access\n' + oldlogs)

  elif choice == ('2'):
    print('What is your name?')
    name = input('')
    clearConsole()
    print('Please insert your ball into the slot.')
    with open ('templates/logs.txt', 'w') as f:
        f.write(name + ' returned their ball\n' + oldlogs)

  elif choice == ('3'):
    print('What is your name?')
    name = input('')

    if name in admin:
      adminhome = 1
      while adminhome == 1:
        clearConsole()
        print('Admin page')
        with open ('templates/logs.txt', 'w') as f:
          f.write(name + ' opened the admin page\n' + oldlogs)
        print('1. work in progress\n2. exit admin page')
        adminchoice = input('')
        if adminchoice == ('2'):
          adminhome = 0
          clearConsole()
        if adminchoice == ('1'):
          clearConsole()
          print('Work in progress')
          adminhome = 0
    else:
      clearConsole()
      print('You do not have access to this!')
      with open ('templates/logs.txt', 'w') as f:
        f.write(name + ' was blocked from opening the admin page\n' + oldlogs)