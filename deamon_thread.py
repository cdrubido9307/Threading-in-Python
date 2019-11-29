import time
import threading

def stop_when_main():
    print('I will stop when the main thread stops')
    time.sleep(10)
    print('Will show if deamon=False')

if __name__ == '__main__':
    print('Main started')
    # deamon=True (By default False) will end the thread as soon as the main thread is ended
    thread = threading.Thread(target=stop_when_main, daemon=True)
    thread.start()
    print('Main ended')
