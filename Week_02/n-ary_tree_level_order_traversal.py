# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from tools.time_tools import my_timer


class Solution:
    def levelOrder(self, root):
        queue = [root] if root else []
        ans = []

        while queue:
            ans.append([node.val for node in queue])
            queue = [child for node in queue for child in node.children]

        return ans

    def levelOrder_dfs(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        self.res = []
        self.find_level(root)
        return self.res
    
    def find_level(self, node):
        if node is None:
            return
        level = [node]
        while len(level) != 0:
            layer = []
            new_level = []
            for ele in level:
                layer.append(ele.val)
                for n in ele.children:
                    new_level.append(n)
            level = new_level
            self.res.append(layer)


if __name__ == '__main__':
    S = Solution
    prefix = 'levelOrder'[:2]
    n_list = [x for x in S.__dict__.keys() if x.startswith(prefix)]
    f_list = [S.__dict__[x] for x in n_list]
    print(f_list)
    from IPython import embed
    embed()
