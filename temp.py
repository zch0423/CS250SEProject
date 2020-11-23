#%%
# test
import json

# %%
with open("comments.json", "r") as f:
    comments = json.load(f)
    f.close()
# %%
oneIssueComment = comments[0]
# %%
oneComment = oneIssueComment[0]
# %%
oneComment
# %%
commentKeys = oneComment.keys()
# %%
oneComment["body"]
# %%
with open("test.md", "a") as f:
    # 推荐使用markdown打开
    f.write(oneComment["body"])

# %%
issueID = oneComment["issue_url"].split("/")[-1]
# %%
issueID
'''
['url', 'html_url', 'issue_url', 'id', 'node_id',
 'user', 'created_at', 'updated_at', 'author_association',
 'body', 'performed_via_github_app']
'''
# %%
userInfo = oneComment["user"]
# %%
userID = userInfo["id"]
# %%
createdTime = oneComment["created_at"]
# %%
createdTime
# %%
updatedTime = oneComment["updated_at"]
# %%
with open("issues.json", "r") as f:
    issues = json.load(f)
    f.close()
# %%
issues
# %%
oneIssue = issues[0]
# %%
type(oneIssue)
# %%
oneIssue
# %%
issueKeys = oneIssue.keys()
# %%
issueKeys
'''
['url', 'repository_url', 'labels_url', 
'comments_url', 'events_url', 'html_url', 
'id', 'node_id', 'number', 'title', 'user', 
'labels', 'state', 'locked', 'assignee', 
'assignees', 'milestone', 'comments', 'created_at', 
'updated_at', 'closed_at', 'author_association', 
'active_lock_reason', 'body', 'closed_by', 
'performed_via_github_app']
'''
# %%
# issueID = oneIssue["url"].split("/")[-1]
issueID = oneIssue["number"]
# %%
issueID
# %%
oneIssue["url"]
# %%
issueStatus = oneIssue["state"]
# %%
issueStatus  # "closed" "open"
# %%
issueBody = oneIssue["body"]
# %%
issueBody  # markdown
# %%
issueTime = oneIssue["created_at"]
# %%
oneIssue
# %%
issueTitle = oneIssue["title"]
# %%
issueLauncherInfo = oneIssue["user"]
# %%
issueLauncherID = issueLauncherInfo["id"]
# %%
labels = oneIssue["labels"]  # list
# %%
labelNames = []
for label in labels:
    labelNames.append(label["name"])
print(labelNames)
# %%
issueCommentNumber = oneIssue["comments"]
#%%
issueTime
# %%
times = sorted([each["created_at"].split("T")[0] for each in issues])
# %%
times[0]
# %%
times[-1]
# %%
for each in times[0:20]:
    print(each)
    print(each>"2015-02-22")
# %%
print("9"<"123")
# %%
print(type(oneIssue["number"]))
# %%
