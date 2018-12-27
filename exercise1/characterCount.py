message = 'You have been so amazing at what you do, though you still spend a lot of time before getting things done'
count = {}

for alphabet in message:
	count.setdefault(alphabet, 0)
	count[alphabet] = count[alphabet] + 1

print(count)
