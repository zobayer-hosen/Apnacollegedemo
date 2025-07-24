import phonenumbers
from phonenumbers import geocoder

number = phonenumbers.parse("+1-555-0123")
location = geocoder.description_for_number(number, "en")
print(location)

