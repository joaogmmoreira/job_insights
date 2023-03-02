from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    jobs = read(path)

    industries = set()

    for job in jobs:
        if job["industry"]:
            industries.add(job["industry"])

    return industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    industries_by_type = [
        industries for industries in jobs if industries["industry"] == industry
        ]

    return industries_by_type
