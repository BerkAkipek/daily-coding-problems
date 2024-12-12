# This problem was asked by Microsoft.

# You are given a list of jobs to be done, where each job is represented by a start time and end time. 
# Two jobs are compatible if they don't overlap. Find the largest subset of compatible jobs.

# For example, given the following jobs (there is no guarantee that jobs will be sorted):

# [(0, 6),
# (1, 4),
# (3, 5),
# (3, 8),
# (4, 7),
# (5, 9),
# (6, 10),
# (8, 11)]
# Return:

# [(1, 4),
# (4, 7),
# (8, 11)]

## Solution ##

# There are several ways we can order and schedule jobs greedily:

# 1) Earliest start time 2) Earliest finish time 3) Shortest interval 4) Fewest conflicts

# However, all of them but one can be quickly proven wrong with a counterexample:

# We can also intuit that sorting by earliest finish time works, as since we'll always be picking the closest one to finishing, it can't conflict with future candidates.

# So, our algorithm will look like this:
# 1) Sort all jobs by their earliest finish time 
# 2) Go over every sorted job, and if it's compatible with the current schedule, then add it to our result

def largest_subset_jobs(jobs):
    sorted_jobs = sorted(jobs, key=lambda j: j[1])
    results = []

    for job in sorted_jobs:
        if not results:
            results.append(job)
        if job[0] >= results[-1][1]:
            results.append(job)
    
    return results

# This algorithm takes O(n log n) time, since although we only iterate over the jobs array once, we have to sort it by end time first.