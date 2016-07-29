 """插入区间

    描述
    笔记
    数据
    评测

给出一个无重叠的按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
您在真实的面试中是否遇到过这个题？
样例

插入区间[2, 5] 到 [[1,2], [5,9]]，我们得到 [[1,9]]。

插入区间[3, 4] 到 [[1,2], [5,9]]，我们得到 [[1,2], [3,4], [5,9]]。"""
"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    Insert a new interval into a sorted non-overlapping interval list.
    @param intevals: Sorted non-overlapping interval list
    @param newInterval: The new interval.
    @return: A new sorted non-overlapping interval list with the new interval.
    """
    def insert(self, intervals, newInterval):
        result = []
        length = len(intervals)
        if length == 0:
            return [newInterval]

        for i in xrange(length):
            if newInterval.end < intervals[i].start:
                result.append(newInterval)
                for j in xrange(i, length):
                    result.append(intervals[j])
                break
            elif newInterval.start > intervals[i].end:
                result.append(intervals[i])
            else:
                newInterval.start = min(newInterval.start, intervals[i].start)
                newInterval.end = max(newInterval.end, intervals[i].end)
            if i == length- 1:
                result.append(newInterval)
        return result

