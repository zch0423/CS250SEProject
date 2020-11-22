#coding:utf-8
'''
 FileName      ：issueCrawler.py
 Author        ：@zch0423
 Date          ：Nov 22, 2020
 Description   ：crawler for issues and comments
 2054 not found
'''
# import gevent
# from gevent import monkey
# monkey.patch_all()
# from gevent.pool import Pool
# from gevent.queue import Queue
import requests
from bs4 import BeautifulSoup
import time
import random

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Host": "api.github.com",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15",
    "Accept-Language": "zh-cn",
    "Accept-Encoding": "gzip",
    "Connection": "keep-alive",
    "Authorization": "token f4ca57fbcd8c27db46b77abb454f8bca4f66a324"
}
TIMEOUT = 10

def crawlComments(issuesID):
    '''
    Description:爬取某个id issue的评论
    ---
    Params:
    ---
    Returns:
    
    '''
    issueUrl = f"https://api.github.com/repos/junit-team/junit5/issues/{issuesID}"
    commentsUrl = f"https://api.github.com/repos/junit-team/junit5/issues/{issuesID}/comments"
    r1 = requests.get(issueUrl, timeout=TIMEOUT, headers=HEADERS)
    r2 = requests.get(commentsUrl, timeout=TIMEOUT, headers=HEADERS)
    if r1.status_code==200 and r2.status_code==200:
        with open(f"issues/i{issuesID}.json", "wb") as f:
            f.write(r1.content)
        with open(f"comments/c{issuesID}.json", "wb") as f:
            f.write(r2.content)
    else:
        return False
    t = random.uniform(0, 1.5)
    print("issues", issuesID, "sleep", t)
    time.sleep(t)
    return True

def getIP(q):
    r = requests.get(PROXYURL)
    for each in r.text.split():
        q.put_nowait(each)

# def main(maxworker=10):
#     pool = Pool(maxworker)
#     q = Queue(200)
#     getIP(q)
#     jobs = []
#     for i in range(1, 2478):
#         jobs.append(pool.spawn(crawlComments, i, q))
#     gevent.joinall(jobs)
def dealWithFailed():
    # 失败链接重新爬取
    f = open("failed.txt", "r")
    ids = [line.strip() for line in f.readlines()]
    f.close()
    for eachId in ids:
        flag = False
        count = 1
        while not flag:
            print("time ", count)
            try:
                flag = crawlComments(eachId)
            except Exception as e:
                print(e)
                print("Sleep for 3s")
                flag = False
                time.sleep(2)
            count += 1
            if count == 3:
                with open("failed1.txt", "a") as f:
                    f.write(str(eachId)+"\n")
                break

def main2():
    
    for i in range(1, 2478):
        flag = False
        count = 1
        while not flag:
            print("time ", count)
            try:
                flag = crawlComments(i)
            except Exception as e:
                print(e)
                print("Sleep for 3s")
                flag = False
                time.sleep(2)
            count += 1
            if count == 3:
                with open("failed.txt", "a") as f:
                    f.write(str(i)+"\n")
                break


if __name__ == "__main__":
    # main()
    # main2()
    dealWithFailed()
    # crawlComments(1)

    
