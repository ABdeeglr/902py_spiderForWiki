# luca.py is an utility for catch html origin source and provide some basic process

import requests
import re

def catcher_HTMLCatcher(page_URL:str, file_path:str, used_headers:dict)->None:
    """
    根据给出的 URL 获取 HTML 资源

    >>> page_URL 网页资源地址
    file_path 本地保存路径
    headers 请求头
    """
    ret = requests.get(page_URL, headers=used_headers)

    with open(file_path, "w", encoding="utf-8") as writeFile:
        writeFile.write(ret.text)



def downloader_singlePictureDownload(page_URL:str, dir_path:str, used_headers:dict):
    """
    获取指定页面上的图片资源

    >>> page_URL 网页资源地址
    dir_path 本地保存的目录路径
    headers 请求头
    """
    pre_name = page_URL.split('/')[-1]
    file_name = pre_name.rstrip("\n")
    name = file_name[:-4]
    resotore_path = "{}/{}.png".format(dir_path, name)
    ret = requests.get(page_URL, headers = used_headers)

    with open(resotore_path, "bw") as writeFile:
        writeFile.write(ret.content)



def downloader_iteratorPictureDownloader(url_list:list, dir_path:str, used_headers:dict, downloader):
    """
    使用指定的下载函数，遍历下载全部图片资源

    >>> page_URL 网页资源地址
    dir_path 本地保存的目录路径
    headers 请求头
    downloader 下载函数
    """

    for this_url in url_list:
        try:
            downloader(this_url, dir_path, used_headers)
        except NameError(): # 这里的错误检测还需要完善
            with open("./data/log/download.log", "w+") as writeFile:
                writeFile.write("NameError: {} downloading failed".format(this_url))



if __name__ == "__main__":

    dst_file_path = "./data/html/test.html"
    azli_URL = "https://azurlane.koumakan.jp/wiki/List_of_Ships"
    default_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57"
    }

    scylla = "https://azurlane.netojuu.com/images/d/d3/ScyllaSchool.png"


    print("\n\n\nRUN!!!\n______________________________________")
    
    downloader_singlePictureDownload(scylla, "./data/pic_demo", default_headers)