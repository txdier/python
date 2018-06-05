# -*- coding: utf-8 -*-
import time
import requests
import random
import os
from bs4 import BeautifulSoup
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

#设置要抓取的页面范围，以下为1-4页。
nb = list(range(1,51))

#抓取的链接
url = 'http://www.xicidaili.com/nn/'

#临时存储页面信息的文件
filename = 'html.txt'

# 通过for循环依次拼接链接
for i in nb:
	full_url = url + str(i)
	
	# 设置请求的头部信息，伪装成浏览器。
	headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4091.2 Safari/537.36'}
	
	# 随机等待几秒，防止抓取过于频繁被锁定。
	time.sleep(random.randint(5, 10))
	
	print("正在抓取第" + str(i) + "页……")
	
	# 通过前面拼接的链接，抓取页面信息
	r = requests.get(full_url, headers=headers)
	
	print("第" + str(i) + "页抓取完成！")
	
	# 将抓取到的页面存入临时的文件
	with open(filename, 'a') as f_obj:
		f_obj.write(r.text)

print("开始过滤抓取的页面，请稍后……")

# 处理前面抓取到的文件
with open(filename) as f:
	
	# 通过BeaufifulSoup来处理前面抓取的html内容
	bsobj = BeautifulSoup(f.read(), 'html.parser')
	
	# 过滤出html页面中标题位置元素信息，
	title_list = bsobj.findAll('th')
	
	# 过滤出html页面中IP、端口等信息。
	ip_list = bsobj.findAll('td')

info_list = []		
	
# 对ip、端口等信息进行处理，将处理的信息也写入info中，一行一条。
for ip_info in ip_list:

	text = ip_info.get_text().strip() + ' '
	if text == ' ':
		text = '填充 '
		info_list.append(text.strip())
	else:
		info_list.append(text.strip())

print("信息过滤完成！\n开始测试代理的可用性，这个过程可能有点长，请耐心等待~~~\n")

#删除列表中的空元素
while '' in info_list:
	info_list.remove('')

#定义4个空列表，用来存放下面过滤出来的信息
ip = []
prot = []
location = []
type = []
	
#通过while循环过滤出IP、端口、地区和类型信息	
a = 0
while a <= 10:
	for i in info_list[a::10]:
		if a == 1:
			ip.append(i)
		elif a == 2:
			prot.append(i)
		elif a == 3:
			location.append(i)
		elif a == 5:
			type.append(i)
		else:
			break
	a += 1

#依次从IP、端口、地区和类型列表中取出一个值，拼接成IP:Prot
#测试代理IP是否可用，如果可用，则写入it_works.txt文件中
#将所有代理用来请求chinaz.com，如果响应代码为200-300之间，则表示这个代理可以用。
url = 'http://ip.chinaz.com/getip.aspx'
while type:
	i = ip.pop(0)
	t = type.pop(0)
	p = prot.pop(0)
	l = location.pop(0)
	proxy_url = i + ':' + str(p)

	#防止过滤的信息中有空值，只有所有值均不为空的时候才进行测试
	if i !='' and t !='' and p !='' and l !='':
		try:
			r = requests.get(url=url, proxies={'http': proxy_url}, timeout=2)
		except:
			pass
		else:
			#只有响应代码在200-300之间才说明该代理IP可用，才会写入指定的文件中
			# if r.status_code >= 200 and r.status_code < 300:
			if r.status_code == 200:
				# print(url + ' ' + l + ' 这个代理可用！')
				with open("it_works.txt", 'a') as f:
					f.write(t + '\t')
					f.write(i + '\t')
					f.write(p + '\t')
					f.write(l + '\n')
			else:
				pass
	else:
		continue

		#删除之前存储临时页面信息的文件
if os.path.exists(filename):
	os.remove(filename)
		
print("信息过滤完成！请查看it_works.txt文件")
