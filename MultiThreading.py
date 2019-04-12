import threading
import time

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter, delay):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
      self.delay = delay

   def run(self):
      print ("Starting {}".format(self.name))
      print_time(self.name, self.counter,self.delay)
      print ("Exiting " + self.name)

def print_time(threadName, counter, delay):
   while counter:
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1


# Create new threads
thread1 = myThread(1, "Thread-1", 6, 1)
thread2 = myThread(2, "Thread-2", 4, 2)

# Start new Threads
thread1.start()
thread2.start()

print("Exiting Main Thread")