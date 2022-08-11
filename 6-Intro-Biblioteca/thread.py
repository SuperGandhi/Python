import _thread
import time

def current_hour(name_thread, timestamp):
    count = 0
    
    while count < 5:
        time.slepp(timestamp)
        count += 1
        print(f'hilo: {name_thread} - {time.ctime(time.time())}')

_thread.start_new_thread(current_hour, ('thread_one', 1))
_thread.start_new_thread(current_hour, ('thread_two', 2))

print('He disparado ya los hilos')

while True:
    time.sleep(0.1)
