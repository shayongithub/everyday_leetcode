def climbStairsRecursionWithMemo(n: int) -> int:
    def climb(n):
        if n in memo:
            return memo[n]
        else:
            memo[n] = climb(n - 1) + climb(n - 2)

        return memo[n]

    memo = {1: 1, 2: 2}

    return climb(n)


def climbStairsDP(n: int) -> int:
    """Using bottom-up technique"""

    if n <= 2:
        return n

    # Create a list containe n+1 elements:
    dp = [0] * (n + 1)

    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def climbStairDPWithSavingMemo(n: int) -> int:
    if n <= 2:
        return n

    ans = 0

    first_prev = 2
    second_prev = 1

    for _ in range(3, n + 1):
        ans = first_prev + second_prev

        first_prev, second_prev = ans, first_prev

    return ans


if __name__ == "__main__":
    n = 4
    climbStairDPWithSavingMemo(n)
