# 예외처리

# 예를 들어 아파트가 11층까지인 줄 알았는데 가보니 10층까지만 있음 

# try:

#     print("나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요: "))
#     num2 = int(input("두 번째 숫자를 입력하세요: "))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2))) # try 내부에 있는 문장이 잘 실행이 되다가 문제가 발생했을 때 \except 부분을 찾아서 발생한 오류에 해당하는 부분이 있으면 그 내부에 있는 명령을 실행함

# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err: # 발생하는 이 에러 문장을 그대로 출력
#     print(err)    # 명확히 어떤 에러가 발생했을 때 그에 대한 처리를 해줄 수 있음

try:

    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요: "))) # 값 추가
    nums.append(int(input("두 번째 숫자를 입력하세요: ")))
    #nums.append(int(nums[0] / nums[1])) # 나눈 값을 nums에 추가해서 출력함
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2])) # try 내부에 있는 문장이 잘 실행이 되다가 문제가 발생했을 때 \except 부분을 찾아서 발생한 오류에 해당하는 부분이 있으면 그 내부에 있는 명령을 실행함

except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err: # 발생하는 이 에러 문장을 그대로 출력
    print(err)    # 명확히 어떤 에러가 발생했을 때 그에 대한 처리를 해줄 수 있음
# except: 
#     print("알 수 없는 에러가 발생하였습니다.") # try문에서 문장이 실행되다가 어떤 오류가 발생했을 때 거기에 대한 오류 ValueError나 ZeroDivisionError가 아닌 나머지 모든 오류 처리
    
except Exception as err: # 어떤 에러인지 메세지를 받기 위해
    print("알 수 없는 에러가 발생하였습니다.") # try문에서 문장이 실행되다가 어떤 오류가 발생했을 때 거기에 대한 오류 ValueError나 ZeroDivisionError가 아닌 나머지 모든 오류 처리
    print(err)