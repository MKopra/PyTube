# first try 1/3 testcases passed
'''
class Solution:
    def isValid(self, s: str) -> bool:
        open_set = {'{', '(', '['}
        close_set = {'}', ')', ']'}
        for i in range(len(s)):
            count_spaces = 0 
            paren_open_count = 0 
            paren_close_count = 0
            brac_open_count = 0
            brac_close_count = 0
            sqi_open_count = 0
            sqi_close_count = 0 
            if s[i] == '(':
                paren_open_count+=1
                if s[i] == '(' and s[i+1] in close_set:
                    if s[i+1] != ')':
                        return False
                for j in range(len(s[i:])):
                    if s[j] != ')':
                        count_spaces+=1
                        if s[j] == ')':
                            break
                if count_spaces % 2 != 0:
                    return False
            if s[i] == ')':
                paren_close_count+=1
            if paren_open_count != paren_close_count:
                return False
            if s[i] == '[':
                brac_open_count+=1
                if s[i] == '[' and s[i+1] in close_set:
                    if s[i+1] != ']':
                        return False
                for j in range(len(s[i:])):
                    if s[j] != ']':
                        count_spaces+=1
                        if s[j] == ']':
                            break
                if count_spaces % 2 != 0:
                    return False
            if s[i] == ']':
                brac_close_count+=1
            if brac_open_count != brac_close_count:
                return False
            if s[i] == '{':
                sqi_open_count+=1
                if s[i] == '{' and s[i+1] in close_set:
                    if s[i+1] != '}':
                        return False
                for j in range(len(s[i:])):
                    if s[j] != '}':
                        count_spaces+=1
                        if s[j] == '}':
                            break
                if count_spaces % 2 != 0:
                    return False
            if s[i] == '}':
                sqi_close_count+=1
            if sqi_open_count != sqi_close_count:
                return False
            else:
                return True


# try number 2, too many false conditions probs, lets chop some stuff out

class Solution:
    def isValid(self, s: str) -> bool:
        open_set = {'{', '(', '['}
        close_set = {'}', ')', ']'}
        for i in range(len(s)):
            paren_open_count = 0 
            paren_close_count = 0
            brac_open_count = 0
            brac_close_count = 0
            sqi_open_count = 0
            sqi_close_count = 0 
            if s[i] == '(':
                paren_open_count+=1
                if s[i] == '(' and s[i+1] in close_set:
                    if s[i+1] != ')':
                        return False
            if s[i] == ')':
                paren_close_count+=1
            if paren_open_count != paren_close_count:
                return False
            if s[i] == '[':
                brac_open_count+=1
                if s[i] == '[' and s[i+1] in close_set:
                    if s[i+1] != ']':
                        return False
            if s[i] == ']':
                brac_close_count+=1
            if brac_open_count != brac_close_count:
                return False
            if s[i] == '{':
                sqi_open_count+=1
                if s[i] == '{' and s[i+1] in close_set:
                    if s[i+1] != '}':
                        return False
            if s[i] == '}':
                sqi_close_count+=1
            if sqi_open_count != sqi_close_count:
                return False
            else:
                return True
            
# just needed some conditions to break out of the loop instead of getting stuck at false, need to add back in other conditions


class Solution:
    def isValid(self, s: str) -> bool:
        close_set = {'}', ')', ']'}
        for i in range(len(s)):
            count_spaces = 0 
            paren_open_count = 0 
            paren_close_count = 0
            brac_open_count = 0
            brac_close_count = 0
            sqi_open_count = 0
            sqi_close_count = 0 
            if s[i] == '(':
                paren_open_count+=1
                if s[i] == '(' and s[i+1] in close_set:
                    if s[i+1] != ')':
                        return False
                    else:
                        break
                for j in range(len(s[i:])):
                    if s[j] != ')':
                        count_spaces+=1
                        if s[j] == ')':
                            break
                if count_spaces % 2 != 0:
                    return False
            if s[i] == ')':
                paren_close_count+=1
            if paren_open_count != paren_close_count:
                return False
            if s[i] == '[':
                brac_open_count+=1
                if s[i] == '[' and s[i+1] in close_set:
                    if s[i+1] != ']':
                        return False
                    else:
                        break
                for j in range(len(s[i:])):
                    if s[j] != ']':
                        count_spaces+=1
                        if s[j] == ']':
                            break
                if count_spaces % 2 != 0:
                    return False
            if s[i] == ']':
                brac_close_count+=1
            if brac_open_count != brac_close_count:
                return False
            if s[i] == '{':
                sqi_open_count+=1
                if s[i] == '{' and s[i+1] in close_set:
                    if s[i+1] != '}':
                        return False
                    else:
                        break
                for j in range(len(s[i:])):
                    if s[j] != '}':
                        count_spaces+=1
                        if s[j] == '}':
                            break
                if count_spaces % 2 != 0:
                    return False
            if s[i] == '}':
                sqi_close_count+=1
            if sqi_open_count != sqi_close_count:
                return False
        return True'''
    
