from googletrans import Translator

sentence = str(input("say......"))

translator = Translator()

translated_sentence = translator.translate(sentence, src="en", dest="ca")

print(translated_sentence.text)
