#-*- coding: utf-8 -*-
import os
path = os.environ['PATH']
new_path = 'C:\\Python38\\tcl\\Python38\\lib\\;' + path
os.environ['PATH'] = new_path
import random as random_
import turtle as tu
a = 0
b = 0
c = 0
d = 0
e = 0
m = 0
encouragement = ['      오늘 하루 정말 멋졌어요!', '      오늘도 수고했어요!', '      오늘 열심이었어요. 이제 푹 쉬어요.']
hello = ['      안녕하세요? 전 docom 이라고 해요.', '      인사해주어서 고마워요!', '      좋은 하루 보내세요~']
random = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
z = 100
print('docom ver a2. 2. 4\n도움말을 원하시면 /help 또는 /? 를 입력하세요.')
while z == 100:
    a = (input('>>> '))
    if(a == '/?' or a == '/help'):
        print('      /hello - docom이 인사를 해줍니다.\n      /esc - 종료됩니다.\n      /plus -> ··· 더해지는 수 -> ··· 더하는 수 - 두 수가 더해집니다.\n      /minus -> ··· 빼지는 수 -> ··· 빼는 수 - 두 수가 빼집니다.\n      /plus. -> ··· 더해지는 수 -> ··· 더하는 수 - 두 수가 소숫점으로 더해집니다.\n      /minus. -> ··· 빼지는 수 -> ··· 빼는 수 - 두 수가 소숫점으로 빼집니다.\n      /encouragement, /encour. - 오늘 하루에 대해 docom이 격려해줍니다.\n      /who - 만든 사람을 알립니다.\n      /ver - 버전 정보를 알려줍니다.\n      /rcp - 가위바위보를 docom과 대결합니다.\n      /painting, /pain. -> ···(앞으로 가는 수치) -> ···(각도 조정) -> ···/esc(마침) - 그림을 그립니다. 반복 가능\n      /random, /ran. -> ···랜덤으로 고를 단어 또는 수치 -> ···/result, /res.(마치고 결과를 내보냄) - 많은 단어와 수치중 하나를 고릅니다.')
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
    elif(a == '/encouragement' or a == '/encour.'):
        b = random.choice(encouragement)
        print(b)
    elif(a == '/who'):
        print('      만든 사람 : 김도훈\n     만든 사람의 말/painting 넘 어렵다')
    elif(a == '/ver'):
        print('      ver a3. 1. 1, 구버전입니다. 업데이트가 필요합니다.\n      6/6 a1. 1 - /hello, /esc 외 5개의 명령어 추가\n      6/6 a1. 2 - /encouragement명령어 간편화, /who, /ver명령어 추가, 각종 간편 업데이트\n      6/7 a2. 1 - /painting, /pain., /rcp명령어 추가\n      6/7 a2.2   ')
    elif(a == '/rcp'):
        d = 100
        while d == 100:
            a = ['가위', '바위', '보']
            b = random_.choice(a)
            c = (input('      가위... 바위...(가위, 바위, 보) : '))
            print('      보!')
            if(c == '가위' or c == '바위' or c == '보'):
                print('      난 %s !'%c)
                print('      상대는 %s!'%b)
                if(b == '      가위'):
                    if(c == '      가위'):
                        print('      비겼다! 다시하자.')
                        if(d == 100):continue
                    elif(c == '      바위'):
                        print('      내가 이겼다!')
                        d = 1
                    else:
                        print('      내가 졌다...')
                        d = 1
                elif(b == '      바위'):
                    if(c == '      바위'):
                        print('      비겼다! 다시하자.')
                        if(d == 100):continue
                    elif(c == '      보'):
                        print('      내가 이겼다!')
                        d = 1
                    else:
                        print('      내가 졌다...')
                        d = 1
                else:
                    if(c == '      보'):
                        print('      비겼다! 다시하자.')
                        if(d == 100):continue
                    elif(c == '가위'):
                        print('      내가 이겼다!')
                        d = 1
                    else:
                        print('      내가 졌다...')
                        d = 1
            else:
                print('      상대 : 이게 도대체 무슨 모양이고? %s모양은 처음 듣는데 다시 똑바로 내시지?'%c)
                if(m == 100):continue
    elif(a == '/painting' or a == '/pain.'):
        a = 0
        while a == 0:
            b = (input('··· '))
            if(b == '/esc'):
                break
            b = int(b)
            tu. fd(b)
            b = (input('··· '))
            if(b == '/esc'):
                break
            b = int(b)
            tu. rt(b)
    elif(a == '/random' or a == '/ran.'):
        a = 0
        c = []
        while a == 0:
            b = (input('··· '))
            if(b == '/result' or b == '/res.'):
                b = random_.choice(c)
                print('      %s이/가 행운의 주인공입니다!'%b)
                a = 1
            else:
                c.append(b)
                continue
    elif(a == '/day'):
        print
    else:
        print('      error001\n      명령어에 /를 포함했나요?\n      명령어의 철자가 맞나요?\n      간결화 명령어일 경우 뒤에 .을 붙였나요?\n      위가 하나도 지켜지지 않을 경우 오류가 납니다.\n      docom이 처음이라면 /?나 /help를 입력해 도움을 받으십시요.')
