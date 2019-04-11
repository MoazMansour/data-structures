#!/usr/bin/env python3

'''
    The function determines if the text and pattern are the equal,
    where the '.' is treated as a single a character wildcard, and '*' is matched for a zero
    or more sequence of the previous letter
'''

def star(char, arr):
    '''This function checks all following letters in a test string is equal
        to a constant char that comes after a star.
        retrun cond:
            - if charachers are not equal
            - if test string ran out of characters
        input:
            - constant char for testing
            - test string stack
        returns:
            - test string stack after eliminating the tested characters
        '''
        tchar = arr.pop()
        # if the pattern char is the wildcard '.'
        # takes the matching char in the test string as the constant
        if char == '.':
            char = tchar
        while char == tchar:
            if arr:
                tchar = arr.pop()
                continue
            break
        if char != tchar:
            arr.append(tchar)
        return arr


def compare(p, t):
    '''compares to stack of characters to be equal
    takes input
    while p and t:
        char = p.pop()
        tchar = t.pop()
        if char == '.':
          continue
        if char == '*':
          char = p.pop()
          t.append(tchar)
          t = star(char, t)
          continue
        if char != tchar:
          return False
    if p:
        while p and p.pop() == '*':
          p.pop()
        if p:
          return False
    if t:
        return False
    return True

def is_match(text, pattern):
  if text == pattern:
    return True
  text_stack = []
  pattern_stack = []
  for char in text:
    text_stack.append(char)
  for char in pattern:
    pattern_stack.append(char)
  return compare(pattern_stack, text_stack)


def main():
  print (is_match("aaa", "b*c*a*a*"))

if __name__ == '__main__':
  main()
