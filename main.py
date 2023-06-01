import thislib.luca as luca
import thislib.mom as mom


if __name__ == "__main__":

    # 信息部分
    url = "https://azurlane.koumakan.jp/wiki/Centaur/Gallery"
    url_2 = "https://azurlane.koumakan.jp/wiki/Br%C3%BCnhilde/Gallery"
    fpath = "./data/html/Centaur.html"
    dpath = "./data/html/Brunhilde.html"


    used_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57"
    }

    # 获取网页资源
    luca.catcher_HTMLCatcher(url_2, dpath, used_headers)

    # 获取图片链接列表
    used_list = []
    mom.URLFileCatcher(dpath, used_list, mom.filter_cursiveURLCatcher)
    used_list = mom.cleanerTotally(used_list)
    
    # 图片链接存储
    with open("demo2.txt", "w", encoding="utf-8") as wf:
        for line in used_list:
            wf.write(line)
            wf.write("\n")

    # 图片下载

    for line in used_list:
        if "Bg_20" in line:
            continue
        else:
            url = "https://{}".format(line)
            luca.downloader_singlePictureDownload(url, dir_path="./data/pic_demo", used_headers=used_headers)
