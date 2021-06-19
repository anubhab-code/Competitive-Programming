def match(candidate, job):
    return candidate["min_salary"] * 9 <= job["max_salary"] * 10