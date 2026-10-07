## Product of Array Except Self

### Brute Force
Use a nested loop, and in the inner loop use `continue` to skip `i == j`.
Time complexity: **O(n²)**

```python
def productExceptSelf(self, nums):
    ans = []
    for i in range(len(nums)):
        mult = 1
        for j in range(len(nums)):
            if i == j:
                continue
            mult *= nums[j]
        ans.append(mult)
    return ans
```

### Optimized (Prefix and Postfix)
For each index, the result is `prefix * postfix`.

> [!NOTE]
> **Prefix** = product of all elements before that index
>
> **Postfix** = product of all elements after that index

Time: **O(n)**, Space: **O(n)** (two extra arrays)

### Space Optimized
Time: **O(n)**, Space: **O(1)** (excluding the output array)

> [!NOTE]
> **Pass 1 (left to right):**
> - `res[i] = prefix`
> - then `prefix *= nums[i]`

> [!NOTE]
> **Pass 2 (right to left):**
> - `res[i] *= postfix`
> - then `postfix *= nums[i]`
