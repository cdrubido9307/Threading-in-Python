import time
import threading

def func_demo(name):
    print(f'Hello, {name}')
    time.sleep(10)
    print('func_demo ended')

if __name__ == '__main__':
    print('Main thread started')
    # Target specifies the function we want our thread to execute
    # args takes an itarable (pass parameters to our fucntion)
    t = threading.Thread(target=func_demo, args=['Carlos'])
    t.start()
    print('Main thread ended')