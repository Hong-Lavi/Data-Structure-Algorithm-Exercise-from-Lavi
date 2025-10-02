def remove_space(txt):
    return txt.replace(" ", "")

def is_numeric(txt):
    return txt.isdigit()

def contain(maint, subt):
    if subt in maint:
        return True
    else:
        return False

txt1="I like an Apple"
txt2="142840"
maint="Hello World"
subt="World"

print(remove_space(txt1))
print(is_numeric(txt2))
print(contain(maint,subt))
