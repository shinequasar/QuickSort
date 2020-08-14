import csv
import random
import time
import sys

def writeFile(file):
    f = open(file, "w") # 파일쓰기
    wr = csv.writer(f)
    num_arr=[]
    for i in range(0,1000000): # 백만개의 임의정수
        num_arr.append(i)
    mixArr(num_arr) #순서 무작위로 섞기
    wr.writerow(num_arr)
    #print(">> 생성된 임의의 정수 개수 : ",len(num_arr))
    f.close()

def writeFile2(arr,file):
    f = open(file, "w") # 파일쓰기
    wr = csv.writer(f)
    wr.writerow(arr)
    print(">> 저장되었습니다 ")
    f.close()
    

def readFile(file):
    f = open(file, "r") # 파일 읽기
    rdr = csv.reader(f)
    arr=[]
    for i in rdr:
        arr.append(i)
    #string으로 저장된 내용 int형으로 변환
    for i in range(0,1000000):
        arr[0][i] = int(arr[0][i])  
    #print("담긴 임의의 정수 : ",arr[0][1])
    f.close()
    return arr   

def mixArr(num_arr):
    random.shuffle(num_arr) #순서 무작위로 섞기


def quick_sort_before(arr):
    if (len(arr) > 1):
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
        return quick_sort_before(left) + mid + quick_sort_before(right)
    else:
        return arr

def quick_sort_after(arr):
    if(len(arr)>1):
	    pivot = arr[random.randint(0, len(arr)-1)] 
	    right = [i for i in arr if i > pivot]
	    left = [i for i in arr if i < pivot]
	    middle = [i for i in arr if i == pivot]
	    return quick_sort_after(left) + middle + quick_sort_after(right)
    else:
	    return arr

print("BoB9 보안제품개발트랙 정소연\n")
print("[일반 quick sort 정렬]")
writeFile("numbers.csv")
arr = readFile("numbers.csv")
start = time.time()  # 시작 시간 저장
arr = quick_sort_before(arr[0])
#arr.sort()
before_time = time.time() - start
print(">> 처리된 시간 : ", before_time, "초")  # 현재시각 - 시작시간 = 실행 시간
#print(">> 담긴 임의의 정수 : ",arr[3]) 
#print(">> 담긴 정수의 인덱스 : ",arr.index('2')) 
print(">> 생성된 임의의 정수 개수 : ",len(arr))
print(">> 사용한 메모리 : ",sys.getsizeof(arr),"byte")
writeFile2(arr,"numbers.csv")
print("\n 다시 순서 섞는 중\n")

# arr = readFile("numbers2.csv")
# mixArr(arr[0])
writeFile("numbers2.csv")
arr = readFile("numbers2.csv")
#
print("[개선한 quick sort 정렬]")
start = time.time()  # 시작 시간 저장

arr = quick_sort_after(arr[0])
#arr.sort()
after_time = time.time() - start
print(">> 처리된 시간 : ",after_time , "초")  # 현재시각 - 시작시간 = 실행 시간
#print(">> 담긴 임의의 정수 : ",arr[3]) 
#print(">> 생성된 임의의 정수 개수 : ",len(arr))
print(">> 사용한 메모리 : ",sys.getsizeof(arr),"byte")

writeFile2(arr,"numbers2.csv")
print("\n[정렬시간 비교]")
print(">> 개선 전 Quick Sort 시간: ",before_time,"초")
print(">> 개선 후 Quick Sort 시간: ", after_time,"초")
time=before_time - after_time
print("## ",time,"초 빨라졌습니다")

