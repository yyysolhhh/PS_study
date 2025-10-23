import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def find_child(in_l, in_r, post_l, post_r):
    if in_l > in_r:
        return
    root = postorder[post_r]
    print(root, end=" ")
    root_idx = inorder_index[root]
    offset = root_idx - in_l
    find_child(in_l, root_idx - 1, post_l, post_l + offset - 1)
    find_child(root_idx + 1, in_r, post_l + offset, post_r - 1)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
inorder_index = {v: idx for idx, v in enumerate(inorder)}
find_child(0, n - 1, 0, n - 1)