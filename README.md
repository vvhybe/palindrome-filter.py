# palindrome-filter.py
python algorithm to check for palindrome English words in 3 json files.
palindrome words like "mom", "dad", "eye" you can read theme from left to right (ltr) and right to left (rtl).

File         | Code         | words quantity | approximate filter time (s)
------------ | ------------ | -------------- | ----------------------------
words_l.json | `l`:[light]  |    <= 1000     |            0.001s
words_m.json | `m`:[medium] |    <= 10000    |            0.05s
words_h.json | `h`:[heavy]  |    <= 370000   |            1.6s
