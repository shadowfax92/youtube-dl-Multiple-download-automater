#!/usr/bin/python

__author__ = 'nsonti'

import sys
import os
import csv

from YoutubeDLThreadPool import *

#############################################################################
#                           file format                                     #
#   <youtube-link>, <name-of-video-for-reference>, <done/not_done>          #
#############################################################################

DEFAULT_FILE_LOCATION='/Users/nsonti/youtube_videos_download.txt'
DOWNLOAD_DIRECTORY='/Users/nsonti/Movies/youtube_downloads/'
# Log levels
# - 0 = Debug
# - 1 = Info
LOG_LEVEL = 1

def read_file_content_csv(file_name):
    to_download = []
    fh = open(file_name, 'Ur')
    for line in csv.reader(fh, delimiter=' ',skipinitialspace=True):
        url = line[0]
        try:
            if len(line) > 1:
                if line[1] != 'done' and line[2]!= 'done':
                    to_download.append(url)
                else:
                    print 'Skipping '+str(url)
            else:
                to_download.append(url)
        except:
            print 'index out of range'
    return to_download

def youtube_dl_download(url):
    print 'Downloading '+str(url)
    #go to download directory
    _cmd='cd '+DOWNLOAD_DIRECTORY
    #os.system(_cmd)
    #download in the given directory
    _cmd=_cmd+' | '+'youtube-dl -o ~/Movies/youtube_downloads/"%(title)s-%(id)s.%(ext)s" --max-quality mp4 '+str(_list[0])
    os.system(_cmd)

def main():
    if len(sys.argv) > 0:
        print 'Input file specified and is '+str(sys.argv[1])
        file_name = sys.argv[1]
    else:
        file_name = DEFAULT_FILE_LOCATION

    # get download urls
    to_download = read_file_content_csv(file_name)
    print to_download

    # create thread pool
    download_thread_pool = DownloadThreadPool(10)
    download_thread_pool.create_threads()

    # add data to queue
    for url in to_download:
        tmp = {}
        tmp['url'] = url
        download_thread_pool.add_to_queue(tmp)

    # join once all urls are downloaded
    download_thread_pool.join_all(wait_for_tasks=True)

def logging(string,log_level=0):
    if LOG_LEVEL == log_level:
        print string
    return

if __name__ == '__main__':
    main()


