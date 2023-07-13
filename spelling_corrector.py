from textblob import TextBlob

file1 = open("1.txt", "w+")


# Write some text to the file
#file1.write("original text")

# Reset the file pointer to the beginning of the file
#file1.seek(0)


a = file1.read()
print("original text : " + str(a))
b = TextBlob(a)

print("corrected text: " + str(b.correct()))
file1.close()

d = open("1.txt", "w")
d.write(str(b.correct()))
d.close()
