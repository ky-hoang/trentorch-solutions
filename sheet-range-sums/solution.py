from itertools import accumulate

def range_sums(nums, queries):
    """Return the sum of nums[l..r] for each [l, r] in queries."""
    # same solution, but more concise and using library module functions
    prefix = [0] + list(accumulate(nums))

    return [prefix[r+1] - prefix[l] for l, r in queries]
