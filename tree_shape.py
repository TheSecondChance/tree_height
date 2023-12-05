"""Tree shap"""
tree_l = int(input("Enter Tree Hight: "))

space = tree_l - 1
hash = 1
f_space = tree_l - 1

while tree_l != 0:
    for i in range(space):
        print(' ', end="")
    for i in range(hash):
        print('#', end="")
    print()
    space -= 1
    hash += 2
    tree_l -= 1
for i in range(f_space):
    print(' ', end="")
print("#")
