require 'net/http'
require 'uri'
require 'json'

uri = URI('https://coderbyte.com/api/challenges/json/age-counting')
response = Net::HTTP.get(uri)

json_data = JSON.parse(response)["data"]

full_array = json_data.split(", ")

counter = 0

full_array.each_slice(2) do |row|
  age = row[1].split("=")[1].to_i
  puts age
  counter += 1 if age >= 50
end



puts response
puts "---"
puts json_data
