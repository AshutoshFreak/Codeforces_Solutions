t = int(input())
for i in range(t):
    word = input()
    if word[-2:] == 'po':
        print('FILIPINO')
    elif word[-4:] == 'desu' or word[-4:] == 'masu':
        print('JAPANESE')
    else:
        print('KOREAN')
