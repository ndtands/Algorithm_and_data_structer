# And a queue that only has enqueue and dequeue operations
class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue) 
        
    def isEmpty(self):
        return self.size()>0
input_queue = Queue()

# The player wants to get the upper hand so pressing the right combination of buttons quickly
input_queue.enqueue('DOWN')
print(input_queue.queue)
input_queue.enqueue('RIGHT')
print(input_queue.queue)
input_queue.enqueue('B')
print(input_queue.queue)
# Now we can process each item in the queue by dequeueing them
key_pressed = input_queue.dequeue() # 'DOWN'
print(input_queue.queue)
# We'll probably change our player position
key_pressed = input_queue.dequeue() # 'RIGHT'
print(input_queue.queue)

# We'll change the player's position again and keep track of a potential special move to perform
key_pressed = input_queue.dequeue() # 'B'
print(input_queue.queue)