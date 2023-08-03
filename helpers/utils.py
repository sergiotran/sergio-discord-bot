import re 
import os

from constants import ROOT_DIR

def is_url(s : str) -> bool:
    pattern = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
    return bool(re.search(pattern, s))

def is_youtube_url(s : str) -> bool:
    if not is_url(s):
        return False

    patterns = (
        r'(https?://)?(www\.)?'
        '(youtube|youtu|youtube-nocookie)\.(com|be)/'
        '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})'
    )

    youtube_regex_match = re.match(patterns, s)

    if youtube_regex_match:
        return youtube_regex_match

    return youtube_regex_match

def log_to_file(data, filename): 
    file = open(os.path.join(ROOT_DIR, filename), 'a')
    file.write(data)
    file.close()
