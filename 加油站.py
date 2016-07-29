"""


在一条环路上有 N 个加油站，其中第 i 个加油站有汽油gas[i]，并且从第_i_个加油站前往第_i_+1个加油站需要消耗汽油cost[i]。

你有一辆油箱容量无限大的汽车，现在要从某一个加油站出发绕环路一周，一开始油箱为空。

求可环绕环路一周时出发的加油站的编号，若不存在环绕一周的方案，则返回-1。
注意事项

数据保证答案唯一。
您在真实的面试中是否遇到过这个题？
样例

现在有4个加油站，汽油量gas[i]=[1, 1, 3, 1]，环路旅行时消耗的汽油量cost[i]=[2, 2, 1, 1]。则出发的加油站的编号为2。
"""
#过于复杂的程序
class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
    #def canCompleteCircuit(gas, cost):
        length = len(gas)
        if sum(cost) > sum(gas):
            return -1
        #visited = [False]*length
        for i in xrange(length):
            have = 0
            tempgas =  gas[i:] + gas[0:i]
            tempcost = cost[i:] + cost[0:i]
            have += tempgas[0]
            j = 0
            while j < length:
                if have >= tempcost[j]:
                    have -= tempcost[j]
                    have += tempgas[j+ 1]
                    j += 1
                    if j == length- 1 and have >= tempcost[-1]:
                        return i
                else:
                    break
#较为简单的程序
class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
    #def canCompleteCircuit(gas, cost):
        length = len(gas)
        if sum(cost) > sum(gas):
            return -1
        #visited = [False]*length
        have, begin = 0, 0
        for i in xrange(length):
            have += gas[i]
            have -= cost[i]
            if have < 0:
                have, begin = 0, i+1
        if sum(gas) >= sum(cost):
            return begin
        else:
            return  -1
