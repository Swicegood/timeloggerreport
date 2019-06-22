import os
import os.path
import ftplib
import ftputil
import fnmatch, re

dir_dest = '../images' # Directory where the files needs to be downloaded to
pattern = r'^[a-z]+.*\.(jpg|jpeg)' #filename pattern for what the script is looking for
print ('Looking for this pattern :', pattern) # print pattern
i = 0


with ftputil.FTPHost('ftp.atourcity.com', 'bkgoswami@atourcity.com', '{j~B9x27N)UN', session_factory=ftplib.FTP_TLS) as host: # ftp host info
    recursive = host.walk("/wp/wp-content/uploads",topdown=True,onerror=None) # recursive search )
    for root, dirs, files in recursive:
        image_list = [f for f in files if re.match(pattern, f)] # collect all files that match pattern into variable:image_list
        for fname in image_list:
            fpath = host.path.join(root, fname)
            if host.path.isfile(fpath):
                host.download_if_newer(fpath, os.path.join(dir_dest, fname))
host.close()
