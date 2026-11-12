import json
from pathlib import Path

project_dir = Path(__file__).parent
data_path = project_dir / "data" / "jobs.json"

with data_path.open("r", encoding="utf-8") as file:
    jobs = json.load(file)


def filter_jobs(jobs, city, min_salary, skill):
    results = []

    for job in jobs:
        if job["city"] == city and job["salary_min"] >= min_salary and skill in job["skills"]:
            results.append(job)

    return results


matched_jobs = filter_jobs(jobs, "成都", 10, "AI")

print("符合条件的岗位数：", len(matched_jobs))
for job in matched_jobs:
    print(job["title"], job["company"])