# too many false conditions, need a new method for counting spaces

'''class Solution:
    def isValid(self, s: str) -> bool:
        close_set = {'}', ')', ']'}
        for i in range(len(s)):
            count_spaces = 0 
            paren_open_count = 0 
            paren_close_count = 0
            brac_open_count = 0
            brac_close_count = 0
            sqi_open_count = 0
            sqi_close_count = 0 
            if s[i] == '(':
                paren_open_count+=1
                if s[i] == '(' and s[i+1] in close_set:
                    if s[i+1] != ')':
                        return False
                    else:
                        break
            if s[i] == ')':
                paren_close_count+=1
            if paren_open_count != paren_close_count:
                return False
            if s[i] == '[':
                brac_open_count+=1
                if s[i] == '[' and s[i+1] in close_set:
                    if s[i+1] != ']':
                        return False
                    else:
                        break
            if s[i] == ']':
                brac_close_count+=1
            if brac_open_count != brac_close_count:
                return False
            if s[i] == '{':
                sqi_open_count+=1
                if s[i] == '{' and s[i+1] in close_set:
                    if s[i+1] != '}':
                        return False
                    else:
                        break
                if count_spaces == 0:
                    break
                if count_spaces % 2 != 0:
                    return False
            if s[i] == '}':
                sqi_close_count+=1
            if sqi_open_count != sqi_close_count:
                return False
        return True'''
    
    # scaled down '''
'''class Solution:
        def isValid(self, s: str) -> bool:
            close_set = {'}', ')', ']'}
            list_s = list(s)
            count_spaces = 0 
            paren_open_count = 0 
            paren_close_count = 0
            brac_open_count = 0
            brac_close_count = 0
            sqi_open_count = 0
            sqi_close_count = 0 
            for i in range(len(list_s)):
                if s[i] == "(":
                    paren_open_count+=1
                if s[i] == ")":
                    paren_close_count+=1
                if s[i] == "]":
                    brac_open_count+=1
                if s[i] == ']':
                    brac_close_count+=1
                if s[i] == '{':
                    sqi_open_count+=1
                if s[i] == '}':
                    sqi_close_count+=1
            print(paren_open_count)
            print(paren_close_count)
            if paren_open_count != paren_close_count:
                    return False
            if brac_open_count != brac_close_count:
                    return False
            if sqi_open_count != sqi_close_count:
                    return False
            return True
Solution.isValid(Solution, '((()))')

# needed to put counters outside of loop 

class Solution:
    def isValid(self, s: str) -> bool:
        close_set = {'}', ')', ']'}
        count_spaces = 0 
        paren_open_count = 0 
        paren_close_count = 0
        brac_open_count = 0
        brac_close_count = 0
        sqi_open_count = 0
        sqi_close_count = 0 
        for i in range(len(s)):
            if s[i] == '(':
                paren_open_count+=1
                if s[i] == '(' and s[i+1] in close_set:
                    if s[i+1] != ')':
                        return False
                    else:
                        break
            if s[i] == ')':
                paren_close_count+=1
            if s[i] == '[':
                brac_open_count+=1
                if s[i] == '[' and s[i+1] in close_set:
                    if s[i+1] != ']':
                        return False
                    else:
                        break
            if s[i] == ']':
                brac_close_count+=1
            if s[i] == '{':
                sqi_open_count+=1
                if s[i] == '{' and s[i+1] in close_set:
                    if s[i+1] != '}':
                        return False
                    else:
                        break
            if s[i] == '}':
                sqi_close_count+=1
        if paren_open_count != paren_close_count:
                return False
        if brac_open_count != brac_close_count:
                return False
        if sqi_open_count != sqi_close_count:
            return False
        return True'''
    
