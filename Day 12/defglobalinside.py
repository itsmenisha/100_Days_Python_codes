nisha = ["genius"]


def test_genius():
    global nisha
    nisha.append("Amazing Human")
    print(nisha)


test_genius()
print(nisha)
# prints 2 times,['genius', 'Amazing Human']
