import pandas
raw_data = pandas.read_csv("/Users/aaronforbes/for-date-science/raw_data/fiscal_decentralization/time_series.csv", delimiter = ',')
new_data = raw_data.rename(columns = {"Country Name":"country_name", ## easier to read
                              "Country Code": "country_code",
                                  "Indicator Name": "indicator_name",
                                  "Indicator Code": "indicator_code",
                                  "Sector Name": "sector_name",
                                  "Sector Code": "sector_code",
                                  "Attribute": "attribute"})
filtered_data = new_data.dropna(axis='columns', how='all').dropna(axis=1, how='all') ## remove null columns

def output_json(): # output json
    contents = json.dumps([row for row in filtered_data], indent=4)
    with open('filtered_data.json', 'w') as file:
        file.write(contents)

def output_csv(): # output csv
    contents = csv.dumps([row for row in filtered_data], indent=4)
    with open('filtered_data.json', 'w') as file:
        file.write(contents)

# df.to_csv(filtered_data, sep=',', encoding='utf-8')
# df.to_json(filtered_data, sep=',', encoding='utf-8')
# df.to_xlm(filtered_data, sep=',', encoding='utf-8')

def output_xml(): # output xml
    xml = ['<?xml version="1.0" encoding="UTF-8"?>']

# TODO: need to customize for specific data

    # xml.append('<banks>')
    # for row in reader:
    #     xml.append('<bank>')
    #     for k, v in row.items():
    #         xml.append('    <{}>{}</{}>'.format(k, v, k))
    #     xml.append('</bank>')
    # xml.append('<banks>')

    with open('filtered_data.xml', 'w') as file:
        file.write('\n'.join(xml))

# use the below for statistics on fiscal_decentralization

# def bank_deposits():
#     deposits = {}
#
#     for row in reader:
#         if row['NAMEFULL'] not in deposits:
#             deposits[row['NAMEFULL']] = 0
#         deposits[row['NAMEFULL']] += int(row['DEPSUM'].replace(',', ''))
#
#     deplist = []
#
#     for k, v in deposits.items():
#         deplist.append({
#             'name': k,
#             'deposits': v
#         })
#
#     deplist.sort(key=lambda k: k['deposits'])
#
#     pprint(deplist)

print('[1] output as json')
print('[2] output as csv')
print('[3] output as xml')
# min of fiscal_decentralization
# max of fiscal_decentralization

# print('[4] total deposits')
# print('[5] bank deposits')
print('')

try:
    choice = int(input('Pick output '))
except:
    print('bad choice')

if choice == 1:
    output_json()
if choice == 2:
    output_csv()
if choice == 3
    output_xml
# if choice == 3:
#     total_deposits()
# if choice == 4:
#     bank_deposits()
# print(filtered_data   <-- original print for testing
