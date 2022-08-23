from threading import Thread
from queue import Queue
import time

in_queue = Queue()  # 크기가 1인 버퍼


def consumer():
    print('Consumer waiting')
    work = in_queue.get()  # 두 번째로 완료
    print('Consumer working')
    # 작업 수행
    # ...
    print('Consumer done')
    in_queue.task_done()  # 세 번째로 완려


thread = Thread(target=consumer).start()

""" 이제 생산자는 조인으로 소비 스레드를 대기하거나 폴링하지 않아도 됨. 그냥 Queue 인스턴스의 join을 호출해 in_queue가 완료하기를
기다리면 됨 심지어 큐가 비더라도 in_queue의 join메서드는 이미 큐에 추가된 모든 아이템에 task_done을 호출할 때까지 완료하지 않음"""

in_queue.put(object())  # 첫 번째로 완료
print('Producer waiting')
in_queue.join()  # 네 번째로 완료
print('Producer done')