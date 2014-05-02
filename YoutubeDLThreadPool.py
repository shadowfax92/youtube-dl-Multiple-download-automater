__author__ = 'nsonti'

import time
import os
import threading

# Log levels
# - 0 = Debug
# - 1 = Info
LOG_LEVEL = 1

#job of this thread is to download youtube videos using  url and store it in download_path
class DownloadThreadPool:
    def __init__(self, num_threads):
        self.num_threads = num_threads
        self.queue_access_lock = threading.Condition(threading.Lock())
        self.task_queue = [] # each element of task queue contains a dict which stores keys - url, image_store_path
        self.download_count = 0
        self.threads = [] # stores all the threads
        self.is_join = False # when this is set to True threadPool has joined all threads

    def get_thread_count(self):
        return self.num_threads

    def get_queue_size(self):
        self.queue_access_lock.acquire()
        queue_len = len(self.task_queue)
        self.queue_access_lock.release()
        return queue_len

    def create_threads(self):
        for i in range(self.num_threads):
            new_thread = DownloadThreadClass(_pool=self,_id=i)
            self.threads.append(new_thread)
            new_thread.start()

    # data_dictionary can contain any number of fields. In this youtube_dl downloader case it will contain 'url' and 'file_store_path'
    def add_to_queue(self, data_dictionary):
        self.queue_access_lock.acquire()
        self.task_queue.append(data_dictionary)
        self.download_count += 1
        self.queue_access_lock.release()

    def get_next_task(self):
        tmp = {}
        self.queue_access_lock.acquire()
        if len(self.task_queue) != 0:
            tmp = self.task_queue.pop(0)
        else:
            tmp = None
        self.queue_access_lock.release()
        return tmp

    def get_total_image_count(self):
        return self.download_count

    def join_all(self, wait_for_tasks=True):
        self.is_join = False

        if wait_for_tasks:
            while self.task_queue != []:
                time.sleep(2)

        for thread in self.threads:
            thread.set_quit()
            thread.join()

        self.is_join = True


class DownloadThreadClass (threading.Thread):
    def __init__(self, _pool, _id=0):
        threading.Thread.__init__(self)
        self.tid = _id
        self.parent_pool = _pool
        self.die = False
    def run(self):
        logging(str("Thread Started %d" %(self.tid)),0)
        # self.die is set to True, the thread will come out of while loop in next iteration
        while self.die == False:
            job = self.parent_pool.get_next_task()
            if job == None:
                time.sleep(2)
            else:
                if 'url' in job:
                    url = job['url']
                if 'file_store_path' in job:
                    file_store_path = job['file_store_path']
                logging(str('Thread %d: Downloading  %s' %(self.tid,str(url))),1)

                _cmd='cd '+DOWNLOAD_DIRECTORY
                #os.system(_cmd)
                #download in the given directory
                _cmd=_cmd+' | '+'youtube-dl -o ~/Movies/youtube_downloads/"%(title)s-%(id)s.%(ext)s" --max-quality mp4 '+str(url)
                os.system(_cmd)


    def set_quit(self):
        self.die = True


def logging(string,log_level=0):
    if LOG_LEVEL == log_level:
        print string
    return