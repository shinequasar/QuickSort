import csv
import random
import time
import sys

def writeFile():
    f = open("numbers.csv", "w") # 파일쓰기
    wr = csv.writer(f)
    num_arr=[]
    for i in range(0,1000000): # 백만개의 임의정수
        num_arr.append(i)
    random.shuffle(num_arr) #순서 무작위로 섞기
    wr.writerow(num_arr)
    print(">> 생성된 임의의 정수 개수 : ",len(num_arr))
    f.close()

def readFile():
    f = open("numbers.csv", "r") # 파일 읽기
    rdr = csv.reader(f)
    arr=[]
    for i in rdr:
        arr.append(i)
    #print("담긴 임의의 정수 : ",arr[0][1])
    f.close()
    return arr   

def quick_sorted(arr):
    if len(arr) > 1:
        pivot = arr[len(arr)-1]
        left, mid, right = [], [], []
        for i in range(len(arr)-1):
            if arr[i] < pivot:
                left.append(arr[i])
            elif arr[i] > pivot:
                right.append(arr[i])
            else:
                mid.append(arr[i])
        mid.append(pivot)
        return quick_sorted(left) + mid + quick_sorted(right)
    else:
        return arr


print("BoB9 보안제품개발트랙 정소연")
writeFile()
arr = readFile()
start = time.time()  # 시작 시간 저장
arr = quick_sorted(arr[0])
print(">> 처리된 시간 : ", time.time() - start, "초")  # 현재시각 - 시작시간 = 실행 시간
#print(">> 담긴 임의의 정수 : ",arr[3]) 
print(">> 담긴 정수의 인덱스 : ",arr.index('3'))
print(">> 생성된 임의의 정수 개수 : ",len(arr))
print(">> 사용한 메모리 : ",sys.getsizeof(arr),"byte")
#print(arr)
# 담긴 정수가 제대로 정렬이 되었는지 확인하기 3번째가 3이 아니라 100임
#print(arr) 해봐