#first accepted version, lets see if we can optimize

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        lists = list(s)
        listt = list(t)
        set_s = set(lists)
        set_t = set(listt)
        count_s = Counter(s)
        count_val_s = list(count_s.values())
        count_t = Counter(t)
        count_val_t = list(count_t.values())
        for i in range(len(s)-1):
            if lists[i] == lists[i+1]:
                if listt[i] != listt[i+1]:
                    return False
            if listt[i] == listt[i+1]:
                if lists[i] != lists[i+1]:
                    return False
        for i in range(len(count_val_s)):
            if count_val_s[i] != count_val_t[i]:
                return False
        if len(set_s) != len(set_t):
            return False
        else:
            return True
        
# try 2 -- cut the set usage bc the counter takes care of the same functionality

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        lists = list(s)
        listt = list(t)
        count_s = Counter(s)
        count_val_s = list(count_s.values())
        count_t = Counter(t)
        count_val_t = list(count_t.values())
        for i in range(len(s)-1):
            if lists[i] == lists[i+1]:
                if listt[i] != listt[i+1]:
                    return False
            if listt[i] == listt[i+1]:
                if lists[i] != lists[i+1]:
                    return False
        for i in range(len(count_val_s)):
            if count_val_s[i] != count_val_t[i]:
                return False
        else:
            return True

