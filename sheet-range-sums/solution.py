def range_sums(nums, queries):
    """Return the sum of nums[l..r] for each [l, r] in queries."""
    prefix = [0]
    for x in nums:
        prefix.append(prefix[-1] + x)

    res = []
    for l, r in queries:
        res.append(prefix[r + 1] - prefix[l])

    return res
