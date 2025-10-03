def toggle(text):
    ans_text=""
    for i in text:
        if i.isupper():
            ans_text+=i.lower()
        else:
            ans_text+=i.upper()
    return ans_text

text="Hello Python"

print(toggle(text))



