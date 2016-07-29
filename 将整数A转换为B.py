"""
将整数A转换为B

 描述
 笔记
 数据
 评测
如果要将整数A转换为B，需要改变多少个bit位？

您在真实的面试中是否遇到过这个题？ Yes
样例
如把31转换为14，需要改变2个bit位。

(31)10=(11111)2

(14)10=(01110)2"""
class Solution {
public:
    /**
     *@param a, b: Two integer
     *return: An integer
     */
    int bitSwapRequired(int a, int b) {
        int i = 0;
        int j = 0;
        int count = 0;
        int scanbit = 1;
        while (scanbit)
        {
            i = a & scanbit;
            j = b & scanbit;
            if(i ^ j)
                count += 1;
            scanbit = scanbit<<1;
        }

        return count;
    }
};
