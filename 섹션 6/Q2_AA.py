tree = [1, 2, 3, 4, 5, 6, 7]

def preorder(idx: int) :
    if (len(tree) - 1 < idx) :
    # if (len(tree) - 1 <= 2 * idx) :
        # print(tree[idx])
        return
    print(tree[idx])
    preorder(2 * idx + 1)
    preorder(2 * idx + 2)

def inorder(idx: int) :
    if (len(tree) - 1 <= 2 * idx) :
        print(tree[idx])
        return
    inorder(2 * idx + 1)
    print(tree[idx])
    inorder(2 * idx + 2)

def postorder(idx: int) :
    if (len(tree) - 1 <= 2 * idx) :
        print(tree[idx])
        return
    postorder(2 * idx + 1)
    postorder(2 * idx + 2)
    print(tree[idx])

print(f'preorder')
preorder(0)
print(f'preorder')
print(f'inorder')
inorder(0)
print(f'inorder')
print(f'postorder')
postorder(0)
print(f'postorder')
