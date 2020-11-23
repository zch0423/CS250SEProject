#coding:utf-8
'''
 FileName      ：process.py
 Author        ：@zch0423
 Date          ：Nov 22, 2020
 Description   ：处理comments和issues json文件，进行user friendly输出

commentKeys
['url', 'html_url', 'issue_url', 'id', 'node_id', 
'user', 'created_at', 'updated_at', 'author_association', 
'body', 'performed_via_github_app']

issueKeys
issue编号是number
['url', 'repository_url', 'labels_url', 
'comments_url', 'events_url', 'html_url', 
'id', 'node_id', 'number', 'title', 'user', 
'labels', 'state', 'locked', 'assignee', 
'assignees', 'milestone', 'comments', 'created_at', 
'updated_at', 'closed_at', 'author_association', 
'active_lock_reason', 'body', 'closed_by', 
'performed_via_github_app']
# 2019-03-08T11:31:58Z time
'''


import json
# 读入comments文件
f = open("comments.json", "r")
comments = json.load(f)
f.close()
commentsKeys = ['url', 'html_url', 'issue_url', 'id', 'node_id',
                'user', 'created_at', 'updated_at', 'author_association',
                'body', 'performed_via_github_app']
# 读入issues文件
f = open("issues.json", "r")
issues = json.load(f)
f.close()
issuesKeys = ['url', 'repository_url', 'labels_url',
              'comments_url', 'events_url', 'html_url',
              'id', 'node_id', 'number', 'title', 'user',
              'labels', 'state', 'locked', 'assignee',
              'assignees', 'milestone', 'comments', 'created_at',
              'updated_at', 'closed_at', 'author_association',
              'active_lock_reason', 'body', 'closed_by',
              'performed_via_github_app']


def commentsByID(ID, content="all"):
    '''
    Description: 
    根据id提取comments的指定cotent
    ---
    Params:
    ID，int 最小为1, 最大为2477
    content, string，形如 “id url”用空格分开的属性字符串，必须在issuesKeys中
    ---
    Returns:
    targets, 返回新的comments列表
    '''
    # 参数检查
    if ID < 1 or ID > 2477:
        print("请将ID范围限制在1-2477")
        return
    if content=="all":
        keys = commentsKeys
    else:
        keys = content.split()
        for key in keys:
            if key not in commentsKeys:
                print("请输入正确的comments属性，属性列表")
                print(commentsKeys)
                return
    targets = []
    for oneIssue in comments:
        if not oneIssue:
            continue
        issueID = int(oneIssue[0]["issue_url"].split("/")[-1])
        if issueID!=ID:
            continue
        for comment in oneIssue:
            # 每一条comment
            temp = dict()
            for key in keys:
                temp[key] = comment[key]
            targets.append(temp)
        return targets


def issueSelector(startID=1, endID=2477, state="all", startTime="2015-01-17", endTime="2020-11-20"):
    '''
    Description: 
    指定开始id结束id，state等筛选issue信息
    ---
    Params:
    startID，int 最小为1，开始的ID号，默认为1
    endID，int 最大为2477，结束的ID号，默认为2477
    state，issue状态，closed, open, all分别表示关闭、开放、不指定
    startTime， string，形如2015-01-17，指定建立时间的起始时间
    endTime，string，形如2020-11-20，指定建立时间的结束时间
    ---
    Returns:
    targets, 返回新的issues列表
    '''
    # 参数检查
    if startID<1 or endID>2477:
        print("请将ID范围限制在1-2477")
        return 
    if startTime<"2015-01-17" or endTime>"2020-11-20":
        print("请将时间范围限制在2015-01-17 ~ 2020-11-20")
        return 
    if state not in ["all", "closed", "open"]:
        print("请将state限制在 all closed open中的一个")
        return 
    targets = []
    for issue in issues:
        issueID = issue["number"]
        if issueID<startID or issueID>endID:
            # 限制ID范围
            continue
        createdTime = issue["created_at"].split("T")[0]
        if createdTime<startTime or createdTime>endTime:
            # 限制创建时间范围
            continue
        issueState = issue["state"]
        if state!="all" and issueState!=state:
            # 限定了状态如open closed 但是不匹配
            continue
        targets.append(issue)
    return targets


def getIssueContent(targets, content):
    '''
    Description:
    获取targets中指定内容或指定多个内容
    ---
    Params:
    targets, list, issues 列表
    content, string, 形如 “id url”用空格分开的属性字符串，必须在issuesKeys中
    ---
    Returns:
    results, list, 包含所有content的列表，其中每个issue信息由字典表示
    '''
    keys = content.split()
    # 检查输入
    for key in keys:
        if key not in issuesKeys:
            print("请输入正确的属性, 属性列表如下")
            print(issuesKeys)
            return 
    results = []
    for issue in targets:
        temp = dict()
        for key in keys:
            temp[key] = issue[key]
        results.append(temp)
    return results
    

