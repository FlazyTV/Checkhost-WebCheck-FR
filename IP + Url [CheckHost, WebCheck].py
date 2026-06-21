import webbrowser
import time

print("-------------------------- WEB/IP Analyzer --------------------------")
print("")
print("[URL] Attention a bien mettre .org / .net / .com et autres")
print("")

print("1) Check-host.net")
print("2) Web-check.xyz")
print("")

OptionCW = input("Choisissez une option : ")

if OptionCW == "1":
  
  print("")
  print("1) Url")
  print("2) IPv4")
  print("")
  OptionCheck = input("Choisissez une option : ")
  if OptionCheck == "1":
    print("")
    UrlCheck = input("Entrez votre url : ")
    if UrlCheck.isdigit():
      print("")
      print("Entrez une url valide.")
    elif len(UrlCheck) <= 5:
      print("")
      print("Entrez une url valide.")
    else:
      print("Redirecting to url with Check-Host...")
      time.sleep(0.5)
      webbrowser.open(f"check-host.net/check-http?host={UrlCheck}")
  elif OptionCheck == "2":
    print("")
    IPv4 = input("Entrez votre IPv4 : ")
    if len(IPv4) >= 16:
      print("")
      print("Entrez une ip valide.")
    elif len(IPv4) <= 6:
      print("")
      print("Entrez une ip valide.")
    else:
      print("Redirecting to ip with Check-Host...")
      time.sleep(0.5)
      webbrowser.open(f"check-host.net/ip-info?host={IPv4}")
  else:
    print("Ce n'est pas une option valide.")

elif OptionCW == "2":
  print("")
  print("1) Url")
  print("")
  OptionWeb = input("Choisissez une option : ")
  if OptionWeb == "1":
    print("")
    UrlWeb = input("Entrez une url : ")
    if UrlWeb.isdigit():
      print("Entrez une url valide.")
    elif len(UrlWeb) <= 5:
      print("Entrez une url valide.")
    else:
      print("Redirecting to url with Web-Check...")
      time.sleep(0.5)
      webbrowser.open(f"https://web-check.xyz/check/{UrlWeb}")
  
else:
  print("Veuillez choisir une option valide.")
