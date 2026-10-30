class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        stickerCount = []
        # build frequency maps for each sticker
        for i, s in enumerate(stickers):
            stickerCount.append({})
            for c in s:
                stickerCount[i][c] = 1 + stickerCount[i].get(c, 0)

        dp = {} # key = subsequence of target, val = min num stickers

        def dfs(t, sticker):
            if t in dp:
                return dp[t]
            if t == "":
                return 0

            result = 1 if sticker else 0 # 1 sticker used
            remainingChars = ""
            for c in t:
                if c in sticker and sticker[c] > 0:
                    sticker[c] -= 1
                else:
                    remainingChars += c

            # if we have more chars left then explore
            if remainingChars:
                used =  float("inf")

                for s in stickerCount:
                    if remainingChars[0] not in s:
                        continue
                    used = min(used, dfs(remainingChars, s.copy()))

                dp[remainingChars] = used
                result += used

            return result
                

            
        result = dfs(target, {})
        return result if result != float("inf") else -1