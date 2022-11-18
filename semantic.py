import spacy

nlp = spacy.load("en_core_web_md")

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# I have noticed that the cat and the monkey score higher on the similarity because they are both
# animals.  Moreover, banana and monkey are more similar because people associate them with each other
# rather than the cat and the banana.

word4 = nlp("car")
word5 = nlp("airplane")
word6 = nlp("truck")

print(word4.similarity(word5))
print(word6.similarity(word5))
print(word6.similarity(word4))

# In my own example, truck and car have high similarity because they are both ground vehicles
# as compared to planes


tokens = nlp ("cat apple monkey banana")

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# Similar to the above, apple and banana are closer to each other because they are fruits
# as  monkey and cat are animals.  Also monkey and banana is similar than monkey, apple, and cat, apple
# cat banana because of how we associate bananas with monkeys

sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
             "Hello, there is my car",
             "I\'ve lost my car in my car",
             "I\'d like my boat back",
             "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

# I have noticed that with the code above, there is increased similarity with the mention
# of the word car. Moreover, the comparing a sentence with an animal such as dog in the first and the
# last sentence also increases the similarity.


# === Example File ====

# Running the example and comparing en_core_web_md against en_core_web_sm, I have found that there
# is a higher similarity between the recipes, complaints and recipes anc complaints with en_core_web_md.
#  The similarity value was abovoe 0.5+.  Where as when I ran it on simpler language, the similarity value
# value came down.