d2 = {'First name:': 'Andrii2',
      'Last name:': 'AQA2',
      'Street Address:': 'Street2',
      'Secondary Address:': 'Street22',
      'City:': 'Lviv2',
      'State:': 'AZ',
      'Zip code:': '790002',
      'Country:': 'canada',
      'Birthday:': '6/12/1985',
      'Color:': '(0, 123, 26);',
      'Age:': '36',
      'Website:': 'https://www.site2.com',
      'Phone:': '123-4562',
      'Climbing?': 'No',
      'Dancing?': 'No',
      'Reading?': 'No',
      'Note:': 'Test note2'}

v = "(25, 150, 245)"
tlv = []
lv = v[1:-1].split(", ")
for el in lv:
      tlv.append(int(el))
ttlv = tuple(tlv)
# lv = tuple(v)
print(ttlv)
print(type(ttlv))