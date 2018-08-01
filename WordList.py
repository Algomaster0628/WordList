def WorldList(n):# Returns word in a given sentence including punctuation in alphabetical order.
  n = n.replace(';','').replace(':','').replace("'",'').replace(',','').replace('.','')
  n = n.lower()
  n = n.split()
  n.sort()
  return n
x = WorldList("This is a samp;:le pi;'ece of text to illust,rate this problem.")
for words in x:
  print(words)
