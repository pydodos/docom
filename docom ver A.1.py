import random
encouragement = ['      오늘 하루 정말 멋졌어요!', '      오늘도 수고했어요!', '      오늘 열심이었어요. 이제 푹 쉬어요.']
hello = ['      안녕하세요? 전 docom 이라고 해요.', '      인사해주어서 고마워요!', '      좋은 하루 보내세요~']
z = 100
print('docom ver a1. 2. 3 BY-CC-ND\n도움말을 원하시면 /help 또는 /? 를 입력하세요.')
while z == 100:
    a = (input('>>> '))
    if(a == '/?' or a == '/help'):
        print('      /hello - docom이 인사를 해줍니다.\n      /esc - 종료됩니다.\n      /plus -> ··· 더해지는 수 -> ··· 더하는 수 - 두 수가 더해집니다.\n      /minus -> ··· 빼지는 수 -> ··· 빼는 수 - 두 수가 빼집니다.\n      /plus. -> ··· 더해지는 수 -> ··· 더하는 수 - 두 수가 소숫점으로 더해집니다.\n      /minus. -> ··· 빼지는 수 -> ··· 빼는 수 - 두 수가 소숫점으로 빼집니다.\n      /encouragement - 오늘 하루에 대해 docom이 격려해줍니다.')
    elif(a == '/esc'):
        b = (input('      정말 종료하시겠습니까? (종료하지 않을려면 n를 누르세요.)\n· · · '))
        if (b == 'n'):continue
        else:break
    elif(a == '/hello'):
        b = random.choice(hello)
        print(b)
    elif(a == '/plus'):
        b = int(input('··· '))
        c = int(input('··· '))
        print('      %d + %d = %d' %(b, c, b + c))
    elif(a == '/minus'):
        b = int(input('··· '))
        c = int(input('··· '))
        print('      %d - %d = %d' %(b, c, b - c))
    elif(a == '/plus.'):
        b = float(input('· · · '))
        c = float(input('· · · '))
        print('      %f + %f = %f' %(b, c, b + c))
    elif(a == '/minus.'):
        b = float(input('··· '))
        c = float(input('··· '))
        print('      %f - %f = %f' %(b, c, b - c))
    elif(a == '/encouragement'):
        b = random.choice(encouragement)
        print(b)
    else:
        print('      error\n      명령어에 /를 포함했나요?\n      명령어의 철자가 맞나요?\n      간결화 명령어일 경우 뒤에 .을 붙였나요?\n      위가 하나도 지켜지지 않을 경우 오류가 납니다.\n      docom이 처음이라면 /?나 /help를 입력해 도움을 받으십시요.')
