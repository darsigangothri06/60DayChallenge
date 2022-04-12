start = 1
end = n
if n == 1:
    return 1
while start <= end:
    mid = (start + end) // 2
    if isBadVersion(mid):
        if not isBadVersion(mid-1):
            return mid
        end = mid - 1
    if not isBadVersion(mid):
        start = mid + 1