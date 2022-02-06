

class Solution:
    
    #Function to find the minimum number of swaps required to sort the array.
	def minSwaps(self, nums):
		#Code here
		d={}
		n=len(nums)
		for i in range(n):
		    d[nums[i]]=i
		sortnums=sorted(nums)
		count=0
		index=0
		for i in range(n):
		    if nums[i]!=sortnums[i]:
		       count+=1
		       index=d[sortnums[i]]
		       d[nums[i]]=index
		       nums[i],nums[index]=nums[index],nums[i]
		return count
		        
#{ 
#  Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		obj = Solution()
		ans = obj.minSwaps(nums)
		print(ans)

# } Driver Code Ends