# coding=utf-8
# without context manager
f = open("new.txt", "w")
print(f.closed)               # whether the file is open
f.write("Hello World!")
f.close()
print(f.closed)

# with context manager
with open("new.txt", "w") as f:
    print(f.closed)
    f.write("Hello World!")
print(f.closed)


# customized object

class VOW(object):
    def __init__(self, text):
        self.text = text
    def __enter__(self):
        self.text = "I say: " + self.text    # add prefix
        return self                          # note: return an object
    def __exit__(self,exc_type,exc_value,traceback):
        self.text = self.text + "!"          # add suffix


with VOW("I'm fine") as myvow:
    print(myvow.text)

print(myvow.text)

# 没怎么理解

