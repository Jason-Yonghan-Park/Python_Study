### 조건문 - if

# if - else 구분
score = 60
if score >= 60 : # 선언부 -> 조건 , 콜론으로 구분
    print("합격") # 실행부 -> 들여쓰기 -> 조건에 부합하면
else :
    print("불합격")

# if - elif - else 구분
if score >= 90 :
    print("A")
elif score >= 80 :
    print("B")
else:
    print("나머지")

# [], (), {}, "", 0, 0.0, None -> False
if() :
    print("참")
else:
    print("거짓")


