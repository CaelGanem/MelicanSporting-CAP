class isadmin:
  def isadmin(name, code):
    name = (str(name))
    code = (str(code))
    name = name.lower()
    with open('data/blacklist.txt') as f:
      blacklist = f.read()
    blacklist = (blacklist.split(", "))
    with open('data/admin.txt') as f:
      admin = f.read()
    admin = (admin.split(", "))
    with open("templates/demo/logs.txt") as f:
      oldlogs = f.read()

    if name in admin:
      if name in blacklist:
        response = ('You have a valid admin id, but are blacklisted')
        with open ('templates/demo/logs.txt', 'w') as f:
          f.write(name + ' was delined access to admin (blacklist)\n' + oldlogs)
      else:
        response = ("Logged into admin!")
        with open ('templates/demo/logs.txt', 'w') as f:
          f.write(name + ' was given access to admin\n' + oldlogs)
    else:
      response = ("Sorry, you can't access this admin resourse!")
      with open ('templates/demo/logs.txt', 'w') as f:
        f.write(name + ' was declined access to admin\n' + oldlogs)

    with open('data/response.txt', 'w') as f:
      f.write(response)