class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str1 = s
        charset = list(set(s))
        
        print(len(charset))
        
        if (len(charset)==0) :
            return 0
        
        maximum_length = len(charset)
        list_str = list(str1)
        
#        print(list_str)
        
        for j in range(0,maximum_length):
            
            for i in range(len(list_str)):
                
                set_of_list_part = set(list_str[i:i+maximum_length-j])
                
                print(list_str[i:i+maximum_length-j])
                print(set_of_list_part)
                if (len(list_str[i:i+maximum_length-j]) == len(list(set_of_list_part))):
#                    print(set_of_list_part)
#                    print(list_str[i:i+maximum_length-j])
                    return len(set_of_list_part)
        
        return 1
        
        
