def generateParenthesis(n):
    dp = [[] for _ in range(n + 1)]

    dp[0].append('')
    dp[1].append('()')
    for i in range(2, n + 1):
        for j in range(0, i):
            end = dp[i - j - 1]
            front = ['(' + x + ')' for x in dp[j]]
            for f in front:
                for e in end:
                    dp[i].append(f + e)
    return dp[n]

print(generateParenthesis(3))