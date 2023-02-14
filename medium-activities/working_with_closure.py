def salute(salutation):
  def person(nome):
      return f"{salutation}, {nome}!"
  return person

morning = salute('Good Morning')
night = salute('Good Night')
name = input('Type your name: ')
print(morning(name))
print(night(name))
