import threading
import queue
import os

buffer_size = 5

lock = threading.Lock()
queue = queue.Queue(buffer_size)
file_count = 0

def producer(top_dir, queue_buffer):
    # Search sub-dir in top_dir and put them in queue
    queue_buffer.put(top_dir,timeout = 1)
    files = os.listdir(top_dir)
    for f in files:
        filepath = os.path.join(top_dir, f)
        if os.path.isdir(filepath):
            producer(filepath,queue)

def consumer(queue_buffer):
    # search file in directory
    global file_count
    global path
    try:
        path = queue_buffer.get(timeout = 3)
        #print(path)
    except:
        return
    paths = os.listdir(path)
    #print('all list', paths)
    #print('*'*20)
    for p in paths:
        tmp = os.path.join(path,p)
        #print(tmp)
        if os.path.isfile(tmp):
            #print('correct')
            #print('-'*20)
            lock.acquire()
            file_count += 1
            lock.release()
    
def main():
    producer_thread = threading.Thread(target = producer, args = ('testdata', queue))

    consumer_count = 20
    consumers = []
    for i in range(consumer_count):
        consumers.append(threading.Thread(target = consumer, args = (queue,)))

    producer_thread.start()
    for c in consumers:
        c.start()

    producer_thread.join()
    for c in consumers:
        c.join()

    print(file_count, 'files found.')

if __name__ == "__main__":
    main()
