import re

# find the base URL from a URL string
# Using regular expressions


def base(url):
    # regex = "https?://([A-Za-z_0-9.-]+).*"
    # url = re.search(regex, url)

    prefix = re.compile(r"(https?://)?(www\.|w3\.)?")
    url = prefix.sub('', url).strip().split("/")  # noqa

    if url:
        return url[0]
    else:
        return ""


def filterBlacklistedUrl(history_list, blacklisted_sites):
    return [url for url in history_list if base(url) not in blacklisted_sites]
