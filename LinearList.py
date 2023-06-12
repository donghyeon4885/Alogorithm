#!/usr/bin/env python
# coding: utf-8

# In[1]:


def add_data(friend):
    katok.append(None)
    katok[len(katok) - 1] = friend
    
def insert_data(position, friend):
    if position < 0 or position > len(katok):  # 인덱스 범위 체크
        print("index range error")
        return 
    katok.append(None)  #  빈 칸 추가
    # 2. 마지막에 마지막 -1위 값을 이동, 뒤에서 부터 원하는 위치전까지
    for idx in range(len(katok)-1, position, -1):
        katok[idx] = katok[idx - 1]
        katok[idx - 1] = None
    katok[position] = friend
    
def delete_data(position):
    if position < 0 or position > len(katok)-1:  # 인덱스 범위 체크
        print("index range error")
        return 

    katok[position] = None
    for idx in range(position + 1, len(katok)):
        katok[idx - 1] = katok[idx]
        katok[idx] = None
    del katok[len(katok) -1 ]   # 마지막 자료 삭제  


# In[4]:


## 메인 코드 부분 ## 
katok = []
select = -1
if __name__ == "__main__" :   
    while (select != 4) :
        select = int(input("선택하세요(1: 추가, 2: 삽입, 3: 삭제, 4: 종료)--> ")) 
        if (select == 1) :
            data = input("추가할 데이터--> ")
            add_data(data)
        elif (select == 2) :
            pos = int(input("삽입할 위치--> "))
            data = input("추가할 데이터--> ")
            insert_data(pos, data)
        elif (select == 3) :
            pos = int(input("삭제할 위치--> "))
            delete_data(pos)
        elif (select == 4) :
            break
        else :
            print("1~4 중 하나를 입력하세요.")
            continue
        print(katok)


# In[ ]:




