import concurrent.futures
import time

def greetings(name):
    # Wait 10 second before you greet
    time.sleep(10)
    print(f'Hello, {name}')

if __name__ == '__main__':
    print('Main started')
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as e:
        e.map(greetings, ['Foo', 'Bar', 'Baz'])
    print('Done greeting')
    print('Main ended')