def swap(s, a, b):
    s = s[:a] + s[b] + s[a+1:b] + s[a] + s[b+1:]
    return s


t = int(input())
for i in range(t):
    s, c = input().split()
    if s > c:
        same = 0
        for j in range(1, len(s)):
            if s[0] != s[j]:
                same = j
                break
        a = same
        for j in range(same, len(s)):
            if s[j] < s[a]:
                a = j
        b = 0
        for j in range(a):
            if s[a] < s[j]:
                b = j
                break
        s = swap(s, b, a)
        if s < c:
            print(s)
        else:
            print('---')
    else:
        print(s)
