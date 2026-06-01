from address import Address
from mailing import Mailing

address = Address('40065', "Volgograd", "Lenina", '109', '56')
from_address = Address('400125', "Moscou", "Kirova", '23', '155')
mailing = Mailing(address, from_address, '787', '43587677')

print(mailing)
