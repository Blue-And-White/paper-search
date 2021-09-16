# paper-search
paper search script


This is a simple tool to automatically find and download papers through SCHUB by importing DOI.

这是一个通过导入DOI，自动通过SCIHUB查找并且，下载论文的简单工具。

The principle is not introduced, it is a simple crawler.

其原理不做介绍，简单的爬虫。

Main can be run directly as the main program. After startup, it will be asked to import a txt file for reading. Note that this file is the file we import DOI. After obtaining the DOI of the paper, put one DOI per line, and then import it. Crawl and download automatically in SCIUB.

main为主程序直接运行即可，启动之后会要求导入一个txt文本类型的文件进行读取，注意这个文件是我们导入DOI的文件，取得论文的DOI之后，每行放一个DOI，然后导入即可在SCIHUB自动爬取下载。



Present problems:

目前存在的问题：

1 For issues that are not supported by SCIHUB in certain formats (we will look for ways to improve in the future)

1  对于某些格式SCIHUB不支持的问题（后续会寻找办法改善）

2 Some DOI does not exist or input errors will cause the program to crash

2 某些DOI不存在或者输入错误会导致程序崩溃

At present, there is only one interface. If there is time, we will consider adding the index function on the engraved book.

目前的接口仅有一个，后面如果有时间会考虑加入刻印本上的索引功能。



​																																																												版本1.0

​																																																												ver 1.0
