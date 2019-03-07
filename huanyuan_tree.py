
import queue
'''
二叉树结点
'''  
class TreeNode:
    def __init__(self,val=None,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
    def settag(self,tag=None):
        self.tag = tag
 
def visit(treenode):
    print(str(treenode.val),end=' ')
'''
根据前序中序遍历非递归构造二叉树
'''
def ConstructTreeByPreInOrder(preorder,inorder):
    print('ConstructTreeByPreInOrder:',end=' ')
    treesize = len(preorder)
    root = TreeNode(preorder[0])
    isvisited = []
    for i in range(treesize):
        isvisited.append(0)
    stactnode = queue.LifoQueue()
    rootindex = inorder.index(preorder[0])
    isvisited[rootindex] = 1
    cur = root
    j = 1
    while(j<treesize):
        if(rootindex>0 and isvisited[rootindex-1]!=1):#构造左子树
            cur.left = TreeNode(preorder[j])
            rootindex = inorder.index(preorder[j])
            isvisited[rootindex] = 1
            j+=1
            stactnode.put(cur)
            cur = cur.left
        elif(rootindex<treesize and isvisited[rootindex+1]!=1):#构造右子树
            cur.right = TreeNode(preorder[j])
            rootindex = inorder.index(preorder[j])
            j+=1
            isvisited[rootindex] = 1
            cur = cur.right
        else:
            cur = stactnode.get()
            rootindex = inorder.index(cur.val)  
    PostOrderWithoutRecursion(root) #后序遍历输出构造的二叉树
'''
根据中序后序遍历非递归构造二叉树
'''
def ConstructTreeByInPostOrder(inorder,postorder): 
    print('\nConstructTreeByInPostOrder:',end=' ')
    treesize = len(postorder)
    root = TreeNode(postorder[treesize-1])
    isvisited = []
    for i in range(treesize):
        isvisited.append(0)
    stactnode = queue.LifoQueue()
    rootindex = inorder.index(postorder[treesize-1])
    isvisited[rootindex] = 1
    cur = root
    j = treesize-2
    while(j>=0):
        if(rootindex<treesize-1 and isvisited[rootindex+1]!=1):#构造右子树
            cur.right = TreeNode(postorder[j])
            rootindex = inorder.index(postorder[j])
            isvisited[rootindex] = 1
            j-=1
            stactnode.put(cur)
            cur = cur.right
        elif(rootindex>0 and isvisited[rootindex-1]!=1):#构造左子树
            cur.left = TreeNode(postorder[j])
            rootindex = inorder.index(postorder[j])
            j-=1
            isvisited[rootindex] = 1
            cur = cur.left
        else:
            cur = stactnode.get()
            rootindex = inorder.index(cur.val)  
    PreOrderWithoutRecursion(root) #前序遍历输出构造的二叉树

if __name__=='__main__':
    preorder = [1, 2, 4, 3, 5, 6, 7]
    inorder = [2, 4, 1, 5, 3, 7, 6]
    postorder = [4, 2, 5, 7, 6, 3, 1]
    ConstructTreeByPreInOrder(preorder, inorder)
    ConstructTreeByInPostOrder(inorder, postorder)
