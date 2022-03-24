people = [1,2]
limit = 3
cnt = 0
people.sort()
start = 0
end = len(people) - 1
while start <= end:
    if start < end and people[start] + people[end] <= limit:
        start += 1
    end -= 1
    cnt += 1
return cnt