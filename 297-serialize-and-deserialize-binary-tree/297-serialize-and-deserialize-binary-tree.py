# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        if not root:
            return ""
        s=""
        q=[root]
        while q:
            curr=q.pop(0)
            if curr:
                s+=str(curr.val)+","
                q.append(curr.left)
                q.append(curr.right)
            else:
                s+="#,"
        return s

    def deserialize(self, s):
        if len(s)==0:
            return []
        s=s.split(",")
        s=s[:-1]
        root=TreeNode(int(s[0]))
        q=[root]
        i=1
        while q:
            curr=q.pop(0)
            if len(s)>=i:
                if s[i]=="#":
                    curr.left=None
                    i+=1
                else:
                    curr.left=TreeNode(int(s[i]))
                    q.append(curr.left)
                    i+=1
                if s[i]=="#":
                    curr.right=None
                    i+=1
                else:
                    curr.right=TreeNode(int(s[i]))
                    q.append(curr.right)
                    i+=1
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))