# Python code to find the base URL from a URL string
# Using regular expressions
import re 

def base(url): 
    regex = 'https?://([A-Za-z_0-9.-]+).*'
    url = re.search(regex, url)
    if url:
        return url.group(1)
    else:
        return ''

def filterBlacklistedUrl(history_list, blacklisted_sites):
    
    return [url for url in history_list if base(url) not in blacklisted_sites]