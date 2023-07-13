import os
import shutil
from datetime import datetime

current_month = datetime.today().strftime('%Y-%m')

path = os.path.join(r'D:\DESKTOP-ARCHIV', current_month)
dir_exist = os.path.exists(path)
if not dir_exist:
    os.mkdir(path)

desktop_path = r'C:\Users\Thoxh\Desktop'

list_of_content = os.listdir(desktop_path)
list_of_ignored_content_extensions = ['.exe', '.lnk']

for c in list_of_content:
    extension = os.path.splitext(c)
    extension = extension[1]
    if extension in list_of_ignored_content_extensions:
       print(f'ignoring {c}')
       continue
    source_path = rf'{desktop_path}\{c}'
    dest_path = rf'{path}\{c}'
    shutil.move(source_path, path)
    print(f'Moved {c} to archive')
       
