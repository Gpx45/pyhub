
from url_utils import gen_from_urls
from pprint import pprint
urls = ('https://google.com', 'https://cnn.com', 'https://reddit.com')

for resp_len, status, url in gen_from_urls(urls):
    print(resp_len, '->', status, '->', url)


urls_res = {url: size for size, _, url in gen_from_urls(urls)} 
pprint(urls_res)
#                               ^
# The underscore is tell the code to ignore the item
