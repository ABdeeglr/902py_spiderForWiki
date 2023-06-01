# mom.py provides
# 1. Format HTML text
# 2. Find the certain url in HTML text
# 3. Clean the url and store it in JSON format


def rEE_filter01(line:str)->tuple:
    """
    rEE 是匹配指定类型的字符串的函数

    filter01 用于匹配起始语句和终止语句确定的 URL
    """

    startExpression = "azurlane.netojuu.com"
    endExpression = ".png"

    start = line.find(startExpression)
    end = line.find(endExpression) + len(endExpression)

    return (start, end)



def filter_cursiveURLCatcher(line:str, dump_list:list)->None:
    """
    Recursively filter out all URLs that match the criteria
    """

    _nums = rEE_filter01(line)
    start = _nums[0]
    end = _nums[1]

    if start > 0:
        dump_list.append(line[start:end])
        line = line[end:]
        filter_cursiveURLCatcher(line, dump_list)



def singleLineURLCatcher(line:str, dump_list:list, filter)->None:
    """
    Extract all URLs that match the criteria from a single-line string
    """
    # 调用指定筛选器函数进行处理
    # 这里做一层封装进行隔离
    filter(line, dump_list) 

    

def URLFileCatcher(file_path:str, dump_list:list, filter)->None:
    """
    Gets all eligible URLs from the specified file
    """

    with open(file_path, "r", encoding="utf-8") as readFile:
        while True:
            line = readFile.readline()
            if not line:
                break
            else:
                singleLineURLCatcher(line, dump_list, filter)


# def cleaner_baseURLCleaner(url_list:list, )



if __name__ == "__main__":

    pass