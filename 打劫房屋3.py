"""
在上次打劫完一条街道之后和一圈房屋之后，窃贼又发现了一个新的可以打劫的地方，但这次所有的房子组成的区域比较奇怪，聪明的窃贼考察地形之后，发现这次的地形是一颗二叉树。与前两次偷窃相似的是每个房子都存放着特定金额的钱。你面临的唯一约束条件是：相邻的房子装着相互联系的防盗系统，且当相邻的两个房子同一天被打劫时，该系统会自动报警。

算一算，如果今晚去打劫，你最多可以得到多少钱，当然在不触动报警装置的情况下。

 注意事项

这题是House Robber和House Robber II的扩展，只不过这次地形由直线和圈变成了二叉树

您在真实的面试中是否遇到过这个题？ Yes
样例
  3
 / \
2   3
 \   \ 
  3   1
窃贼最多能偷窃的金钱数是 3 + 3 + 1 = 7.

    3
   / \
  4   5
 / \   \ 
1   3   1
窃贼最多能偷窃的金钱数是 4 + 5 = 9."""
"""
记当前房间为root，如果偷窃当前房间，则其左右孩子left和right均不能偷窃；而其4个孙子节点（ll，lr，rl，rr）不受影响。

因此最大收益为：

maxBenifit = max(rob(left) + rob(right), root.val + rob(ll) + rob(lr) + rob(rl) + rob(rr))
使用字典valMap记录每一个访问过的节点，可以避免重复运算。
"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        sef.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param {TreeNode} root, the root of binary tree.
    # @return {int} The maximum amount of money you can rob tonight
    def houseRobber3(self, root):
        valMap = dict()
        def solve(root, path):
            if root is None: return 0
            if path not in valMap:
                left, right = root.left, root.right
                ll = lr = rl = rr = None
                if left:  ll, lr = left.left, left.right
                if right: rl, rr = right.left, right.right
                passup = solve(left, path + 'l') + solve(right, path + 'r')
                grabit = root.val + solve(ll, path + 'll') + solve(lr, path + 'lr') \
                         + solve(rl, path + 'rl') + solve(rr, path + 'rr')
                valMap[path] = max(passup, grabit)
            return valMap[path]
        return solve(root, '')
