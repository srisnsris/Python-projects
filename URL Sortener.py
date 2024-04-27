import pyshorteners

def short_url(url):
    shortener = pyshorteners.Shortener()
    a = shortener.tinyurl.short(url)
    return a

url_data = "https://www.youtube.com/watch?v=k8v9ivdG48Y"
print(short_url(url_data))