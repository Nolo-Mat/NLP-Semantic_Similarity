import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("car")
word2 = nlp("truck")
word3 = nlp("plane")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))


tokens = nlp('cat apple monkey banana ')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


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


# Note on Similarities:
# I found it interesting that the word vectors for "cat" and "monkey" were more similar to each other than to "banana." 
# This suggests a certain level of semantic similarity between animals. It makes sense since both "cat" and "monkey" are mammals, while "banana" is a fruit.


# Note on my own Example:
# I also found it interesting that the words "car" and "truck" were more similar to each other than to "plane."
# This suggest that while they all might be modes of transport, there is a higher degree of semantic similarity between 
# the two vehicles since a plane is more of an aircraft.


# Note on The Difference Between Language Models:
# I noticed that the overall values that represent semantic similarity have generally decreased when compared using the smaller ‘en_core_web_sm’ language model.
# This is like due to the fact that this smaller model doesn't have any word vectors loaded and therefore can't provide semantic similarity judgement 
# with the same accuracy as the larger ‘en_core_web_md’ language model. This means that the complaints and recipes being compared could have much higher or 
# lower semantic similarity than the values represented using the 'en_core_web_sm' language models.



