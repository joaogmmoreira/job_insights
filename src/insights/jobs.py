from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, encoding="utf-8") as file:

        jobs_file = csv.DictReader(file)

        jobs_arr = []

        for job in jobs_file:
            jobs_arr.append(job)

        return jobs_arr


def get_unique_job_types(path: str) -> List[str]:
    jobs = read(path)

    types_list = set()

    for job in jobs:
        types_list.add(job["job_type"])

    return types_list


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    jobs_by_type = [job for job in jobs if job["job_type"] == job_type]

    return jobs_by_type