def outputBody(targets, outPath="out.md"):
    '''
    Description:
    将body部分导出，默认存为markdown模式，使用markdown编辑器打开
    输出分割线为 “编号 this is not ID”
    ---
    Params:
    targets, issues或者comments列表
    outPath, 输出文件名，建议markdown文件方便显示
    ---
    Returns:
    
    '''
    f = open(outPath, "w")
    count = 1
    for each in targets:
        body = each["body"]
        f.write(f"# {count} this is title\n")
        f.write(body)
        f.write("\n\n\n\n")
        count += 1
    f.close()

def selectIssueInput():
    '''
    筛选issues
    Returns: tuple, (startID, endID, state, startTime, endTime)
    '''
    IDinfo = input("开始ID和结束ID,1-2477中一个值，用空格隔开，直接回车默认全选: ")
    if IDinfo:
        temp = IDinfo.split()
        startID = int(temp[0])
        endID = int(temp[1])
    else:
        startID = 1
        endID = 2477 
    stateInfo = input("state信息 输入o表示open，c表示closed，直接回车默认全选: ")
    if stateInfo=='o':
        state = "open"
    elif stateInfo=="c":
        state = "c"
    else:
        state = "all"
    timeInfo = input("时间范围，用空格隔开，格式为2015-01-17 2020-11-20，不超出此时间范围，直接回车默认全选: ")
    if timeInfo:
        temp = timeInfo.split()
        startTime = temp[0]
        endTime = temp[1]
    else:
        startTime = "2015-01-17"
        endTime = "2020-11-20"
    print("请输入需要选择的字段，用空格隔开，所有属性列表如下")
    print('''
    number:编号
    title:标题
    labels:标签 
    state:状态
    comments:评论数
    created_at:创建时间
    body:内容
    ------------------
    如要导出请包含 body
    ''')
    print("------------------")
    content = input("(title body ...) 回车默认全选: ")
    if not content:
        content = "number title labels state comments created_at body"
    return (startID, endID, state, startTime, endTime), content

def issuesLoop():
    '''
    Description:
    一次issues循环体
    ---
    Params:
    ---
    Returns:
    '''
    print("------------------")
    switch = input("请输入需要进行的操作 --- (a)导出筛选的body内容 (b)命令行输出结果 a/b: ")
    params, content = selectIssueInput()  # (startID, endID, state, startTime, endTime)
    targets = issueSelector(*params)
    results = getIssueContent(targets, content)
    if switch=="a":
        outfile = input("请输入导出文件地址，回车默认out.md(推荐使用md格式打开查看): ")
        if not outfile:
            outfile = "out.md"
        outputBody(results, outfile)
    elif switch=="b":
        # 格式化输出
        for each in results:
            print("------------------")
            print()
            for key, item in each.items():
                print(key, item)

def commentsLoop():
    '''
    Description:
    一次comments循环体
    ---
    Params:
    ---
    Returns:
    '''
    print("------------------")
    print("查找某个编号issues的comments信息")
    ID = int(input("请输入需要查找的issues编号 1-2477: "))
    print("------------------")
    print("请输入需要选择的字段，用空格隔开，所有属性列表如下")
    print('''
    user: 用户信息
    created_at: 创建日期
    body: 内容
    -----------------------
    如果需要导出body请选择body
    ''')
    content = input("(user body ...) 回车默认全选: ")
    if not content:
        content = "user created_at body"
    targets = commentsByID(ID, content)
    switch = input("请输入需要进行的操作 --- (a)导出筛选的body内容 (b)命令行输出结果 a/b: ")
    if switch =='a':
        outfile = input("请输入导出文件地址，回车默认com.md(推荐使用md格式打开查看): ")
        if not outfile:
            outfile = "com.md"
        outputBody(targets, outfile)
    elif switch=='b':
        # 格式输出
        for each in targets:
            print("------------------")
            print()
            for key, item in each.items():
                print(key, item)

def main():
    while True:
        try:
            content = input("你需要查看什么信息？输入i查看issues，输入c查看comments信息 i/c:")
            if content == "i":
                issuesLoop()
            elif content == "c":
                commentsLoop()
        except Exception as e:
            print(e)
            print("请按指示输入")
        finally:
            q = input("输入q退出，任意字符继续")
            if q=="q":
                break

if __name__ == "__main__":
    main()
    # test()
