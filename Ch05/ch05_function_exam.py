### 연습문제 01

def rect_area():
    import sys
    print("사각형의 폭을 입력해주세요")
    width = int(sys.stdin.readline())
    print("사각형의 높이를 입력해주세요")
    height = int(sys.stdin.readline())
    peri = (width+height)*2
    area = width * height
    d1 = {"폭": width, "높이": height, "둘레": peri, "면적": area}
    return "폭: {}m, 높이: {}m인 사각형의 둘레: {}m, 면적: {}㎡".format(d1.get("폭"), d1.get("높이"), d1.get("둘레"), d1.get("면적"))

d = rect_area()
print(d)

### 연습문제 02

def sal_amount():
    import sys
    print("월급을 입력해주세요 : ")
    sal = int(sys.stdin.readline())
    tax1 = sal * 0.045; tax2 = sal * 0.0306; tax3 = tax2 * 0.0655
    tax4 = sal * 0.0065; tax5 = 33570; tax6 = tax5 * 0.1
    sum_tax = tax1 + tax2 + tax3 + tax4 + tax5 + tax6
    real_sal = sal - sum_tax
    print("월 급여 : ", sal)
    print("[소득 공제액]")
    print("국민연금: ", tax1)
    print("건강보험: ", tax2)
    print("장기요양: ", tax3)
    print("고용보험: ", tax4)
    print("소득세: ", tax5)
    print("지방소득세: ", tax6)
    print("총 공제액", sum_tax)
    print("==========================================")
    print("실수령액: ", real_sal)

sal_amount()

### 연습문제 3

dic = {"그리스":"아테네",
       "네덜란드":"암스테르담",
       "노르웨이":"오슬로",
        "덴마크":"코펜하겐",
       "독일": "베를린",
       "라트비아" : "리가",
       "러시아" : "모스크바",
       "루마니아" : "부쿠레슈티",
       "룩셈부르크" : "룩셈부르크",
       "리투아니아" : "빌뉴스",
       "리히텐슈타인" : "파두츠",
       "마케도니아" : "스코페",
       "스웨덴" : "스톡홀름",
       "스위스" : "베른",
       "슬로바키아" : "브라티슬라바",
       "슬로베니아" : "류블랴나",
       "아이슬란드" : "레이캬비크",
       "아일랜드" : "더블린",
       "안도라" : "안도라라베야",
       "알바니아" : "티라나",
       "에스토니아" : "탈린",
       "에스파냐" : "마드리드",
       "영국" : "런던",
       "오스트리아" : "빈",
       "모나코" : "모나코",
       "몬테네그로" : "포드고리차",
       "몰도바" : "포드고리차",
       "몰타" : "발레타",
       "바티칸" : "바티칸시티",
       "벨기에" : "브뤼셀",
       "벨로루시" : "민스크",
       "보스니아헤르체코비나" : "사라예보",
       "불가리아" : "소피아",
       "산마리노" : "산마리노시티",
       "세르비아" : "베오그라드",
       "우크라이나" : "키예프",
       "이탈리아" : "로마",
       "체코" : "프라하",
       "크로아티아" : "자그레브",
       "키프로스" : "니코시아",
       "포르투갈" : "리스본",
       "폴란드" : "바르샤바",
       "프랑스" : "파리",
       "핀란드" : "헬싱키",
       "헝가리" : "부다페스트"
       }

def europe_capital():
    import sys
    print("유럽나라의 수도를 맞추어 주세요.(프로그램을 종료: Enter키 입력)")
    for answer in dic.items():
        print("{}의 수도는?".format(answer[0]))
        input_data = sys.stdin.readline().rstrip()
        if input_data == dic.get(answer[0]):
            print("정답 입니다")
        elif input_data == '':
            print("프로그램을 종료합니다.")
            break
        elif input_data != dic.get(answer[0]):
            print("{}의 수도는 {}입니다".format(answer[0], answer[1]))

europe_capital()

### 연습문제 4
from functools import reduce
result = reduce(lambda x, y: x + y, list(map(lambda x: x ** 2, range(1, 11))))
print(result)

### 연습문제 5
from functools import reduce
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = reduce(lambda a,b: a+b, list(filter(lambda x: x % 2 == 1, l)))
print(list(filter(lambda x: x % 2 == 1, l)))
print(result)












