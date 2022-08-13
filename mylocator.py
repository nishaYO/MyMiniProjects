# this code will parse the country code and the phone number
# and will provide the country name and the service provider name.

import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier


Ph_no = input('enter the phone number here(along with the country code ):')
number = phonenumbers.parse(Ph_no)
print(number)

country = geocoder.description_for_number(number, lang="en")
print(f"Country: {country}")

service_provider = carrier.name_for_number(number, "en")
print(f"Service Provider: {service_provider}")