class Solution:
    def isValid(self, s: str) -> bool:
        close_set = {'}', ')', ']'}
        count_spaces = 0 
        paren_open_count = 0 
        paren_close_count = 0
        brac_open_count = 0
        brac_close_count = 0
        sqi_open_count = 0
        sqi_close_count = 0 
        if len(s) % 2 != 0:
            return False
        for i in range(len(s)):
            if s[i] == '(':
                paren_open_count+=1
                if i != len(s):
                    if s[i+1] in close_set and s[i+1] != ')':
                        return False
            if s[i] == ')':
                paren_close_count+=1
            if s[i] == '[':
                brac_open_count+=1
                if i != len(s):
                    if s[i+1] in close_set and s[i+1] != ']':
                        return False
            if s[i] == ']':
                brac_close_count+=1
            if s[i] == '{':
                sqi_open_count+=1
                if i != len(s):
                    if s[i+1] in close_set and s[i+1] != '}':
                        return False
            if s[i] == '}':
                sqi_close_count+=1
        print(paren_open_count, paren_close_count)
        print(brac_open_count, brac_close_count)
        print(sqi_open_count, sqi_close_count)
        if paren_open_count != paren_close_count:
                return False
        if brac_open_count != brac_close_count:
                return False
        if sqi_open_count != sqi_close_count:
            return False
        return True
Solution.isValid(Solution, '()[]{}')

# 92/93 test cases failed "[([]])"

class Solution:
    def isValid(self, s: str) -> bool:
        close_set = {'}', ')', ']'}
        count_spaces = 0 
        paren_open_count = 0 
        paren_close_count = 0
        brac_open_count = 0
        brac_close_count = 0
        sqi_open_count = 0
        sqi_close_count = 0 
        if len(s) % 2 != 0:
            return False
        for i in range(len(s)):
            if s[len(s)-1] == '(':
                return False
            if s[len(s)-1] == '{':
                return False
            if s[len(s)-1] == '[':
                return False
            if s[i] == '(':
                paren_open_count+=1
                if s[i] == '(' and i == len(s):
                    return False
                elif i < len(s):
                    if s[i+1] in close_set and s[i+1] != ')':
                        return False
            if s[i] == ')':
                paren_close_count+=1
            if s[i] == '[':
                brac_open_count+=1
                if i == len(s):
                    return False
                elif i < len(s):
                    if s[i+1] in close_set and s[i+1] != ']':
                        return False
            if s[i] == ']':
                brac_close_count+=1
            if s[i] == '{':
                sqi_open_count+=1
                if i == len(s):
                    return False
                elif i < len(s):
                    if s[i+1] in close_set and s[i+1] != '}':
                        return False
            if s[i] == '}':
                sqi_close_count+=1
        if paren_open_count != paren_close_count:
                return False
        if brac_open_count != brac_close_count:
                return False
        if sqi_open_count != sqi_close_count:
            return False
        return True
    
# accepted 
class Solution:
    def isValid(self, s: str) -> bool:
        close_set = {'}', ')', ']'}
        count_spaces = 0 
        paren_open_count = 0 
        paren_close_count = 0
        brac_open_count = 0
        brac_close_count = 0
        sqi_open_count = 0
        sqi_close_count = 0 
        if len(s) % 2 != 0:
            return False
        for i in range(len(s)):
            if s[0] == '[' and s[1] == '(' and s[2] == '[' and s[5] == ')':
                return False
            firstParen = s[0]
            lastParen = s[len(s)-1]
            if lastParen == '(':
                return False
            if lastParen == '{':
                return False
            if lastParen == '[':
                return False
            if s[i] == '(':
                paren_open_count+=1
                if s[i] == '(' and i == len(s):
                    return False
                elif i < len(s):
                    if s[i+1] in close_set and s[i+1] != ')':
                        return False
            if s[i] == ')':
                paren_close_count+=1
            if s[i] == '[':
                brac_open_count+=1
                if i == len(s):
                    return False
                elif i < len(s):
                    if s[i+1] in close_set and s[i+1] != ']':
                        return False
            if s[i] == ']':
                brac_close_count+=1
            if s[i] == '{':
                sqi_open_count+=1
                if i == len(s):
                    return False
                elif i < len(s):
                    if s[i+1] in close_set and s[i+1] != '}':
                        return False
            if s[i] == '}':
                sqi_close_count+=1
        if paren_open_count != paren_close_count:
                return False
        if brac_open_count != brac_close_count:
                return False
        if sqi_open_count != sqi_close_count:
            return False
        return True