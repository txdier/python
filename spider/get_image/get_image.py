import urllib.request, os, re, urllib

#获取html页面
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html.decode('UTF-8')
def getImg(html):
    '''获取图片url'''
    # reg = r'src="(.+?\.png)" pic_ext'
    reg = r'src="(.+?\.png)"'
    imgre = re.compile(reg)
    imglist = imgre.findall(html)
    x = 1    
    path = 'images-2'
    #判断path目录是否存在，如果不存在，则创建
    if not os.path.isdir(path):
        os.makedirs(path)
    paths = path+'/'
    for imgurl in imglist:
        #下载图片，并设置图片命名格式
        urllib.request.urlretrieve(imgurl,'{0}{1}.png' .format(paths,x))
        print("It's start %s" % x) #显示信息
        x += 1
    return imglist
# html = getHtml('http://tieba.baidu.com/p/3840085725')
html = getHtml('https://findicons.com/pack/2787/beautiful_flat_icons')
getImg(html)
