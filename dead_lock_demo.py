import threading

# Dead lock: when you try to lock an existing lock
# Good solution is to let the threading manager handle this
# You can also keep count of your acquires and for each of them hava a realease 
"""
lock = threading.Lock()
lock.acquire()
lock.acquire()
lock.release()
"""

# Other option is to use a re-entance locks
# RLock() allows you to make multiple calls to acquire without causing dead locks
rlock = threading.RLock()
rlock.acquire()
rlock.acquire()
rlock.release()
print(rlock)

# Returns information about the current thread
print(threading.current_thread())