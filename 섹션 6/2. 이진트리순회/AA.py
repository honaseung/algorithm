tree = [1, 2, 3, 4, 5, 6, 7]

def preorder(idx: int) :
    if (len(tree) - 1 < idx) :
    #below if statement means check is there any child before print.
    #so if there is no child, should print itself before return.
    #it's a good way. Because you call function less than above.
    # if (len(tree) - 1 <= 2 * idx) :
    #     print(tree[idx])
        return
    print(tree[idx], end=' ')
    preorder(2 * idx + 1)
    preorder(2 * idx + 2)

def inorder(idx: int) :
    if (len(tree) - 1 <= 2 * idx) :
        print(tree[idx], end=' ')
        return
    inorder(2 * idx + 1)
    print(tree[idx], end=' ')
    inorder(2 * idx + 2)

def postorder(idx: int) :
    if (len(tree) - 1 <= 2 * idx) :
        print(tree[idx], end=' ')
        return
    postorder(2 * idx + 1)
    postorder(2 * idx + 2)
    print(tree[idx], end=' ')

preorder(0)
print(f'preorder')

inorder(0)
print(f'inorder')

postorder(0)
print(f'postorder')
