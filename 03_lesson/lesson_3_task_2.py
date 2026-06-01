from smartphone import Smartphone

catalog = [
   Smartphone("IPhone", "IPhone 17 Pro", '+7 906 774 88 45'),
   Smartphone("Samsung", "Galaxy Note", '+7 988 234 57 77'),
   Smartphone("Honor", "Honor 600 Lite", '+7 917 545 66 34')
     ]

for smartphone in catalog:
    print(f"{smartphone.brend} - {smartphone.model}. {smartphone.number}")
