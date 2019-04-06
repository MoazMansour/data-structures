# Enter your code here. Read input from STDIN. Print output to STDOUT

def maxElement(arr):
    f = open('output.txt','w+')
    stack = []
    i = 0
    maxNum = [0]
    while i < len(arr):
        if arr[i] == 1:
            stack.append(arr[i+1])
            if arr[i+1] >= maxNum[-1]:
                maxNum.append(arr[i+1])
            i += 2
            continue
        if arr[i] == 2:
            if stack:
                v = stack.pop()
                if v == maxNum[-1]:
                    maxNum.pop()
            i += 1
            continue
        if arr[i] == 3:
            # f.write(str(max(stack))+'\n')
            f.write(str(maxNum[-1])+'\n')
            i += 1
    f.close()

def main():
    read = []
    with open('input.txt') as f:
        content = f.readlines()
    for line in content:
        read += (map(int, line.split()))
    maxElement(read)


if __name__ == "__main__":
    main()
