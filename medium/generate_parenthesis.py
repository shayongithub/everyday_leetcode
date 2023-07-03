from typing import List


def generateParenthesis(n: int) -> List[str]:
    # if the number of open parentheses is smaller than n, add '('
    # if the number of close parentheses is smaller current open parentheses, add ')'.
    # if and only if the number of open parentheses = close parentheses = n, add it to the list

    stack = []  # a way to hold each valid parenthesis
    ans = []

    def backtrack(openedN, closedN):
        if openedN == closedN == n:
            # add the valid parenthesis to the list and exit the loop
            ans.append("".join(stack))
            return

        # when the first recursion ends normally with all the open parentheses listed e.g. (((
        # all the closed parentheses will be added and pop out after each recursion to prepare for the next possible answer
        # however, the first open parentheses will never be popped out 
        
        if openedN < n:
            stack.append("(")
            # increment open parentheses as we add it above
            backtrack(openedN + 1, closedN)
            stack.pop()

        if closedN < openedN:
            stack.append(")")
            # increment close parentheses as we add it above
            backtrack(openedN, closedN + 1)
            stack.pop()

    backtrack(0, 0)

    return ans


if __name__ == "__main__":
    n = 2
    print(generateParenthesis(n))
