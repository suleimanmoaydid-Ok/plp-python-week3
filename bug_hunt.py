count = 1
total = 0

# BUG: Changed < to <= so the loop includes 5 instead of stopping at 4.
# BUG: Added a colon because a while statement needs a colon before its loop body.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Converted total to a string so it can be joined with the text.
print("Sum of 1 to 5 is: " + str(total))
