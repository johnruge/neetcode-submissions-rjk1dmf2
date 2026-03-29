class Solution:
    def encode(self, strs: List[str]) -> str:
        res = []
        for string in strs:
            res.append(str(len(string)))
            res.append("#")
            res.append(string)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        l, r = 0, 1
        while r < len(s):
            while s[r] != "#":
                r += 1
            len_curr = int(s[l:r])
            res.append(s[r + 1:r + len_curr + 1])
            l = r + len_curr + 1
            r = l + 1

        return res

