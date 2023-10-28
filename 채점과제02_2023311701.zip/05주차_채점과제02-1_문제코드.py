"""


아래 코드와 주석을 참고하여 이곳에 필요한 함수와 코드를 작성하여
채점과제02-1 예시화면처럼 실행되도록 만들어주세요.
본인 작성한 코드와 결과화면이 함께 보이도록 캡쳐하여 이미지 파일을 만들고
이를 작성한 파이썬 코드와 함께 제출합니다.


"""

import random

def make_q(op):
    if op == "+":
        num1 = random.randint(0,99)
        num2 = random.randint(0,99)
        print(num1, "+" ,num2, "의 결과는 얼마입니까?" )
        q_res = num1+num2

    elif op == "-":
        num1 = random.randint(0,99)
        num2 = random.randint(0,99)
        print(num1, "-" ,num2, "의 결과는 얼마입니까?" )
        q_res = num1-num2

    elif op == "*":
        num1 = random.randint(0,99)
        num2 = random.randint(0,99)
        print(num1, "*" ,num2, "의 결과는 얼마입니까?" )
        q_res = num1*num2

    elif op == "/":
        num1 = random.randint(0,99)
        num2 = random.randint(0,99)
        print(num1, "/" ,num2, "의 결과는 얼마입니까?" )
        q_res = float(round(num1/num2, 2))
    
    return q_res

while True:   #무한루프
    print("***사칙연산 퀴즈를 시작합니다.***")   #퀴즈 시작을 알리는 print()
    op = input("어떤 연산을 하고 싶은가요? : ")  #연산자를 입력하고 op에 저장

    if op not in ["+","-","*","/"]:  #연산자를 잘못 입력했으면
        print("잘못 입력하였습니다.\n다시 입력하세요.") #잘못 입력되었다는 문구 출력
        continue                     #continue문 실행
    else:                            #연산자 입력이 올바르게 되었다면
        q_res = make_q(op)           #make_q 함수 호출 후 q_res에 반환값 대입
        if op == "/":
            #사용자가 입력한 값을 u_answer에 대입(저장)
            u_answer = float(input("정답을 입력해주세요.(나눗셈은 소수점 2자리까지만 입력) : "))
        else:
            #사용자가 입력한 값을 u_answer에 대입(저장)
            u_answer = int(input("정답을 입력해주세요.(나눗셈은 소수점 2자리까지만 입력) : "))
        if q_res == u_answer:        #q_res값과 u_answer값이 같으면
            print("정답입니다.")     #정답 처리 출력
        else:                        #q_res값과 u_answer값이 다르면
            print("틀렸습니다.")     #오답 처리 출력

        select = input("계속 문제를 푸시겠습니까?(Y/N) ") #퀴즈 지속여부 입력받아 select에 대입

        if select == "Y" or select == 'y': #select의 값이 'Y'이거나 'y'이면
            continue                       #continue문 실행
        else:                              #select의 값이 'Y', 'y'이 아니면
            print("문제풀기를 종료합니다.")#문제풀기 종료 문구 출력
            break                          #break문 실행 무한루프 탈출
                     
                    

