class isvalid:
  def isvalid(name, code):
    name = (str(name))
    code = (str(code))
    name = name.lower()
    with open('data/accepted.txt') as f:
      accepted = f.read()
    accepted = (accepted.split(", "))
    with open('data/blacklist.txt') as f:
      blacklist = f.read()
    blacklist = (blacklist.split(", "))
    with open('data/admin.txt') as f:
      admin = f.read()
    admin = (admin.split(", "))
    with open("templates/demo/logs.txt") as f:
      oldlogs = f.read()

    if name in accepted:
      if name in blacklist:
        response = ('You have a valid id, but are blacklisted')
        with open ('templates/demo/logs.txt', 'w') as f:
          f.write(name + ' was delined access (blacklist)\n' + oldlogs)
      else:
        response = ("Accepted!")
        with open ('templates/demo/logs.txt', 'w') as f:
          f.write(name + ' was given access\n' + oldlogs)
    else:
      response = ("Sorry, you can't access this")
      with open ('templates/demo/logs.txt', 'w') as f:
        f.write(name + ' was declined access\n' + oldlogs)

    with open('data/response.txt', 'w') as f:
      f.write(response)