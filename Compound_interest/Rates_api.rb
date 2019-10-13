require 'rubygems'
require 'savon'
require 'pp'

url = "http://www.xignite.com/xRates.asmx?WSDL"

soap_header = {
     "Header" => {
          "@xmlns" => "http://www.xignite.com/services/",
          "Username" => "YOUR_TOKEN"
          }
     }

client = Savon.client(wsdl: url, :soap_header => soap_header, convert_request_keys_to: :none, env_namespace: 'soap')

response = client.call(:list_rates, message: {
     "@xmlns" => "http://www.xignite.com/services/",

})

pp response.to_hash

# https://www.xignite.com/Product/global-interest-rates#/DeveloperResources/Code/ListRates
