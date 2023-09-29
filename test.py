import re
from helper import edit_very_special_syms

# text = "The cat is // a a concatenation of categories. cat cat cat"
text = "a+b a-b a/b a//b a*b a**b a%b a+=b a-=b a/=b a//=b a*=b a**=b a%=b a==b a=b a!=b a<b a>b a<=b a>=b a<<b a>>b a|b a&b a^b a~b"

# Match the word "cat" as a whole word
sym = edit_very_special_syms('*')
pattern = rf'(?<![/*=\+\-\%\<\>!]){sym}(?![=/*\<\>])'

print(re.findall(pattern, text))
