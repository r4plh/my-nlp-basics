Here are some **challenging and logical questions** for spaCy's rule-based matching involving operators and advanced token attributes. These questions will test your understanding of pattern creation, combining conditions, and logical operators.

---

### **1. Match Numeric Ranges**
**Task:**
Write a pattern to match mentions of a price range, like `"from $20 to $50"` or `"between $10 and $1000"`. Ensure the pattern accounts for:
- Words like `"from"` or `"between"`.
- A dollar sign (`"$"`) followed by a number.
- Connecting words like `"to"` or `"and"`.
- Another dollar sign (`"$"`) followed by a number.

---

### **2. Match Conditional Statements**
**Task:**
Write a pattern to match conditional phrases, such as:
- `"If you update your app, you will see changes."`
- `"If you encounter any issues, contact support."`

The pattern should:
- Start with `"if"` (case insensitive).
- Include a clause containing a verb (e.g., `"update"`, `"encounter"`).
- Optionally end with another clause connected by a comma.

---

### **3. Match Repeated Words**
**Task:**
Write a pattern to match repeated words, such as `"very very good"` or `"no no no"`. The pattern should:
- Match any word that repeats at least twice.
- Use operators like `{"OP": "!"}` and `{"OP": "+"}` effectively.

---

### **4. Match Product Comparisons**
**Task:**
Write a pattern to match sentences comparing two products or services, such as:
- `"iPhone is better than Android."`
- `"This model is cheaper than the previous one."`

The pattern should:
- Match adjectives like `"better"`, `"cheaper"`, `"faster"`.
- Include connecting words like `"than"`.
- End with a proper noun (`PROPN`) or noun (`NOUN`).

---

### **5. Match Patterns with Negation**
**Task:**
Write a pattern to match negated phrases, such as:
- `"do not update the app"`
- `"never use this feature"`

The pattern should:
- Match negation tokens like `"not"` or `"never"`.
- Follow with a verb (`VERB`).

---

### **6. Match Multi-word Named Entities**
**Task:**
Write a pattern to match multi-word entities like:
- `"New York City"`
- `"San Francisco"`
- `"Los Angeles"`

The pattern should:
- Include proper nouns (`PROPN`).
- Match sequences of two or three consecutive proper nouns.

---

### **7. Match Dates in Different Formats**
**Task:**
Write a pattern to match dates in formats like:
- `"January 1, 2023"`
- `"01/01/2023"`
- `"2023-01-01"`

The pattern should:
- Use token attributes to account for numbers, punctuation, and proper nouns.

---

### **8. Match Email Addresses**
**Task:**
Write a pattern to match email addresses, such as:
- `"example@domain.com"`
- `"contact_us@company.co.uk"`

The pattern should:
- Use token attributes like `IS_ALPHA`, `IS_DIGIT`, and `TEXT`.
- Ensure the presence of an `"@"` symbol and a valid domain.

---

### **9. Match Adjective-Noun Phrases with Intensifiers**
**Task:**
Write a pattern to match phrases like:
- `"really good product"`
- `"extremely useful tool"`

The pattern should:
- Include intensifiers like `"really"`, `"extremely"`, `"very"`.
- Follow with an adjective (`ADJ`) and a noun (`NOUN`).

---

### **10. Match Verb-Noun Collocations**
**Task:**
Write a pattern to match common verb-noun pairs, such as:
- `"make a decision"`
- `"take a break"`
- `"have an impact"`

The pattern should:
- Include specific verbs like `"make"`, `"take"`, `"have"`.
- Match determiners (`DET`) and nouns (`NOUN`) that follow.

---

### **11. Match Sentences with Modal Verbs**
**Task:**
Write a pattern to match sentences containing modal verbs like:
- `"You should update the app."`
- `"We might see improvements."`

The pattern should:
- Match modal verbs (`MD` in POS tagging, e.g., `"should"`, `"might"`, `"can"`).
- Follow with a verb (`VERB`).

---

### **12. Match Keywords in Specific Contexts**
**Task:**
Write a pattern to match mentions of `"update"` only when preceded by `"system"`, `"software"`, or `"app"`. For example:
- Match: `"The app update was successful."`
- Don’t match: `"Please update the system."`

---

### **13. Match Interrogative Sentences**
**Task:**
Write a pattern to match questions, such as:
- `"What is your name?"`
- `"Where can I find the settings?"`

The pattern should:
- Start with question words (`"what"`, `"where"`, `"how"`, etc.).
- End with a question mark (`"?"`).

---

### **14. Match Sentences with Conjunctions**
**Task:**
Write a pattern to match sentences joined by conjunctions like `"and"`, `"but"`, or `"or"`. For example:
- `"I updated the app, but it didn’t work."`
- `"You can download the app or use the website."`

---

### **15. Match Phrases with Numerical Comparisons**
**Task:**
Write a pattern to match phrases with numerical comparisons, such as:
- `"The new version is 10% faster."`
- `"This device is $200 cheaper."`

The pattern should:
- Match numbers followed by comparative adjectives like `"faster"`, `"cheaper"`, `"better"`.  

--- 