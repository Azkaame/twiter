#twitter.py

x = input ("kata :").strip()

for alphabet in "aiueoAIUEO" :
    x = x.replace(alphabet, "").strip()

print(f'\n{x}')