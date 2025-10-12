def somefunction(s):
    uniques = set()
    for i in s:
        uniques.add(i)
    uniqLen = len(uniques)
    ans = 0
    for i in range(len(s)):
        nary = {}
        for j in range(i, len(s)):
            if s[j] in nary:
                nary[s[j]] += 1
            else:
                nary[s[j]] = 1
            if len(nary) == uniqLen:
                eq_count = nary[0]
                isPoss = True
                for k in nary.values():
                    if k != eq_count:
                        isPoss = False
                if isPoss:
                    ans = max(ans, eq_count * uniqLen)
    return ans