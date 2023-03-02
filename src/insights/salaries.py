from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    jobs = read(path)

    salaries = set()

    for job in jobs:
        if job["max_salary"].isnumeric():
            salaries.add(int(job["max_salary"]))

    return max(salaries)


def get_min_salary(path: str) -> int:
    jobs = read(path)

    salaries = set()

    for job in jobs:
        if job["min_salary"].isnumeric():
            salaries.add(int(job["min_salary"]))

    return min(salaries)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        if "min_salary" not in job or "max_salary" not in job:
            raise ValueError

        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])

        if min_salary > max_salary:
            raise ValueError

        salary = int(salary)

        salary_range = min_salary <= salary <= max_salary

        return salary_range

    except Exception:
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    jobs_filter = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_filter.append(job)

        except ValueError:
            continue

    return jobs_filter
