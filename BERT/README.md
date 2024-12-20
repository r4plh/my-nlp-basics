# Comprehensive Overview of BERT

This README provides a detailed summary of key concepts and functionalities of the BERT (Bidirectional Encoder Representations from Transformers) model, based on my personal key findings , which I feel was very important from understanding pre-training and fine-tuning of BERT. It's not a general summary which summarizes the whole paper , I just wanna write down the most important key take aways that one might miss to understand.

## Table of Contents
1. [Introduction](#introduction)
2. [Tokenization](#tokenization)
3. [Model Training and Masking Strategy](#model-training-and-masking-strategy)
4. [The Use of the `[CLS]` Token](#the-use-of-the-cls-token)
5. [Task-Specific Applications](#task-specific-applications)
6. [Evaluation Metrics in QA](#evaluation-metrics-in-qa)
7. [Handling Unanswerable Questions](#handling-unanswerable-questions)
8. [Conclusion](#conclusion)

## Introduction
BERT, or Bidirectional Encoder Representations from Transformers, represents a significant advance in the field of Natural Language Processing (NLP). Developed by Google, BERT's key innovation is its ability to pre-train on a large corpus of text and then fine-tune on specific tasks, which include a broad range of applications from question answering to language inference.

## CLS input token ---> corresponding vector embedding is reffered as C 

## Understanding The different tasks
Natural Language Inference - Sentence Level Task (CLS Token is useful) , Input - Pair of sentences
Sentiment Analysis - Sentence Level Task (CLS Token is useful) , Input - Single sentence
Paraphrase Detection - Sentence Level Task (CLS Token is useful) , Input - Pair of sentence
NER - Token Level (Output tokens are useful , CLS is not useful) , Input - Single sentence
POS - Token Level (Output tokens are useful , CLS is not useful) , Input - Single sentence
Extractive Question Answering - Token Level (Output tokens are useful , CLS is useful) , Input - Pair of sentence
More of less these are main NLP tasks.

## Tokenization
### WordPiece Tokenization
BERT utilizes the WordPiece tokenizer, which is an efficient and dynamic subword tokenization method that enables the model to handle a wide range of vocabularies without significantly increasing the complexity of the model. (30,000 vocab length)

## Model Training and Masking Strategy
### Training Objectives
BERT is pre-trained using two strategies:
1. Masked Language Model (MLM)
2. Next Sentence Prediction (NSP)

### Masking Strategy
During the MLM pre-training, BERT randomly masks tokens in the input data and learns to predict them based on their context, using the following approach:
- **80%** of the time, tokens are replaced with `[MASK]`.
- **10%** of the time, tokens are replaced with a random token.
- **10%** of the time, tokens are left unchanged.

This strategy helps BERT to effectively learn a deep bidirectional understanding of the language context.

The loss function acts upon all the 15% of the mask tokens , that is including 80% MASK ones , 10% random tokens , 10% unchanged , on all the tokens the loss fucntion is applied , the loss is calculated against ground truth in all of the above cases.

Why above strategy is used for pre-training , is becasue in real life fine-tuning tasks , the inputs will not contain the [MASK] token , and if in pre-training , the focus is only made on [MASK] tokens , then it would not perform good on the down stream NLP tasks which don't have MASK tokens , so to generalize , model not only learns for MASK tokens but they learn the representation in better sense and represent token embeddings in more-contextual way as compared to , if the pre-training has been done on only MASK tokens.

## The Use of the `[CLS]` Token
The `[CLS]` token plays a crucial role in BERT's architecture:
- For sentence-level tasks (e.g., classification), the `[CLS]` token's final hidden state is used as the feature vector for classification.
- In question answering tasks, while the token-level predictions determine the answer span, the `[CLS]` token can help determine if the question is answerable or not.
- Generally CLS token is not useful in token level tasks

## Task-Specific Applications
BERT excels in various NLP tasks, including:
- **Extractive Question Answering**: Using token embeddings to identify answer spans within the text.
- **Natural Language Inference (NLI)**: Utilizing the `[CLS]` token to classify the relationship between two sentences.
- **Named Entity Recognition (NER)** and **Part-of-Speech (POS) Tagging**: Leveraging token-level outputs.

## Evaluation Metrics in QA
In extractive QA tasks, BERT is evaluated using:
- **Exact Match (EM)**: This metric measures the percentage of predictions that match any of the ground truth answers exactly. For a prediction to be counted as correct, it must match one of the actual answers exactly, word for word. This is a strict metric because even minor discrepancies, such as extra spaces or punctuation, can result in a mismatch.
- **F1 Score**: This metric considers both the precision and recall of the predictions. It calculates the number of correct token overlaps divided by the union of tokens in the predicted and ground truth answers. The F1 score is more forgiving than the Exact Match because it allows for partial credit if some of the words in the predicted answer are correct, even if the entire sequence isn’t exactly the same.

Precision in this context is the proportion of the words in the predicted answer that are found in the ground truth answer.
Recall is the proportion of the words in the ground truth answer that are found in the predicted answer.

## Handling Unanswerable Questions
BERT has been extended to handle unanswerable questions by:
- Predicting an answer span at the `[CLS]` token when no suitable answer is found in the context.
- Using a threshold to decide between a non-null span and a null response, improving its utility in datasets like SQuAD 2.0.

## Conclusion
BERT's innovative approach to bidirectional training and its versatility across different tasks make it a cornerstone in the evolution of NLP technologies. Its ability to adapt to various languages and contexts continues to inspire a wide range of applications in the field.

---
