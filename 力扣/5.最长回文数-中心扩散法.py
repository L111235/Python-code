def main():
    s="babab"
    size = len(s)
    if size == 0:
        print('')

    # 至少是 1
    longest_palindrome = 1
    longest_palindrome_str = s[0]

    for i in range(size):
        palindrome_odd, odd_len = __center_spread(s, size, i, i)
        palindrome_even, even_len = __center_spread(s, size, i, i + 1)

        # 当前找到的最长回文子串
        cur_max_sub = palindrome_odd if odd_len >= even_len else palindrome_even
        if len(cur_max_sub) > longest_palindrome:
            longest_palindrome = len(cur_max_sub)
            longest_palindrome_str = cur_max_sub

    print(longest_palindrome_str)

def __center_spread(s, size, left, right):
    """
    left = right 的时候，此时回文中心是一条线，回文串的长度是奇数
    right = left + 1 的时候，此时回文中心是任意一个字符，回文串的长度是偶数
    """
    l = left
    r = right

    #s的最大索引下标为size-1
    while l >= 0 and r < size and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l + 1:r], r - l - 1
    #当s[i]两端没有两个相同字符时，返回s[i-1+1:i+]和i+1-(i-1)-1

main()

'''
        size=len(s)
        if size==0:
            return ''
        max_len=1
        max_str=s[0]
        for i in range(size):
            temp_str1,temp_len1=self.cen_spread(s,size,i,i)
            temp_str2,temp_len2=self.cen_spread(s,size,i,i+1)
            if temp_len1>temp_len2:
                temp_len=temp_len1
                temp_str=temp_str1
            else:
                temp_len=temp_len2
                temp_str=temp_str2
            if temp_len>max_len:
                max_len=temp_len
                max_str=temp_str
        return max_str
    #r:right,l:left
    def cen_spread(self,s,size,l,r):
        while l>=0 and r<size and s[r]==s[l]:
            l-=1
            r+=1
        #字符串切片取值左开右闭
        return s[l+1:r],r-l-1
        '''