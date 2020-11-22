#coding:utf-8
'''
 FileName      ：combine.py
 Author        ：@zch0423
 Date          ：Nov 22, 2020
 Description   ：合并json文件
'''
import os
import json
def combine(dirPath, outPath):
    results = []
    for jsonFile in os.listdir(dirPath):
        if not jsonFile.endswith("json"):
            continue
        filePath = os.path.join(dirPath, jsonFile)
        with open(filePath, "r") as f:
            results.append(json.load(f))
    print(len(results))
    with open(outPath, "w") as f:
        json.dump(results, f)
    

def main():
    combine("issues/", "issues.json")
    combine("comments/", "comments.json")

if __name__ == "__main__":
    main()
