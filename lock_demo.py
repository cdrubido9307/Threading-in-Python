import threading

# Locks when first created are instantiated as unlocked states
lock = threading.Lock()
print(lock)

# To lock
lock.acquire()
print(lock)

# To unlock
lock.release()
print(lock)