from bs4 import BeautifulSoup
import  requests
import re
import urllib.parse
import json
from urllib.parse import urlparse, parse_qs
#from faker import Faker
array = []
url_store = {}
usable = []
dic= {}
depth = 2
fuzz_response = {}
#fake = Faker()
def extract(start_url,depth):
    global url_store
    global array
    url_store.setdefault('0', []).append(start_url)
    for i in range(depth):
        print("---------------------------------------------------")
        for url in url_store[str(i)]:
            print(url)
            parse = requests.get(url=url)
            soup = BeautifulSoup(parse.content,'lxml')
            links = soup('a')

            mis_links = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',str(parse.content))
            for link in links:
                try:
                    if(link['href']):
                        li = urllib.parse.urljoin(str(parse.url), str(link['href']))
                        if (start_url in li):
                            get_response(li,start_url,array,i,url_store)
                        else:
                            pass
                        if(li in array):
                            continue
                        else:
                            if(start_url in li):
                                url_store.setdefault(str(i+1), []).append(li)
                                array.append(li)
                except:
                    continue
            for more in mis_links:
                if (more in array):
                    continue
                else:
                    if(start_url in more):
                        url_store.setdefault(str(i + 1), []).append(more)
                        array.append(more)


def get_response(url,start_url,array,i,url_store):
    global depth
    print(url)
    if(i<depth):
        global dic
        dic_dic={}
        parse = requests.get(url=url)
        soup = BeautifulSoup(parse.content,'lxml')
        form = soup('form')

        if(form):
            for form in form:
                if(str(form['action']).startswith('http')):
                    pass
                else:
                    action = urllib.parse.urljoin(str(url), str(form['action']))
            if(form['method']=='get'):
                login = {}
                inputs = form('input')
                for inp in inputs:
                    try:
                        print(inp['name'])
                        login[str(inp['name'])] = 'name'
                        login[str(inp['name'])] = inp['value']
                    except:
                        pass
                get_parse = requests.get(url=action,data=login)
                if not str(url) in dic:
                    dic[str(url)] = {}
                    dic[str(url)]['data'] = []

                dic_dic['response'] = dict(get_parse.headers)
                dic_dic['content'] = "content"
                dic_dic['method'] = 'GET'
                dic_dic['attr'] = "a"
                dic_dic['depth'] = i+1
                dic_dic['parent'] = str(parse.url)
                dic[str(url)]['data'].append(dic_dic)

            if(form['method']=='post'):
                inputs = form('input')
                for inp in inputs:
                    try:
                        print(inp['name'])
                        login[str(inp['name'])] = 'name'
                        login[str(inp['name'])] = inp['value']
                    except:
                        pass
                print("ssss")
                s = requests.session()
                post_parse = s.post(url=action,data=login)
                print(post_parse.content)
        else:
            if not str(url) in dic:
                dic[str(url)] = {}
                dic[str(url)]['data'] = []

            dic_dic['response'] = dict(parse.headers)
            dic_dic['content'] = "content"
            dic_dic['method'] = 'GET'
            dic_dic['attr'] = "a"
            dic_dic['depth'] = i
            dic_dic['parent'] = str(parse.url)
            dic[str(url)]['data'].append(dic_dic)

    else:
        pass
	
#extract('http://quotes.toscrape.com',2)

def fuzz_pitchfork(url):
	global fuzz_response
	dictionary = {}
	url = "http://httpbin.org/get?token=TOKEN_TO_REPLACE&param2=c"
	
	o = urlparse(url)
	query = parse_qs(o.query)
	for key in query:
		print(key)
		print("Enter the name of dictionary for this parameter")
		name = str(input())
		with open(name) as f:
			lines = [line.rstrip('\n') for line in open(name)]
			loop_length = len(lines)
		dictionary[str(key)] = lines
	print(loop_length)
	
	for i in range(5):
		for key in query:
			try:
				query[str(key)] = dictionary[str(key)][i]
			except:
				pass
		parse=requests.get(url=url,data=query)
		print(parse.url)
		print(parse.content)
print("Enter the url to fuzz")
url = str(input())
fuzz_pitchfork(url,)
#with open('data.txt', 'w') as outfile:
   # json.dump(dic, outfile)





