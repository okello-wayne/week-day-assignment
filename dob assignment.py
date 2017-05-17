import calendar
year=int(input('Enter year of birth:'))
month=int(input('Enter month of birth(1-12):'))
day=int(input('Enter day of birth:(1-31)'))

dob= calendar.weekday(year,month,day)
d=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']




print('You are blessed to be born on','***', d[dob],'***')

print('By OKELLO WAYNE STEVEN 15/U/12008/PS')

