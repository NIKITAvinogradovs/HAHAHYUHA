text = input("Ievadi teikumu; ")
if text.count("e")>0:
  text = text.replace("e", " ")
  text = text.upper()
  print (text)
else:
  t = "TEKSTA NAV VAJADZIGS BURTS!!!!!"
  print (t)


