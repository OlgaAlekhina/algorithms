def max_profit_assignment(difficulty, profit, worker) -> int:
    job_list = list(zip(difficulty, profit))
    sorted_jobs = sorted(job_list)
    sorted_workers = sorted(worker)
    max_profit, cur_profit, i = 0, 0, 0
    for w in sorted_workers:
        if i < len(profit) and w >= sorted_jobs[i][0]:
            while i < len(profit) and sorted_jobs[i][0] <= w:
                cur_profit = sorted_jobs[i][1] if sorted_jobs[i][1] > cur_profit else cur_profit
                i += 1
        max_profit += cur_profit

    return max_profit


print(max_profit_assignment([27,28,31,44,44], [29,39,60,84,93], [67,53,61,56,63]))

# You have n jobs and m workers. You are given three arrays: difficulty, profit, and worker where:
#
# difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and
# worker[j] is the ability of jth worker (i.e., the jth worker can only complete a job with difficulty at most worker[j]).
# Every worker can be assigned at most one job, but one job can be completed multiple times.
#
# For example, if three workers attempt the same job that pays $1, then the total profit will be $3. If a worker cannot complete any job, their profit is $0.
# Return the maximum profit we can achieve after assigning the workers to the jobs.
#
#
#
# Example 1:
#
# Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
# Output: 100
# Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get a profit of [20,20,30,30] separately.
# Example 2:
#
# Input: difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25]
# Output: 0
#
#
# Constraints:
#
# n == difficulty.length
# n == profit.length
# m == worker.length
# 1 <= n, m <= 104
# 1 <= difficulty[i], profit[i], worker[i] <= 105