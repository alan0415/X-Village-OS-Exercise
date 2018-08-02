from lib.queue import Queue

q = Queue()

def hot_potato(name_list, num):
    for i in range (0,len(name_list)):
        q.enqueue(name_list[i])
    while(q.size() > 1):
        for i in range (0,num):
            tmp = q.dequeue()
            q.enqueue(tmp)
        q.dequeue()
    remaining_person = q.dequeue()
    print(remaining_person)
    return remaining_person

hot_potato(["Susan","Brad","Kent","David"], 6)               # 回傳 "Brad"
hot_potato(["Bill","David","Susan","Jane","Kent","Brad"], 7) # 回傳 "Susan"