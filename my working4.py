ItemCart = 0
if ItemCart != 1:
    # raise Exception("You can't go anymore")
    pass

# assert(ItemCart == 1) # rise error
assert(ItemCart == 0) # not raise error

try:
    with open("joker.txt", "r") as reader:
        reader.read()
# except:
#     print("joker left the chat")
except Exception as e:
    print(e)

finally:
    print("clean up your mess")