# While común
print("While")
i = 0
while i < 10:
    i += 1
    print(i)

# While - Break
print("Break")
i = 0
while i < 10:
    i += 1
    if i >= 3:
        break
    print(i)

# While - Continue
print("Continue")
i = 0
while i < 10:
    i += 1
    if i < 6:
        continue
    print(i)