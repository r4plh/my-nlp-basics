**BM25**, also known as Okapi BM25, is an advanced ranking function used in information retrieval to estimate the relevance of documents to a given search query. It improves on the simpler TF-IDF approach by incorporating document length and query term frequency in its scoring formula.

### The Components of BM25
BM25 scoring for a query against a document is computed as the sum of its components for each query term. Here are the main elements of the BM25 formula:

1. **TF (Term Frequency)**: Like in TF-IDF, term frequency measures how often a term appears in a document. However, BM25 modifies the TF component to prevent term frequency saturation.
   
2. **IDF (Inverse Document Frequency)**: This is similar to the IDF in TF-IDF but often calculated differently to better handle scenarios where documents do not contain the term.

3. **Document Length Normalization**: This component adjusts the score based on the length of the document compared to the average document length in the corpus, helping to avoid favoring longer documents.

### The Formula
The formula for BM25 for a term \( t \) in a document \( d \) is given as:

\[
\text{Score}(d, q) = \sum_{i=1}^{n} \text{IDF}(t_i) \cdot \frac{f(t_i, d) \cdot (k_1 + 1)}{f(t_i, d) + k_1 \cdot (1 - b + b \cdot \frac{\text{len}(d)}{\text{avgdl}})}
\]

where:
- \( q \) is the query containing terms \( t_1, t_2, ..., t_n \).
- \( f(t_i, d) \) is \( t_i \)'s term frequency in the document \( d \).
- \( \text{len}(d) \) is the length of the document \( d \) (total number of words).
- \( \text{avgdl} \) is the average document length in the text collection.
- \( k_1 \) and \( b \) are free parameters, usually chosen, in typical applications, as \( k_1 = 1.2 \) to \( 2.0 \) and \( b = 0.75 \).
- \( \text{IDF}(t_i) \) is the IDF of term \( t_i \), which can be computed as:
  \[
  \text{IDF}(t_i) = \log \left(\frac{N - n(t_i) + 0.5}{n(t_i) + 0.5} + 1\right)
  \]
  Here, \( N \) is the total number of documents, and \( n(t_i) \) is the number of documents containing the term \( t_i \).

### Example
Let's consider a simple example with the following parameters:
- Assume \( N = 1000 \) documents, and the term "apple" appears in 50 of these.
- In a specific document \( d \), "apple" appears 3 times, the length of \( d \) is 100 words, and the average document length \( \text{avgdl} \) is 150 words.
- We use common values for \( k_1 \) and \( b \) as 1.5 and 0.75, respectively.

**Calculation**:
1. **Calculate IDF for "apple"**:
   \[
   \text{IDF}(\text{"apple"}) = \log \left(\frac{1000 - 50 + 0.5}{50 + 0.5} + 1\right) \approx \log \left(\frac{950.5}{50.5} + 1\right) \approx \log(19.91) \approx 2.995
   \]
2. **Calculate BM25 for "apple" in \( d \)**:
   \[
   \text{Score}(d, \text{"apple"}) = 2.995 \cdot \frac{3 \cdot (1.5 + 1)}{3 + 1.5 \cdot (1 - 0.75 + 0.75 \cdot \frac{100}{150})} \approx 2.995 \cdot \frac{6}{3.75} \approx 4.794
   \]

This score indicates how relevant the document \( d \) is for the query term "apple," with adjustments for term frequency saturation and document length normalization. BM25 is particularly effective in information retrieval systems where document relevance and term specificity are critical.

Let's consider a query and three documents to calculate the BM25 scores for each document concerning the query. This example will demonstrate how BM25 evaluates document relevance based on multiple query terms across different document lengths.

### Example Query and Documents
**Query**: "blue red square"

**Document 1**: "blue square blue square red"
**Document 2**: "blue blue blue blue red"
**Document 3**: "red square green"

### Corpus Details
- Total number of documents, \( N \) = 3
- Average document length, \( \text{avgdl} \) (calculated as total words / number of documents) = (6 + 5 + 3) / 3 = 4.67

### Term Frequencies in Documents
- **Doc1**: "blue" = 2, "red" = 1, "square" = 2, Total words = 5
- **Doc2**: "blue" = 4, "red" = 1, Total words = 5
- **Doc3**: "red" = 1, "square" = 1, "green" = 1, Total words = 3

### Number of Documents containing each term
- \( n("blue") \) = 2 (Doc1, Doc2)
- \( n("red") \) = 3 (All)
- \( n("square") \) = 2 (Doc1, Doc3)

### Parameters for BM25
- \( k_1 = 1.5 \)
- \( b = 0.75 \)

### IDF Calculations for Each Term
Using the formula: 
\[ \text{IDF}(t) = \log \left(\frac{N - n(t) + 0.5}{n(t) + 0.5} + 1\right) \]

- \( \text{IDF}("blue") = \log \left(\frac{3 - 2 + 0.5}{2 + 0.5} + 1\right) \approx \log(1.83) \approx 0.604 \)
- \( \text{IDF}("red") = \log \left(\frac{3 - 3 + 0.5}{3 + 0.5} + 1\right) \approx \log(1.17) \approx 0.156 \)
- \( \text{IDF}("square") = \log \left(\frac{3 - 2 + 0.5}{2 + 0.5} + 1\right) \approx \log(1.83) \approx 0.604 \)

### BM25 Score Calculation for Each Document
Using the formula:
\[ \text{Score}(d, q) = \sum_{i=1}^{n} \text{IDF}(t_i) \cdot \frac{f(t_i, d) \cdot (k_1 + 1)}{f(t_i, d) + k_1 \cdot (1 - b + b \cdot \frac{\text{len}(d)}{\text{avgdl}})} \]

#### Document 1
\[
\begin{align*}
\text{Score}(d1, q) = & \; \text{IDF}("blue") \cdot \frac{2 \cdot (1.5 + 1)}{2 + 1.5 \cdot (1 - 0.75 + 0.75 \cdot \frac{5}{4.67})} \\
& + \text{IDF}("red") \cdot \frac{1 \cdot (1.5 + 1)}{1 + 1.5 \cdot (1 - 0.75 + 0.75 \cdot \frac{5}{4.67})} \\
& + \text{IDF}("square") \cdot \frac{2 \cdot (1.5 + 1)}{2 + 1.5 \cdot (1 - 0.75 + 0.75 \cdot \frac{5}{4.67})} \\
\approx & \; 0.604 \cdot 1.915 + 0.156 \cdot 1.370 + 0.604 \cdot 1.915 \\
\approx & \; 1.157 + 0.214 + 1.157 \\
\approx & \; 2.528
\end{align*}
\]

#### Document 2 and 3 can be calculated similarly, following the steps for each term in the query and summing up the results.

This BM25 calculation reveals how each document's relevance to the query is quantified, accounting for term frequency, document length, and term specificity across the corpus.