nums = [1,100,200,1,100]
key = 1
dict = {}
for i in range(len(nums)-1):
    if nums[i] == key:
        if nums[i+1] not in dict:
            dict[nums[i+1]]=1
        else:
            dict[nums[i+1]]+=1
return max(dict, key = dict.get)