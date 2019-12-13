import math

'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th2(word):
    count = 0
    if len(word) == 0: return 0
    for char in range(len(word) -1):
      # print(char)
      if word[char] == "t" and  word[char + 1]== "h":
            count += 1 
    return count

def count_th(word):
      count = 0
      if len(word) < len("th"):
            return 0
      if len(word) == len("th"):
            if word == "th":
                  return 1
            else:
                  return 0
      
      sub1 = ""
      sub2 = ""
      midpoint = math.floor(len(word) / 2)
      sub1 = word[:midpoint]
      sub2 = word[midpoint:]
      # print(sub1)
      # print(sub2)
      count1 = count_th2(sub1)
      count2 = count_th2(sub2)
      count3 = 0
      if sub1[-1] == "t" and sub2[0] == "h":
            count3 = 1
      return count1 + count2 + count3



# if char == t or h and index of t == index of h - 1
#   count + 1

test = count_th("abcthxyz")
print(test)