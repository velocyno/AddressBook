container = ['Address was successfully created.', 'First name:', 'Andrii', 'Last name:', 'AQA', 'Street Address:',
             'Street', 'Secondary Address:', 'Street2', 'City:', 'Lviv', 'State:', 'AK', 'Zip code:', '79000',
             'Country:', 'us', 'Birthday:', '6/11/1985', 'Color:', 'Age:', '35', 'Website:', 'https://www.site.com',
             'Phone:', '123456', 'Climbing?', 'Yes', 'Dancing?', 'Yes', 'Reading?', 'Yes', 'Note:', 'Test note',
             'Edit', '  |  ', 'List']

# j = 0
# for i in container:
#     print(f'{j}: {i}')
#     j += 1
#
# def hex_to_rgb(value):
#     value = value.lstrip('#')
#     lv = len(value)
#     return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
#
# hex = "#00FF33"
# rgb = (0, 255, 51)
#
# print(hex_to_rgb(hex))
#
# def rgb_to_hex(rgb):
#     return '#%02x%02x%02x' % rgb
#
# print(rgb_to_hex((0, 255, 51)))

# from pages.adresses_object import Converters

# converter = Converters()
# # print(converter.rgb_to_hex((0, 255, 51)))

lr = {
    'First name:': 'Andrii',
    'Last name:': 'AQA',
    'Street Address:': 'Street',
    'Secondary Address:': 'Street2',
    'City:': 'Lviv',
    'State:': 'AK',
    'Zip code:': '79000',
    'Country:': 'us',
    'Birthday:': '6/11/1985',
    'Color:': (0, 255, 51),
    'Age:': '35',
    'Website:': 'https://www.site.com',
    'Phone:': '123456',
    'Climbing?': 'Yes',
    'Dancing?': 'Yes',
    'Reading?': 'Yes',
    'Note:': 'Test note'
}
print(lr['Age:'])

# date = "6/11/1985"
#
# mm, dd, yyyy = date.split('/')
# print(f'{dd}/{mm}/{yyyy}')

d1 = {'First name:': 'Andrii2',
      'Last name:': 'AQA2',
      'Street Address:': 'Street2',
      'Secondary Address:': 'Street22',
      'City:': 'Lviv2',
      'State:': 'AZ',
      'Zip code:': '790002',
      'Country:': 'canada',
      'Birthday:': '6/12/1985',
      'Color:': (0, 123, 26),
      'Age:': '36',
      'Website:': 'https://www.site2.com',
      'Phone:': '1234562',
      'Climbing?': 'No',
      'Dancing?': 'No',
      'Reading?': 'No',
      'Note:': 'Test note2'}

