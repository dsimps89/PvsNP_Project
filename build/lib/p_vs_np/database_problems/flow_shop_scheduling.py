#Flow-Shop Scheduling










# Example usage
    # Jobs and their processing times on each machine




if __name__ == '__main__':
    def johnsons_algorithm(jobs):
        num_jobs = len(jobs)
        num_machines = len(jobs[0])
        schedule = [[] for _ in range(num_machines)]
        completion_times = [0] * num_machines
        sorted_jobs = sorted(jobs, key=lambda job: min(job[0], job[1]))
        for job in sorted_jobs:
            processing_time_machine1, processing_time_machine2 = job
            if completion_times[0] <= completion_times[1]:
                machine_id = 0
            else:
                machine_id = 1
            start_time = completion_times[machine_id]
            completion_time = start_time + job[machine_id]
            schedule[machine_id].append((job, start_time, completion_time))
            completion_times[machine_id] = completion_time
        makespan = max(completion_times)
        return schedule, makespan
    if __name__ == "__main__":
        jobs = [
            (2, 3),  # Job 0: Processing times on machines [2, 3]
            (4, 1),  # Job 1: Processing times on machines [4, 1]
            (3, 2)   # Job 2: Processing times on machines [3, 2]
        ]
        schedule, makespan = johnsons_algorithm(jobs)
        print("Job Schedule:")
        for machine_id, tasks in enumerate(schedule):
            print(f"Machine {machine_id + 1}:")
            for task in tasks:
                job = task[0]
                start_time = task[1]
                completion_time = task[2]
                print(f"Job {job}: Start Time = {start_time}, Completion Time = {completion_time}")
            print()
        print("Makespan:", makespan)
