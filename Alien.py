userNames = ['nam', 'hoang', 'tien', 'quan', 'admin']
for user in userNames:
    if user == 'admin':
        print('Hello admin, Would you like to see a status report ?')
    else:
        print(f'Hello {user}, thank you for logging in again')

if len(userNames) == 0:
    print('We need to find some users')

userNames.clear()
if not userNames:
    print('We need to find some users')

current_users = ['nam', 'hoang', 'tien', 'QUAn', 'hoa']
new_users = ['hoa', 'linh', 'HUonNG', 'anh', 'vu']

for current_user in current_users:
    current_user = current_user.lower()

for new_user in new_users:
    if new_user.lower() in current_users:
        print('da ton tai')
    else:
        print('OK')


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number == 1:
        print('1st')
    elif number == 2:
        print('2nd')
    elif number == 3:
        print('3rd')
    else:
        print(f'{number}th')