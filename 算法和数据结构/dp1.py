"""
动态规划问题关键：（找出问题的子状态，简历转态转移方程）
"""

# 背包问题：
"""
n: a b c d e
w: 2 2 6 5 4
v: 6 3 5 4 6

name	weight	value	1	2	3	4	5	6	7	8	9	10
  a  	  2	     6	    0	6	6	9	9	12	12	15	15	15
  b  	  2	     3	    0	3	3	6	6	9	9	9	10	11
  c  	  6	     5	    0	0	0	6	6	6	6	6	10	11
  d  	  5	     4	    0	0	0	6	6	6	6	6	10	10
  e  	  4	     6	    0	0	0	6	6	6	6	6	6	6
"""

# 子问题：
"""
欲求前i个物体放入容量为m（kg）背包的最大价值c[i][m]
- w[i]：第i个物体的重量 
- p[i]：第i个物体的价值 
- c[i][j]：前i个物体放入容量为j 包的最大价值 
- c[i-1][j-w[i]]：前i-1个物体放入容量为j-w[i] 包的最大价值
"""

# 状态方程：
"""
c[i, w] = {
    0: if i == 0 or w == 0
    c[i-1, w]:  if w(i) > w
    max(v(i) + c[i - 1, w - w(i), c[i - 1, w]): if w >= w(i) and i > 0
}
"""

import numpy as np


def solve(vlist, wlist, totalWeight, totalLength):
    resArr = np.zeros((totalLength + 2, totalWeight + 2), dtype=np.int)
    # print('arr : \n', resArr)
    for j in range(1, totalWeight + 1):
        for i in range(totalLength, 0, -1):
            # print('i, j', i, j, wlist[i-1])
            if wlist[i - 1] <= j:
                resArr[i, j] = max(resArr[i + 1, j - wlist[i-1]] + vlist[i - 1], resArr[i + 1, j])
                # print('change', resArr[i, j])
            else:
                resArr[i, j] = resArr[i - 1, j]
    # print("resArr:\n {}".format(resArr))
    result = []
    for i in range(1, totalLength + 1):
        result.append(resArr[i, totalWeight])
    r = max(r for r in result)
    return r

'''
----
-00-
-00-
----
1	2	3	4	5	6	7	8	9	10

0	6	6	9	9	12	12	15	15	15
0	3	3	6	6	9	9	9	10	11
0	0	0	6	6	6	6	6	10	11
0	0	0	6	6	6	6	6	10	10
0	0	0	6	6	6	6	6	6	6
'''

if __name__ == '__main__':
    v = [6, 3, 5, 4, 6]
    w = [2, 2, 6, 5, 4]
    weight = 10
    n = 5
    result = solve(v, w, weight, n)
    print(result)
