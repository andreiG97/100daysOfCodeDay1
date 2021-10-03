# print('''     ,-.
#                      `\ `.
#                       (`- `.
#            __          `c.- \
#           (_ `---..__   `\"_ \
#             `(`-.__  `-._ (_c |
#               `--.____ ( `,-  | |/
#                   `---(___| ,---/         ,.
#                     ,-;::,'|_/\-|       ,' /
#             _.._    ||   `-'\@/@|_      | ||-.
#     _.--.--'    `-. \`--/,-._/    `\_,--',/|,-\
#   .',- _     _.__  `-:_|/   (      /      )|-'|
#  /_/_,;-  ,-'    `-._ _)_,-,-,___,'---'\___.-'
#  |___,,.  | _    _.-'' ((_{_// /
#  \.-'  | (-' \.-'       `---'`'
#     ,-'\__>  /|         /
#   .',-'/|.   \ \        |
#  / / _|``.`.  `/\_     /|  ,,.
# /  \  |  |  `-.`(_),. /((((   )
# |   `--\ `.`=. `-._`'|__|  `''
# |  ,'  |`-|   T``'',----.
# |      |  `.__|-,-',----.|
# \     / ,-' _,-;,-'      |
#  `---'  | ,;-''       _,'
#         `//       _,-'
# hjm      \____.-''
# ''')
#
# print('Welcome to Rome\n' + 'Your quest is to find the magic potion')
# first_move = input('Where should we go Obelix ? To the left or to the right ? ')
#
# if first_move == 'left':
#     print('You entered a dark alley ')
# else:
#     print('The romans found you ')
#
# second_move = input('You see a strange man. Do you talk to him ? ')
# if second_move == 'yes' or second_move == 'Yes':
#     print('By Toutatis you found one of the Getafix\'s teachers. He will make you the magic potion and you will escpae from Rome')
# else:
#     print('While you were searching the romans send you to prison')

print('You are having a drink with a friend tonight and you don\'t know what to wear')
choice = input('Do you feel sexy ? Yes or No\n')
if choice.lower() == 'yes':
    print('You decide to wear a black, short dress')
else:
    print('You just dress casually')

print('''
    Your friend arrives and after small talk you open a bottle of wine.You know you shouldn't be
     drinking to much so you have to decide how many glasses of wine you should have.
''')
choice1 = int(input('1 or 2\n '))
if choice1 == 1:
    print('You have a nice evening and a good laugh')
else:
    print('After your second drink he tries to kiss you')
    choice2 = input('Not sure if you should stop this or go for it. "Stop it", or just kiss him back\n')
    if choice2.lower() == 'stop it':
        print('You send him home and go to sleep')
    else:
        print('You get on his lap and as you press your lips harder and harder he tries to reach under your dress')
        choice3 = input('Should you let him continue ? Yes or no\n')
        if choice3.lower() == 'no':
            print('You just kiss for a while and then stop')
        else:
            print('''
            While he is almost there he stops and takes you off his lap. 
            He then stands up and turns you with your back onto him while kissing 
            your neck. You feel his hand going down again and you are still not 
            sure what to do''')
