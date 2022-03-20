digits = "23"
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
if len(digits) == 1:
    return list(mappings[digits])
nums = list(mappings[digits[0]])
for i in digits[1:]:
    nums = [old + new for old in nums for new in mappings[i]]
return nums