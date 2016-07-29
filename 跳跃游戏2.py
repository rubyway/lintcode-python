"""
跳跃游戏 II
给出一个非负整数数组，你最初定位在数组的第一个位置。
数组中的每个元素代表你在那个位置可以跳跃的最大长度。　　　
你的目标是使用最少的跳跃次数到达数组的最后一个位置。
样例
给出数组A = [2,3,1,1,4]，最少到达数组最后一个位置的跳跃次数是2(从数组下标0跳一步到数组下标1，然后跳3步到数组的最后一个位置，一共跳跃2次)"""
#://leetcode.com/discuss/422/is-there-better-solution-for-jump-game-ii?show=422#q422
"""
In DP, if you use an array to track the min step at [i], not only will you know the minimum steps needed to get to the destination, but also how to get there. With simple calculation on your array, you can find every optimal road to the end.

This unnecessary information lead to unnecessary cost.

What we really need to do is to calculate: with k steps, what's the furthest point I can reach.

public static int jump(int[] A){ // Jump Game II
    if(null == A || A.length <= 1) return 0;

    int minSteps = 0;
    int furthest = 0;
    int toCheck = 0;
    while(furthest < A.length - 1){
        int endIndex = furthest;
        while(toCheck <= endIndex){
            furthest = Math.max(furthest, toCheck + A[toCheck]);
            toCheck++;
        }
        if(furthest == endIndex) return -1; // this.time.furthest == last.time.furthest: we're trapped, which means the destination cannot be reached.
        minSteps++;
    }
    return minSteps;        
}
"""
class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        length = len(A)
        if length <= 0:
            return 0
        steps, maxjump, i = 0, 0, 0
        while maxjump < length- 1:
            temp = maxjump
            while i<= temp:
                maxjump = max(maxjump, i+ A[i])
                i += 1
            if maxjump == temp:
                return False
            steps += 1
        return steps
