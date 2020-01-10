def job_count_to_simulation_count(job_count: int) -> int:
    if job_count <= 1:
        return job_count
    return job_count - 1
