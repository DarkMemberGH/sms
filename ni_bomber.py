import requests
import services

# colours
green     = '\033[92m'
cyan      = '\033[95m'
bold      = '\033[1m'
underline = '\033[4m'
end       = '\033[0m'
red       = '\033[91m'

# header
print(f"{green}{bold}\t\t{underline}║SMS Bomber Sri Lanka║{end}")

print()
print(f"{bold}Coded By{end}", end="")
print(f"{green}{bold} >> {end}", end="")
print(f"{cyan}{bold}nikait{end}")

print(f"{bold}twitter{end}", end="")
print(f"{green}{bold} >> {end}", end="")
print(f"{cyan}{bold}@aaanikit{end}")
print()

# inputs
print('enter the number without or with prefixes (+94)\nExample: 763097388')
input_number = input(green + bold + ">> " + end)
print('How Many SMS Send?')
sms = int(input(green + bold + ">> " + end))

print(f"you need a{cyan} tor {end}y/n? ")
is_tor = input(bold + green + ">> " + end)


def parse_number(number):
	msg = f"[*]check number - {green}{bold}OK{end}"
	if len(number) in (9, 10, 11):
		if number[0] == "7":
			number = number[1:]
			print(msg)
		elif number[:2] == "+94":
			number = number[2:]
			print(msg)
		elif int(len(number)) == 11 and number[0] == 9:
			print(msg)
	else:
		print(f"[*]check number - {red}{bold}failed number!{end}\nThis bomber is intended only for Russia and if the number you entered belongs to another country then alas this bomber is not suitable for you!")
		quit()
	return number
number = parse_number(input_number)

# tor
if str(is_tor) == "y":
        print(f"[*]launch {cyan}{bold}Tor{end}...")
        proxies = {
            'http': 'socks5://139.59.53.105:1080',
            'https': 'socks5://139.59.53.105:1080'
        }
        tor = requests.get('http://icanhazip.com/', proxies=proxies).text
        tor = (tor.replace('\n', ''))
        print(f"[*]launch {cyan}{bold}Tor{end} - {green}{bold}OK{end}")

services.attack(number, sms)
