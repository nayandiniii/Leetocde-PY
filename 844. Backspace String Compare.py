class Solution(object):
    def backspaceCompare(self, s, t):
        # we create stacks to store the characters
        s_stack = []
        t_stack = []

        for char in s:
            if char != '#':
                s_stack.append(char)
            elif s_stack: # pops the element before '#'
                s_stack.pop()

        for char in t:
            if char != '#':
                t_stack.append(char)
            elif t_stack:
                t_stack.pop()

        return s_stack == t_stack
