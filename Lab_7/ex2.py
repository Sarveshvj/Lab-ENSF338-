print("\nTest Case 1: Case #1 (No Pivot)")
tree1 = BST()

inputs1 = [50, 30, 70]   # Balanced insertions

for x in inputs1:
    tree1.insert(x)

print("\nTest Case 2: Case #2 (Insert into shorter subtree)")
tree2 = BST()

inputs2 = [50, 30, 70, 20, 40]  

for x in inputs2:
    tree2.insert(x)

print("\nTest Case 3: Case #3 (Not Supported)")
tree3 = BST()

inputs3 = [50, 40, 30]   # Left-Left imbalance

for x in inputs3:
    tree3.insert(x)

print("\nTest Case 4: Case #3 (Right-heavy imbalance)")
tree4 = BST()

inputs4 = [50, 60, 70]   # Right-Right imbalance

for x in inputs4:
    tree4.insert(x)



