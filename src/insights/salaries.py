from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    @staticmethod
    def is_valid_salary_max(job: dict) -> bool:
        max_salary = job.get('max_salary')
        return max_salary and max_salary != 'N/A' and max_salary.isdigit()

    @staticmethod
    def is_valid_salary_min(job: dict) -> bool:
        min_salary = job.get('min_salary')
        return min_salary and min_salary != 'N/A' and min_salary.isdigit()

    @staticmethod
    def _parse_salary(salary: Union[str, int]) -> int:
        if isinstance(salary, str) and salary.isdigit():
            return int(salary)
        elif isinstance(salary, int):
            return salary
        else:
            raise ValueError('Invalid salary')

    @staticmethod
    def _validate_salary_range(
            min_salary: Union[str, int], max_salary: Union[str, int]) -> None:
        if not isinstance(min_salary, (int, str)) or not isinstance(
                max_salary, (int, str)):
            raise ValueError('Invalid min or max salary')
        min_salary = int(min_salary)
        max_salary = int(max_salary)
        if min_salary > max_salary:
            raise ValueError('Invalid salary range')

    @staticmethod
    def is_valid_salary_range(job: Dict) -> bool:
        min_salary = job.get('min_salary')
        max_salary = job.get('max_salary')
        if isinstance(min_salary, str) and min_salary.isdigit(
        ) and isinstance(max_salary, str) and max_salary.isdigit():
            return int(min_salary) <= int(max_salary)
        return False

    def get_max_salary(self) -> int:
        valid_salaries = [int(job['max_salary']) for job
                          in self.jobs_list if self.is_valid_salary_max(job)]
        return max(valid_salaries) if valid_salaries else 0

    def get_min_salary(self) -> int:
        valid_salaries = [int(job['min_salary']) for job
                          in self.jobs_list if self.is_valid_salary_min(job)]
        return min(valid_salaries) if valid_salaries else 0

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        min_salary = job.get('min_salary')
        max_salary = job.get('max_salary')
        if min_salary is None or max_salary is None:
            raise ValueError('Invalid salary range')
        self._validate_salary_range(min_salary, max_salary)
        salary = self._parse_salary(salary)
        return int(min_salary) <= salary <= int(max_salary)

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        if isinstance(salary, str) and not salary.isdigit():
            raise ValueError('Invalid salary')
        valid_jobs = [job for job in jobs if self.is_valid_salary_range(
            job) and self.matches_salary_range(job, salary)]
        return valid_jobs
