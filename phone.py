from phonenumbers import parse
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

phnum= input('insert phone number')

number= parse(phnum)

#print(geocoder.description_for_number(number,'en'))
print(carrier.name_for_number(number,'en'))
print(timezone.time_zones_for_number(number))
print(phnum)
