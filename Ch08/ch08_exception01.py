### 예외 처리

a = [1, 2, 3, 4, 5]
a[5]

## 예외처리 실습
def divide(a, b):
    return a/b

try:
    d = divide(10, 10)
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다")
except (TypeError, SyntaxError):
    print("데이터 타입이 맞지 않거나 문법 오류")
except:
    print("다른 예외 발생")
else:
    print("아무 오류도 발생하지 않음 - d:", d)
finally:
    print("예외 발생 여부와 상관없이 항상 실행")

print("연산결과 : ", d)

file_path = "word1.txt"
try:
    f = open(file_path, "rt", encoding="utf-8")
    try:
        data = f.read()
    finally:
        # 파일이 열려있는 상태에서 파일의 내용을 읽다가
        # 예외 발생 혹은 파일 읽기가 끝나면 파일을 닫음
        f.close()
except IOError:
    print("{} 읽기 실패".format(file_path))
else:
    print("else", data)

# 예외가 발생한 경우 f, data는 생성되지 않는 객체 -> NameError 발생
print(f, data)

## 예외 발생 및 미루기

## 예외 발생
def raiseErrorFunc():
    # 예외를 강제로 발생시킬 때 raise 키워드 사용
    raise ZeroDivisionError("0으로 나눌 수 없음")

try:
    raiseErrorFunc()
except ZeroDivisionError as msg:
    print("Zero: ", msg)
except Exception as msg:
    print("Exception: ", msg)

## 예외 전달 (미루기)
def propagationError():
    try:
        raiseErrorFunc()
    except:
        print("예외 발생 전")
        raise
try:
    propagationError()
except Exception as e:
    print("예외처리: {}".format(e))















