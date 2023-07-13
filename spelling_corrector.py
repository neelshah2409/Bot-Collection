from textblob import TextBlob

file1 = open("1.txt", "w+")
a = file1.read()
print("original text : " + str(a))
b = TextBlob(a)

print("corrected text: " + str(b.correct()))
file1.close()

d = open("1.txt", "w")
d.write(str(b.correct()))
d.close()
