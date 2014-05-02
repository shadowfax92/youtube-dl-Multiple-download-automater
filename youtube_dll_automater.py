import sys
import commands
import os
import csv

#############################################################################
#                           file format                                     #
#   <youtube-link>, <name-of-video-for-reference>, <done/not_done>          #
#############################################################################

DEFAULT_FILE_LOCATION='/Users/nsonti/youtube_videos_download.txt'
DOWNLOAD_DIRECTORY='/Users/nsonti/Movies/youtube_downloads/'

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

    to_download = read_file_content_csv(file_name)
    print to_download


if __name__ == '__main__':
    main()

# file_handle=open(DEFAULT_FILE_LOCATION,'rU')
# new_file_content=''
# for line in file_handle:
#     _list=line.rstrip().split(', ')
#     if _list[2] != 'done':
#         print 'Downloading '+str(_list[1])+'.........\n'
#         #go to download directory
#         _cmd='cd '+DOWNLOAD_DIRECTORY
#         #os.system(_cmd)
#         #download in the given directory
#         _cmd=_cmd+' | '+'youtube-dl -o ~/Movies/youtube_downloads/"%(title)s-%(id)s.%(ext)s" --max-quality mp4 '+str(_list[0])
#         os.system(_cmd)
#         print 'downloading done'
#         _list[2]='done'
#     new_file_content+=', '.join(_list)+'\n'
# file_handle.close()
#
# #open for writing new file contents
# file_handle_write=open(DEFAULT_FILE_LOCATION,'w')
# file_handle_write.write(new_file_content)
# file_handle_write.close()
#
# #print new_file_content.rstrip()

