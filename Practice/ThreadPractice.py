import threading


class SumThread(threading.Thread):
    def __init__(self, low, high):
        threading.Thread.__init__(self)
        self.low = low
        self.high = high

    def run(self):
        total = 0
        for i in range(self.low, self.high):
            total += i
        print("Subthread", total)


sumThread = SumThread(1, 1000000)
sumThread.start()

print("Main Thread")
