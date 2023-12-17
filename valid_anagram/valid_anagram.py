# Solution1:
#1.Adding the count of repitions into dictionary and comparing the dictionaries

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict={}
        t_dict={}
        if(len(s)!=len(t)):
            return False
        for i in range(0,len(s)): 
            s_dict[s[i]]=s_dict.get(s[i],0)+1
            t_dict[t[i]]=t_dict.get(t[i],0)+1   
        if s_dict==t_dict:
            return True
        else:
            return False