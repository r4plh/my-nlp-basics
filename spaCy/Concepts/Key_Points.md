## Lexical vs. Linguistic Attributes

- **Lexical Attributes**: Properties based on a token's form or appearance (e.g., `TEXT`, `IS_ALPHA`). Context-independent.
- **Linguistic Attributes**: Properties based on a token's role and meaning in context (e.g., `POS`, `NER`). Require model predictions.

---

## Key Data Structures in spaCy

1. **Doc**: A container for linguistic annotations, represented as a sequence of `Token` objects. Internally stored as a Cython-based structure for efficiency.
2. **Vocab**: A hash table-backed data structure mapping strings to unique hash IDs, storing linguistic annotations like word attributes, labels, and entities.
3. **String Store**: A lookup table (hash map) within the `Vocab` that maps strings to unique hash IDs and vice versa, enabling efficient bidirectional access.

![Doc, Vocab, String Store](<Screenshot 2024-12-22 at 6.29.20 PM.png>)

---

## Doc and Span Performance
- The **Doc** and **Span** objects are optimized for performance, offering access to references and relationships between words and sentences.
- Convert `Doc` objects to strings as late as possible to avoid losing token relationships.
- Use built-in token attributes (e.g., `token.i`) to maintain consistency.

---

## Combining Statistical and Rule-Based Models
- Combining **statistical models** with **rule-based patterns** enables powerful and flexible text processing.

![Statistical model + Rule-Based Model Use Cases](<Screenshot 2024-12-22 at 11.13.29 PM.png>)

---

## Common Token Attributes in spaCy

1. **`text`**: Exact text of the token.
2. **`lower`**: Lowercase form of the token.
3. **`is_digit`**: Boolean indicating if the token consists of digits only.
4. **`lemma_`**: Base or dictionary form of the token.
5. **`pos_`**: Part-of-speech tag of the token.
6. **`is_alpha`**: Boolean indicating if the token contains only alphabetic characters.
7. **`is_punct`**: Boolean indicating if the token is punctuation.
8. **`shape_`**: Describes the token’s word shape (e.g., capitalization, digits).

---

## Pattern Matching in spaCy

### **Pattern**
- A pattern is a list of dictionaries where each dictionary defines the attributes of a token to match (e.g., `TEXT`, `LOWER`, `POS`).

### **Matcher**
- A rule-based engine that uses patterns to find specific sequences of tokens in a `Doc`.
- Matches are returned as `(match_id, start, end)` tuples.

---

## Multi-Word Pattern Matching

1. Define a list of dictionaries where each dictionary represents one token in the sequence.
2. Use attributes like `TEXT`, `LOWER`, or `LEMMA` for flexibility.
3. Use operators (`OP`) for optional or repeated tokens.
4. Add the pattern to the matcher and apply it to the `Doc`.

### Example of Flexible Matching
- Match case-insensitive words or optional tokens using `LOWER` and `OP`:
  - `"?"`: Matches 0 or 1 occurrence.
  - `"+"`: Matches 1 or more occurrences.
  - `"*"`: Matches 0 or more occurrences.

---

## spaCy Vocabulary and Hashing

### **Vocab**
- Centralized data store for shared linguistic data (e.g., words, labels, annotations).
- Optimizes memory by storing repeated words or labels only once and referring to them using hash IDs.

### **Hashing**
- Converts strings (e.g., words, labels) into fixed-size hash IDs using a hash function.
- Saves memory and allows fast comparisons.

### **String Store**
- A lookup table in the `Vocab` mapping strings to hash IDs and vice versa.
- Enables bidirectional access:
  - Look up a string to get its hash ID.
  - Look up a hash ID to get its string (if in the vocab).

### **Why Pass the Vocab?**
- Hash IDs are one-way and irreversible without the vocabulary.
- To interpret hash IDs in saved or processed data, the shared `Vocab` is required.

---

## Summary
- The `Vocab` centralizes shared data for memory efficiency and faster processing.
- Words and labels are hashed into IDs to avoid duplication.
- The `String Store` enables efficient mapping between strings and hash IDs.
- Patterns and matchers allow rule-based matching of even complex structures in text.
- Combining statistical models with rule-based patterns unlocks powerful NLP workflows.


The difference between `LOWER` and `TEXT` in spaCy's Matcher is:

- **`TEXT`**: Matches the exact text of a token, case-sensitive.  
  - Example: `"Apple"` matches `"Apple"` but not `"apple"`.

- **`LOWER`**: Matches the lowercase form of the token, case-insensitive.  
  - Example: `"Apple"` matches `"apple"`, `"APPLE"`, and `"Apple"`. 

Use `LOWER` for case-insensitive matching and `TEXT` for exact, case-sensitive matching.

The `LOWER` attribute is case-insensitive, but the value you provide (`"Amazon"`) is case-sensitive because it's written with an uppercase "A". 

The correct pattern should have the value for `LOWER` written entirely in lowercase, like this:

```python
pattern1 = [{"LOWER": "amazon"}]
```

### Explanation:
- The `LOWER` key in the pattern expects the lowercase version of the word (`"amazon"`), regardless of how it appears in the text (e.g., `"Amazon"`, `"AMAZON"`, etc.).
- The mismatch happens because `"Amazon"` is not the lowercase equivalent; it should be `"amazon"`.

With the corrected pattern, the Matcher will successfully find matches for the token "Amazon" in the `doc`.


