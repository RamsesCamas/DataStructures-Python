from random import randint
from node_based_queue import Queue
from time import sleep

class Track:
    def __init__(self, title:str=None) -> None:
        self.title = title
        self.lenght = randint(5,6)

class MediaPlayerQueue(Queue):
    def __init__(self) -> None:
        super(MediaPlayerQueue,self).__init__()
    
    def add_track(self, track: Track):
        self.enqueue(track)

    def play(self):
        print(f'There are {self.count} songs in the queue')

        while self.count > 0 and self.head is not None:
            current_track_node = self.dequeue()
            print(f'Now playing {current_track_node}')

            sleep(current_track_node.lenght)