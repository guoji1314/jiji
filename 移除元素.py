# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 13:29:58 2022
输入：nums = [3,2,2,3], val = 3
输出：2, nums = [2,2]
解释：函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。你不需要考虑数组中超出新长度后面的元素。例如，函数返回的新长度为 2 ，而 nums = [2,2,3,3] 或 nums = [2,2,0,0]，也会被视作正确答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

@author: guo
"""
# val = 3
# s = [3,2,2,3]

val = 2
s = [0,1,2,2,3,0,4,2]
# s = [2,2,2,2]

n,m = 0,0

while m < len(s):
    if s[m] != val:
        s[n] = s[m]
        n += 1
    m += 1
print(n)
        
