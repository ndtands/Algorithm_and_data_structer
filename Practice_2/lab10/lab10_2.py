#heap (time_executive,thread_name)
class JobQueue:
    def read_data(self):
        self.thread_num, self.m = map(int, input().split())
        self.time_jobs     = list(map(int, input().split()))
    def write_response(self):
        for i in range(self.m):
            print(self.thread_name[i], self.start_times[i]) 

    def siftDown(arr,n,i):
        l = 2 * i + 1
        r = 2 * i + 2
        min = i
        #Ưu tiên thread có thời gian xử lý công việc ít hơn hay la can it tho gian để xong cong viec truoc do roi, và thread có cùng thời gian xử lý sẽ ưu tiên thread nhỏ hơn
        if l < n and ((arr[l][0] < arr[min][0]) or (arr[l][0] == arr[min][0] and arr[l][1] < arr[min][1])):
            min = l

        if r < n and ((arr[r][0] < arr[min][0]) or (arr[r][0] == arr[min][0] and arr[r][1] < arr[min][1])):
            min = r

        if i != min:
            arr[i], arr[min] = arr[min], arr[i]
            JobQueue.siftDown(arr,n,min)

    def assign_jobs(self):
        self.thread_name = [None] * self.m
        self.start_times = [None] * self.m
        next_free_time = [(0, i) for i in range(self.thread_num)]
        n = len(next_free_time)
        for i in range(self.m):
            #Get thread and time
            self.thread_name[i] = next_free_time[0][1]
            self.start_times[i] = next_free_time[0][0]
            #update
            next_free_time[0] = (next_free_time[0][0] + self.time_jobs[i], next_free_time[0][1])
            #Sắp sếp ưu tiên
            JobQueue.siftDown(next_free_time, n,0) 

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()