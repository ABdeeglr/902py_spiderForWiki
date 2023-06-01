import thislib.luca as luca
import thislib.mom as mom


if __name__ == "__main__":
    url = "https://azurlane.koumakan.jp/wiki/Centaur/Gallery"
    fpath = "./data/html/Centaur.html"

    used_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57"
    }

    luca.catcher_HTMLCatcher(url, fpath, used_headers)

    used_list = []

    mom.URLFileCatcher(fpath, used_list, mom.filter_cursiveURLCatcher)

    for line in used_list:
        print(line)