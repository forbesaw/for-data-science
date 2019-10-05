import pandas
data = pandas.read_csv("/Users/aaronforbes/for-date-science/raw_data/fiscal_decentralization/time_series.csv", delimiter = ',')
new_data = data.rename(columns = {"Country Name":"country_name", ## easier to read
                              "Country Code": "country_code",
                                  "Indicator Name": "indicator_name",
                                  "Indicator Code": "indicator_code",
                                  "Sector Name": "sector_name",
                                  "Sector Code": "sector_code",
                                  "Attribute": "attribute"})
filtered_data = new_data.dropna(axis='columns', how='all').dropna(axis=1, how='all') ## remove null columns 
print(filtered_data)
