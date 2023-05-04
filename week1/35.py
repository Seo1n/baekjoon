import sys
input = sys.stdin.readline()
N = int(input())
word_list= []
sorted_word = []

for i in range(N):
    a =(input())
    word_list.append(a.rstrip())
    
set_word = list(set(word_list))
for i in set_word:
    sorted_word.append((len(i), i))

result = sorted(sorted_word)

for num, word in result:
    print(word)
   




   
       
