Please use this Google doc to code during your interview. To free your hands for coding, we recommend that you use a headset or a phone with speaker option.




     F
    / \
   /   \
 [B]    G
 / \     \
A   D    [I]
   / \   /
  C   E H


A  F      D    H
    \    / \
     G  C   E

Node:
node.left
node.right

# Given
shouldErase(node)

# To Implement
getForest(node)


def getForest(node):
	result = []
	childs = (node.left, node.right)
	if node.left:
    	if shouldErase(node.left):
    		node.left = None
    	elif shouldErase(node):
    		result.append(node.left)
    if node.right:
    	if shouldErase(node.right):
    		node.right = None
    	elif shouldErase(node):
    		result.append(node.right)
	if not shouldErase(node) and (node not in result):
		result.append(node)
	for child in childs:
        if child:
		          result += getForest(child)
	return result









node: F, B, A
childs: B, G, A, D
return: False
if shouldeErase(node): True

result: [A]
F -> G
Output: List of trees
