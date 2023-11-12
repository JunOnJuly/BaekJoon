def solution(N, data_list):
    # 트리 사전
    tree_dict = {}
    # 사전 작성
    for data in data_list:
        tree_dict[data[0]] = [data[1], data[2]]
    
    # 순회
    # 전위 순회
    preorder_list = preorder(tree_dict, 'A', tree_dict['A'][0], tree_dict['A'][1], [])
    # 중위 순회
    inorder_list = inorder(tree_dict, 'A', tree_dict['A'][0], tree_dict['A'][1], [])
    # 후위 순회
    postorder_list = postorder(tree_dict, 'A', tree_dict['A'][0], tree_dict['A'][1], [])

    print(''.join(preorder_list))
    print(''.join(inorder_list))
    print(''.join(postorder_list))


# 전위 순회
def preorder(tree_dict, root, left, right, print_list):
    # 현재 노드 리스트에 추가
    print_list.append(root)
    # 왼쪽 자식이 있으면
    if left != '.':
        preorder(tree_dict, left, tree_dict[left][0], tree_dict[left][1], print_list)
    # 오른쪽 자식이 있으면
    if right != '.':
        preorder(tree_dict, right, tree_dict[right][0], tree_dict[right][1], print_list)
    return print_list


# 중위 순회
def inorder(tree_dict, root, left, right, print_list):
    # 왼쪽 자식이 있으면
    if left != '.':
        inorder(tree_dict, left, tree_dict[left][0], tree_dict[left][1], print_list)
    # 리스트에 추가
    print_list.append(root)
    # 오른쪽 자식이 있으면
    if right != '.':
        inorder(tree_dict, right, tree_dict[right][0], tree_dict[right][1], print_list)
    
    return print_list


# 후위 순회
def postorder(tree_dict, root, left, right, print_list):
    # 왼쪽 자식이 있으면
    if left != '.':
        postorder(tree_dict, left, tree_dict[left][0], tree_dict[left][1], print_list)
    # 오른쪽 자식이 있으면
    if right != '.':
        postorder(tree_dict, right, tree_dict[right][0], tree_dict[right][1], print_list)
    # 리스트에 추가
    print_list.append(root)

    return print_list


N = int(input())
data_list = [input().split() for _ in range(N)]
solution(N, data_list)