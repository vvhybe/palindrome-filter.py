import json, time, os

print("─"*30+"Palindrome Word Checker"+"─"*30)

def is_one_letter_word(word:str)->bool:
    return [word[l] == word[l+1] for l in range(len(word)-1)][0]

def palindrome_filter(fsuf="l", fltr="normal"):
    fsuf = fsuf in ['l','m','h'] and fsuf or "l"
    print(f">> runnig filter on '{fsuf}' simple.")
    with open(f'words_{fsuf}.json', 'r') as json_words:
        lts = time.time() # load time start
        words = json.load(json_words)
        fts = time.time() # filter time start
        palindrome_words = fltr.lower() =="deep" and [pw for pw in words["words"] if len(pw) > 1 and not is_one_letter_word(pw) and list(pw.lower()) == list(reversed(pw.lower()))] or [pw for pw in words["words"] if len(pw) > 1 and list(pw.lower()) == list(reversed(pw.lower()))] 
        fte = time.time() # filter time end
        print(f">> Filter results: ({len(palindrome_words)} res).")
        print("palindrome words: ",palindrome_words)
        print("─"*12,"Processing Time results:", "─"*80)
        print(f"--#: To filter palindromes words from '{json_words.name}:{(os.stat(json_words.name).st_size / 1024**2):.3f}MB' it take's {fte - fts}s")
        print(f"--#: To load/filter palindromes words from '{json_words.name}:{(os.stat(json_words.name).st_size / 1024**2):.3f}MB' it take's {fte - lts}s")

print("you have 3 simples: ","['l']:light(<=1000 word)", "['m']:meduim(<=10000 word)", "['h']:heavy(<=370000 word)")
palindrome_filter(input("what's simple you want to filter it ['l','m','h']: "), fltr="deep")
print("─"*120)