class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mappings = {
            "2":"abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = [i for i in mappings[digits[0]]]
        for i in digits[1:]:
            X = []
            for p in res:
                for j in mappings[i]:
                    X.append(p + j)
            res = X
        return res