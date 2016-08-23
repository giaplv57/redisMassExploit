import requests
import re

def getAuthCookies(username, password):
    url = 'https://account.shodan.io/login'
    data = {'username': username, 'password': password, 'grant_type': 'password', 'login_submit': 'Log in'}
    session = requests.Session()
    response = session.post(url, data = data)
    return session.cookies.get_dict()

redisVersions = [':2.0', ':2.1', ':2.2', ':2.3', ':2.4', ':2.5', ':2.6', ':2.7', ':2.8', ':2.9', ':3.0', ':3.1', ':3.2', ':', '']
countryList = ['AF', 'AL', 'DZ', 'AS', 'AD', 'AO', 'AI', 'AQ', 'AG', 'AR', 'AM', 'AW', 'AU', 'AT', 'AZ', 'BS', 'BH', 'BD', 'BB', 'BY', 'BE', 'BZ', 'BJ', 'BM', 'BT', 'BO', 'BQ', 'BA', 'BW', 'BV', 'BR', 'IO', 'BN', 'BG', 'BF', 'BI', 'KH', 'CM', 'CA', 'CV', 'KY', 'CF', 'TD', 'CL', 'CN', 'CX', 'CC', 'CO', 'KM', 'CG', 'CD', 'CK', 'CR', 'HR', 'CU', 'CW', 'CY', 'CZ', 'CI', 'DK', 'DJ', 'DM', 'DO', 'EC', 'EG', 'SV', 'GQ', 'ER', 'EE', 'ET', 'FK', 'FO', 'FJ', 'FI', 'FR', 'GF', 'PF', 'TF', 'GA', 'GM', 'GE', 'DE', 'GH', 'GI', 'GR', 'GL', 'GD', 'GP', 'GU', 'GT', 'GG', 'GN', 'GW', 'GY', 'HT', 'HM', 'VA', 'HN', 'HK', 'HU', 'IS', 'IN', 'ID', 'IR', 'IQ', 'IE', 'IM', 'IL', 'IT', 'JM', 'JP', 'JE', 'JO', 'KZ', 'KE', 'KI', 'KP', 'KR', 'KW', 'KG', 'LA', 'LV', 'LB', 'LS', 'LR', 'LY', 'LI', 'LT', 'LU', 'MO', 'MK', 'MG', 'MW', 'MY', 'MV', 'ML', 'MT', 'MH', 'MQ', 'MR', 'MU', 'YT', 'MX', 'FM', 'MD', 'MC', 'MN', 'ME', 'MS', 'MA', 'MZ', 'MM', 'NA', 'NR', 'NP', 'NL', 'NC', 'NZ', 'NI', 'NE', 'NG', 'NU', 'NF', 'MP', 'NO', 'OM', 'PK', 'PW', 'PS', 'PA', 'PG', 'PY', 'PE', 'PH', 'PN', 'PL', 'PT', 'PR', 'QA', 'RO', 'RU', 'RW', 'RE', 'BL', 'SH', 'KN', 'LC', 'MF', 'PM', 'VC', 'WS', 'SM', 'ST', 'SA', 'SN', 'RS', 'SC', 'SL', 'SG', 'SX', 'SK', 'SI', 'SB', 'SO', 'ZA', 'GS', 'SS', 'ES', 'LK', 'SD', 'SR', 'SJ', 'SZ', 'SE', 'CH', 'SY', 'TW', 'TJ', 'TZ', 'TH', 'TL', 'TG', 'TK', 'TO', 'TT', 'TN', 'TR', 'TM', 'TC', 'TV', 'UG', 'UA', 'AE', 'GB', 'US', 'UM', 'UY', 'UZ', 'VU', 'VE', 'VN', 'VG', 'VI', 'WF', 'EH', 'YE', 'ZM', 'ZW', 'AX']
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'}

username = raw_input("YOUR SHODAN ACCOUNT USERNAME: ")
password = raw_input("YOUR SHODAN ACCOUNT PASSWORD: ")
cookies = getAuthCookies(username, password)
worldIPList = []

for redisVersion in redisVersions:
    print '------------------LOOKING FOR REDIS VERSION {0}------------------'.format(redisVersion)
    for country in countryList:
        for page in range(1,6):
            url = 'https://www.shodan.io/search?query=redis_version{0} country:"{1}"&page={2}'.format(redisVersion, country, page)
            r = requests.get(url, headers=headers,  cookies=cookies)
            content = r.text

            countryIPList = re.findall(r'<a href="/host/([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})">', content)
            if countryIPList == []:
                print 'Not found any IP in {0} at page {1}'.format(country, page)
                break
            else:
                print countryIPList
                print 'Found {0} IP from {1} in page {2}'.format(len(countryIPList), country, page)
                for IP in countryIPList:
                    if IP not in worldIPList:
                        worldIPList.append(IP)
                print 'Total number of IP: {0}'.format(len(worldIPList))
    print 'WORLD IP NUMBER AFTER FINDING REDIS VERSION {0}'.format(len(redisVersion))
    print worldIPList
    print '------------------LOOKING FOR REDIS VERSION {0}------------------'.format(redisVersion)
print worldIPList