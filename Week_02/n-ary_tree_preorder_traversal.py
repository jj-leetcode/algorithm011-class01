# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from tools.time_tools import my_timer


class Solution:
   def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []
        
        stack, output = [root, ], []            
        while stack:
            root = stack.pop()
            output.append(root.val)
            stack.extend(root.children[::-1])
                
        return output

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        self.res = []
        self.find_vals(root)
        return self.res

        
    def find_vals(self, node):
        if node:
            self.res.append(node.val)
            #print(node.val)
            if node.children:
                for n in node.children:
                    self.find_vals(n)



if __name__ == '__main__':
    S = Solution
    prefix = 'preorder'[:2]
    n_list = [x for x in S.__dict__.keys() if x.startswith(prefix)]
    f_list = [S.__dict__[x] for x in n_list]
    print(f_list)
    from IPython import embed
    embed()