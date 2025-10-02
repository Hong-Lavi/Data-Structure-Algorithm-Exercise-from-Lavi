def replace_word(txt,old,new):
    return txt.replace(old,new)

def to_upper(txt):
    return txt.upper()


txt= "I love Python"
old="Python"
new="C++"

print(replace_word(txt,old,new))
print(to_upper(txt))
