#最长回文数-动态规划.py
#实际上利用了递归思想并进行去重优化，将之前已经得出的数据结果保存下来了。类似数学归纳法的思想
s='111111111'
print(len(s))
size = len(s)
if size <= 1:
    print(s)
# 二维 dp 问题
# 状态：dp[l,r]: s[l:r] 包括 l，r ，表示的字符串是不是回文串
# 设置为 None 是为了方便调试，看清楚代码执行流程
dp = [[False for k in range(size)] for k in range(size)]
#外方括号中的[False for k in range(size)]相当于内方括号中的False，先建一个列表，再用这个列表当元素建二维列表

print(dp)

longest_l = 1
res = s[0]

# 因为只有 1 个字符的情况在最开始做了判断
# 左边界一定要比右边界小，因此右边界从 1 开始
for r in range(1, size):
    for l in range(r):
        # 状态转移方程：如果头尾字符相等并且中间也是回文
        # 在头尾字符相等的前提下，如果收缩以后不构成区间（最多只有 1 个元素），直接返回 True 即可
        # 否则要继续看收缩以后的区间的回文性
        # 重点理解 or 的短路性质在这里的作用
        if s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1]):
            dp[l][r] = True
            cur_len = r - l + 1
            if cur_len > longest_l:
                longest_l = cur_len
                res = s[l:r + 1]
    # 调试语句
    # for item in dp:
    #     print(item)
    # print('---')
print(res)
print(len(res))