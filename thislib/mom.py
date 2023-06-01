# mom.py provides
# 1. Format HTML text
# 2. Find the certain url in HTML text
# 3. Clean the url and store it in JSON format

import json

json_dir = "./data/json/"

#  _____________________
# |                    |
# |    filter part     |
# |____________________|


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


#  _____________________
# |                    |
# |    cleaner part    |
# |____________________|

# def cleaner_baseURLCleaner(url_list:list, )


def cleaner_deleteSpaceOfList(lst):
    """
    删除 URL_list 中空值, 换行符, 重复项
    """
    processed_list = []

    lst2 = []

    for item in lst:
        if item not in lst2:
            lst2.append(item)

    for item in lst2:
        # 去除字符串两端的空格
        item = item.strip()

        # 检查字符串是否为空
        if item:
            # 去除字符串末尾的换行符
            item = item.rstrip('\n')

            # 将处理后的字符串添加到结果列表
            processed_list.append(item)

    return processed_list



def cleaner_deleteThubmPictures(lst):
    """
    根据 URL 删除多余的图片链接
    """
    
    lst2 = []

    # 模糊删除
    for item in lst:
        # 去除缩略图和 Q 版图
        if item.lower().find("chibi") > 0:
            continue
        elif "skin_bg" in item.lower():
            continue
        elif "icon" in item.lower():
            continue
        else:
            lst2.append(item.replace("thumb/", ""))

    processed_list = []

    # 精确删除
    for item in lst2:
        if item.find("MainDayBG") > 0:
            continue
        if item.find("Ruby") > 0:
            continue
        if item.find("Banner") > 0:
            continue
        else:
            processed_list.append(item)

    return processed_list


def cleanerTotally(lst):
    lst = cleaner_deleteThubmPictures(lst)
    lst = cleaner_deleteSpaceOfList(lst)

    return lst

#  _____________________
# |                    |
# |   switcher part    |
# |____________________|

def loader_saveListToJsonFile(url_list:list, filename):
    # 分析列表并存储为字典

    json_data = json.dumps(lst)

    # 写入 JSON 数据到文件
    with open(filename, 'w') as file:
        file.write(json_data)





if __name__ == "__main__":

    pass