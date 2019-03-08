
import requests


# This is a generator
# A generator releases the data as soon as its available
def gen_from_urls(urls: tuple) -> tuple:
    for resp in (requests.get(url) for url in urls):
        yield len(resp.content), resp.status_code, resp.url

#This is a listcomp
# Unlike a generator it waits for all the data to be produced then it releases 
def gen_from_urls_list(urls: tuple) -> tuple:
    for resp in [requests.get(url) for url in urls]:
        yield len(resp.content), resp.status_code, resp.url


#-------------------------------------------------------------
# Example (Try this in the interpreter and you will see.)
# 
# A generator
# for i in (x*3 for x in [1,2,3,4,5]):
#      print(i)  
#
# A listcomp
# for i in [x*3 for x in [1,2,3,4,5]]:
#      print(i)
#
#
#
#
#
#