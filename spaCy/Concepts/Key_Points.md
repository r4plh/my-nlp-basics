
Lexical attributes refer to properties of words or tokens based on their form or appearance in text, without considering context or grammar. These attributes describe how a word looks or behaves as a string.
Linguistic attributes require a model’s predictions and rely on context, whereas lexical attributes are context-independent.

Difference Between Lexical and Linguistic Attributes:
Lexical Attributes: Based on the token’s form (e.g., TEXT, IS_ALPHA).
Linguistic Attributes: Based on the token’s role and meaning in context (e.g., POS, NER etc).

1. **Doc**: A **container** for linguistic annotations, represented as a sequence of `Token` objects, internally stored as a Cython-based (C++ for efficiency) structure for efficiency.
2. **Vocab**: A **hash table-backed data structure** that maps strings to unique hash IDs and stores linguistic annotations like word attributes, labels, and entities.
3. **String Store**: A lookup table (hash map) within the Vocab that maps strings to unique hash IDs and vice versa, enabling efficient bidirectional access.

![Doc , Vocab , String Store](<Screenshot 2024-12-22 at 6.29.20 PM.png>)



