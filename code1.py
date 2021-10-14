nums = [2, 1, 4, 3, 6, 5];dp = [0]*len(nums)
for i in range(len(nums)):
    dp[i] = 1
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + 1)
ans = max(dp)