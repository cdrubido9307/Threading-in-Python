import time
import threading

def greet_foo():
    time.sleep(5)
    print('Hello, Foo!')

def greet_bar():
    time.sleep(10)
    print('Hello, Bar!')

def greet_baz():
    time.sleep(15)
    print('Hello, Baz!')

if __name__ == '__main__':
    print('Main started')

    # Thread to greet Foo
    t_greet_foo = threading.Thread(target=greet_foo)
    t_greet_foo.start()

    # Thread to greet Bar
    t_greet_bar = threading.Thread(target=greet_bar)
    t_greet_bar.start()

    # Thread to greet Baz
    t_greet_baz = threading.Thread(target=greet_baz)
    t_greet_baz.start()

    # Wait for main to end to start greeting
    # Greet Foo, Greet Buz, Finally Greet Baz
    t_greet_foo.join()
    t_greet_bar.join()
    t_greet_baz.join()

    print('Main ended')
