"""
A thread that can be stopped
"""
import threading


class StoppableThread(threading.Thread):
    """
    Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition

    https://stackoverflow.com/a/325528/6335363
    """

    def __init__(self,  *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()
