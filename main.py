#引入库
import requests
from bs4 import BeautifulSoup

import tkinter as tk
from tkinter.filedialog import askdirectory, askopenfile, askopenfilename

import re
import datetime
#引入其他文件
import printf





def SearchPath():  #指定导入DOI文件路径的函数
    path = askopenfilename()
    return path

def gui():  #后续开发图形界面
    root = tk.Tk()
    path = tk.StringVar()
    root.title("Capture to Paper           By    Blue_And_White")
    tk.Label(root,text="目标路径").grid(row=0,column=0)
    tk.Button(root,text="选择路径",command=SearchPath()).grid(row=0,column=2)
    return path

def Amountdump(path):
    now=str(datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S'))  #这里定义一个文件名，初始化文件，用于记录执行结果
    f=open(now+".txt","w")
    f.write("DOI \t\t\\t\tt\t Status \tPaper Info\n")    
    f.close()
    print("Programe is running\n")
    print("\t\tDOI \t\t\t\t")

    with open(path) as lines:  #导入DOI文献
        for line in lines:
            Scihubdump(line,now)

def Scihubdump(temp,now): #通过Scihub检索论文下载
    #格式化输出
    print("Running:\t"+temp+"\t\t\t\t")
    #构造url,防止被robots杀，换头
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
    url="https://www.sci-hub.ren/"
    url=url+temp
    #requests 库访问对象
    r=requests.get(url)
    soup=BeautifulSoup(r.text,"html.parser")
    if str(soup.title) =="<title>Sci-Hub - search proxy to download article</title>":
        flag=0
    else:
        flag=1
        fname=re.search(r'\|(.*)\|',str(soup.title))#获取论文名方便后续查找
        filename=fname.group(1)
        downloadurl=soup.find_all('a')[1].get("onclick") #抓取下载url
        reurl=re.search("'(.*)'",downloadurl)  #正则表达式剥离出来下载地址,并且修改格式使其能够被requests识别
        reurl=reurl.group(1)                   #剥离出来的DEMO是这样的 https:\\/\\/sci.bban.top\\/pdf\\/10.1109\\/SP40000.2020.00011.pdf?download=true  所以你就知道我们下面怎么做了
        reurl=reurl.replace("/","")
        reurl=reurl.replace("\\","/")
        download=requests.get(reurl,headers=header) 
        #格式化文件名，防止系统误判为目录
        temp=temp.replace("/","_")
        temp=temp.replace("\n","")
        temp=temp.replace(".","_")

        with open("paper/"+ temp +".pdf","wb") as stream: #将论文写入文档
            stream.write(download.content)

    file_open=open(now+".txt","a")
    if flag ==0 :
        file_open.write(temp+" \t\t\t\t "+"False\t"+filename+"\n")
        print("Paper Info:\t"+filename)
        print("Status:\t\tFalse\n")
    else:
        file_open.write(temp+" \t\t\t\t "+"Success\t"+filename+"\n")
        print("Paper Info:\t"+filename)
        print("Status:\t\tSuccess\n")
    file_open.close()

def main():
    printf.main()
    path=SearchPath()
    Amountdump(path)
    print("Download is complete!\n")


if __name__== '__main__':
    main()