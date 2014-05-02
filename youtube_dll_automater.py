import sys
import commands
import os

#############################################################################
#                           file format                                     #
#   <youtube-link>, <name-of-video-for-reference>, <done/not_done>          #
#############################################################################

FILE_LOCATION='/Users/nsonti/youtube_videos_download.txt'
DOWNLOAD_DIRECTORY='/Users/nsonti/Movies/youtube_downloads/'

file_handle=open(FILE_LOCATION,'rU')
new_file_content=''
for line in file_handle:
    _list=line.rstrip().split(', ')
    if _list[2] != 'done':
        print 'Downloading '+str(_list[1])+'.........\n'
        #go to download directory
        _cmd='cd '+DOWNLOAD_DIRECTORY
        #os.system(_cmd)
        #download in the given directory
        _cmd=_cmd+' | '+'youtube-dl -o ~/Movies/youtube_downloads/"%(title)s-%(id)s.%(ext)s" --max-quality mp4 '+str(_list[0])
        os.system(_cmd) 
        print 'downloading done'
        _list[2]='done'
    new_file_content+=', '.join(_list)+'\n'
file_handle.close()

#open for writing new file contents
file_handle_write=open(FILE_LOCATION,'w')
file_handle_write.write(new_file_content)
file_handle_write.close()

#print new_file_content.rstrip()

