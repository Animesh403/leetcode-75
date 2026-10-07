***Brute Force*** - 
Use nested loop and in inner loop use *continue* keyword but this will create ***o(n^2)*** time complexity.
def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(0,len(nums)):
            mult = 1
            for j in range(0,len(nums)):
                if i==j:
                    continue
                else:
                    mult *= nums[j]
            ans.append(mult)
        return ans

***Optimized way***
For the particular index element the result is its *prefix x postfix* values.
> [!NOTE]
> ***Prefix*** = prod of all terms before that index
> ***Postfix*** = prod of all the terms after that index 
This makes the time complexity to *o(n)* but <mark>but space complexity is o(n^2)</mark>
<ins>Optz space complexity</ins>
> prefix array is created by prefix * nums[i] [!NOTE] iteration from 0 to end
> postfix array is the final result so nums[i] is result array x postfix [!NOTE] iteration from end to 0
