#%%
import json
import pandas as pd
f = open("issues.json", "r", encoding="utf-8")
issues = json.load(f)
f.close()

# %%
issues = pd.DataFrame(issues)
# %%
issues
# %%
issues[["number", "title", "comments", "created_at", "body", "labels"]]
# %%
issues
# %%
oneLabel = issues.loc[1, "labels"]
oneLabel
# %%
for each in oneLabel:
    print(each["name"])
# %%
def bugs(labels):
    for label in labels:
        if label["name"] == "type: bug":
            return True
    return False
# %%
bugsLabel = issues[issues["labels"].apply(lambda x: bugs(x))]
# %%
bugsLabel
# %%
bugsLabel["number"]
# %%
for index, row in bugsLabel.iterrows():
    print(row["number"], row["title"])
# %%
bugsLabel[["number", "title", "body"]].to_csv("bugs.csv")
# %%
