# -*- coding: utf-8 -*-
'''
Edited by: [𝐙𝐄𝐑𝟘.𝟙𝐍𝐍]
'''

from requests import get
from time import sleep

def ipTrack(ip):
    response = get(f'http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query')
    data = response.json()

    while True:
        if 'message' in data:
            print('\nIP inválido ou não existente. \nEx.: [ 123.456.789.000 ]\n')
            break
        else:
            print()
            print('='*28)
            print(f'IP to Track: {data["query"]}')
            print('='*28)
            print(f'Continent: {data["continent"]}')
            print(f'Country: {data["country"]}')
            print(f'Country Code: {data["countryCode"]}')
            print(f'State: {data["regionName"]}')
            print(f'City: {data["city"]}')
            print(f'Latitude: {data["lat"]}')
            print(f'Longitude: {data["lon"]}')
            print(f'Timezone: {data["timezone"]}')
            print(f'Provider: {data["isp"]}\n')
            sleep(2)
            break

print('\nCoded by f4ll_py')
print('\nVersion: 0.1')
print('''
██╗██████╗ ████████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║██████╔╝   ██║   ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
██║██╔═══╝    ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║██║        ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
╚═╝╚═╝        ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ 
''')

while True:
    try:
        ip = str(input('\nEnter the IP (w/ dots | 0 to quit): '))
        if ip == '0':
            print('\nCoded by f4ll_py\n')
            sleep(0.5)
            break
        else:
            ipTrack(ip)
    except(KeyboardInterrupt):
        print('\n\nCoded by f4ll_py\n')
        sleep(0.5)
        break
