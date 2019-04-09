# Enter your code here. Read input from STDIN. Print output to STDOUT

def isBalanced(s):
    left = ['(','[','{']
    right = [')',']','}']
    stack = []
    for char in s:
        if char in left:
            stack.append(left.index(char))
        else:
            if stack:
                end = stack.pop()
                if (right.index(char) != end):
                    return 'NO'
            else:
                return 'NO'
    if stack:
        return 'NO'
    return 'YES'

def main():
    with open('input.txt') as f:
        content = f.readlines()
    content = [ x.strip() for x in content]
    f = open('output.txt','w+')
    for string in content:
        f.write(isBalanced(string) + '\n')


if __name__ == "__main__":
    main()
