class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
       
        li = []
        temp = []
     
        for j in range(len(nums)-1):
            for i in range(j,len(nums)):          
                temp.append(nums[i])
                li.append(temp[:])
                print(li)
            temp = []
        li.append([])
        return li
        
        
#caution: temp[:]-> memory address reference
#템프 그대로 갖다 쓰면 좆됨
#temp 그래도 쓰면 주소값 참조라서 [:]-> 값을 복사해야함
