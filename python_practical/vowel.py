def vowel(input):
  vowel = "aeiou"
  count = 0
   
  for char in input:
    if char in vowel:
        count = count + 1
  return count   

input="hello world"
totalcount = vowel(input)
print(f"the vowel is: {totalcount}")