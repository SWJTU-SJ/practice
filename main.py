import json
import string
from pathlib import Path

# 1. 找到 jobs.json
project_dir = Path(__file__).resolve().parent
data_path = project_dir / "data" / "jobs.json"

# 2. 读取文件
# with data_path.open("r", encoding="utf-8") as file:
#     jobs = json.load(file)

def load_job(path):
    with path.open("r",encoding="utf-8") as file:
        jobs = json.load(file)
    return jobs

jobs = load_job(data_path)

# print("岗位数量：", len(jobs))
# print("整体类型：", type(jobs))
# print("第一条岗位的类型：", type(jobs[0]))
# print("第一条岗位名称：", jobs[0]["title"])








def filter_by_city_and_salary(jobs, city, min_salary):
    results = []
    for job in jobs:
        if job["city"] == city:
            if job["salary_min"] >= min_salary:
                results.append(job)
    return results # 应为 0

def filter_by_skill(jobs, skill):
    results = []
    for job in jobs:
        if skill in job["skills"]:
            results.append(job)
    return results

city_salary_jobs = filter_by_city_and_salary(jobs, "成都", 10)
sorted_jobs = sorted(city_salary_jobs,key=lambda job: job["salary_min"], reverse=False)

# for job in city_salary_jobs:
#     print(job["title"], job["salary_min"])
#
# for job in sorted_jobs:
#     print(job["title"], job["salary_min"])


python_jobs = filter_by_skill(city_salary_jobs, "Python")

# print("符合全部条件的岗位数：", len(python_jobs))
# for job in python_jobs:
#     print(job["title"], job["company"])


# pythonskill = filter_by_skill(jobs,"Python")
# AIskill = filter_by_skill(jobs,"AI")
# print(len(pythonskill))
# print(len(AIskill))

def filter_by_city(jobs, city):
    results = [];
    for job in jobs:
        if job["city"] == city:
            results.append(job)

    return results

ai_jobs = filter_by_skill(jobs,"AI")

output_path = project_dir / "results" / "ai_jobs.json"

with output_path.open("w",encoding="utf-8") as file:
    json.dump(ai_jobs,file,ensure_ascii=False,indent=2)

# print("AI岗位数量：", len(ai_jobs))
# print("结果已保存到：", output_path)

import csv

csv_path = project_dir / "results" / "ai_jobs.csv"
fieldnames = ["title", "company", "city", "salary_min", "direction"]

with csv_path.open("w", encoding="utf-8-sig", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames,
        extrasaction="ignore"
    )
    writer.writeheader()
    writer.writerows(ai_jobs)

print("CSV结果已保存到：", csv_path)







chengdu_jobs = filter_by_city(jobs, "成都")
chongqing_jobs = filter_by_city(jobs, "重庆")
shanghai_jobs = filter_by_city(jobs, "上海")

# print("成都：", len(chengdu_jobs))
# print("重庆：", len(chongqing_jobs))
# print("上海：", len(shanghai_jobs))



count1 = filter_by_city_and_salary(jobs, "成都", 10)
count2 = filter_by_city_and_salary(jobs, "重庆", 12)

# print("chengdugangweishu:",len(count1))
# for job in count1:
#     print(job["title"],job["company"])
# print("chongqingweishu:",len(count2))
# for job in count2:
#     print(job["title"],job["company"])


# 3. 统计岗位总数
# print("岗位总数：", len(jobs))
#
# # 4. 找出成都岗位
# chengdu_count = 0
#
# for job in jobs:
#     if job["city"] == "成都":
#         chengdu_count += 1
#         print("成都岗位：", job["title"],job["company"])
#
# print("成都岗位数：", chengdu_count)
#
# # 5. 计算平均最低月薪
# salary_total = 0
#
# for job in jobs:
#     salary_total += job["salary_min"]
#
# average_salary = salary_total / len(jobs)
# print("平均最低月薪：", average_salary, "K")