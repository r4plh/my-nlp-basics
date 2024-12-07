TF-IDF is a technique to represent a whole sentence/document through one embedding , unlike transformers which represent every word by one embedding and the size of representation of one sentence becomes n x m , n - embedding size of a word , m - total number of words in sentence.

Inverse Document Frequency (IDF) is calculated for every word in the vocabulary and is the same across all documents for a given word. It measures how common or rare a word is across the entire corpus. The IDF for a word does not change from one document to another; it is a measure of the general importance of the word across all documents.

Term Frequency (TF) is calculated for each word within a specific document or sentence. It measures how frequently a word appears in that particular document or sentence. Therefore, the same word can have different TF values in different documents depending on how often it appears in each one.

Let's say we have a paragraph and we sentence tokenize it and get the following sentence -  

"The quick brown fox jumps over the lazy dog." - S1
"The quick brown fox is quick." - S2
"Jumping foxes are quick and can jump high." - S3 

Step-by-Step TF-IDF Calculation:

1. Preprocessing:

Sentence Tokenization: Each document is already a single sentence. (Already applied that's why we have sentences.)
Word Tokenization: Split each sentence into individual words. So as to calculate TF and IDF values , because these calculation are done over words only and over the words which are made after word tokenization. This gives the total unique words present in our corpus , that is this process forms our vocabulary.
Cleaning: Convert all words to lowercase to standardize them.
Stopword Removal: Remove common words that might not be useful in analysis (like "the", "is", "are") , that are not considered that much essential to represent the meaning of a document or sentence.
Lemmatization: Convert words to their base form (e.g., "jumping" to "jump", "foxes" to "fox").

2. Calculate Term Frequency (TF):

Term frequency is calculated for every sentence , that is for every word present in a sentence , the same word occuring in two sentence may have different term frequency , the term frequency for a word not occuring in a sentence is 0.
Term Frequency = No of repitation of word in sentence / Total words in the sentence
Count how often each word appears in each document.
Divide by the total number of words in that document.
Example: In Document 2, "quick" appears twice out of six total words, so its TF in Document 2 is 2/4. (Becasue we have revomed the stopwords - [The , is])

3. Compute Inverse Document Frequency (IDF):

The IDF is calculated for every word present in the vocabulary , that is the same word occuring in two sentences will have same IDF always , the IDF of a word which is present in every sentence/document is 0.
Use the formula: IDF = log(Total Number of Documents or sentences / Number of Documents/sentences containing the Word).
Example: If "quick" appears in all three documents, and there are three documents, its IDF is log(3/3) = 0, after smoothing it might slightly differ.


4. Calculate TF-IDF:

Multiply the TF of each word by its IDF.
This score represents the importance of a word in a document, balanced by how common it is in the entire corpus.
Example: The TF-IDF for "quick" in Document 2 is (2/4) * 0 = 0 (considering the simple IDF without smoothing).

6. Vector Representation:

Each document is represented as a vector, where each dimension corresponds to a different word from the entire corpus / whole vocabulary of all documents/sentences.
The values in the vector are the TF-IDF scores for each word.
Example: If our vocabulary sorted alphabetically is ["brown", "dog", "fox", "high", "jump", "jumps", "lazy", "over", "quick"], then each sentence is represented as a vector with these dimensions, filled in with the corresponding TF-IDF scores for words present in the document.

Vector embeddings - ["brown", "dog", "fox", "high", "jump", "jumps", "lazy", "over", "quick"] , length of the vocab is 10 , so every sentence would be represented by a vector of size 10.

Sentence 1 Vector - [0, 0.029, 0.029, 0.080, 0.080, 0.080, 0, 0, 0, 0]

Sentence 2 Vector - [0, 0.044, 0.044, 0, 0, 0, 0, 0, 0, 0]

Sentence 3 Vector - [0, 0, 0, 0, 0, 0, 0.095, 0.095, 0.095, 0.095]
