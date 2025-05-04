# 🔍 Natural Language Processing (NLP)

### 📌 What is NLP?

Natural Language Processing is a subfield of **Artificial Intelligence (AI)** and **Linguistics** focused on enabling machines to understand, interpret, generate, and interact with human language.

---

## 🧰 NLP Tools & Libraries

### ✅ NLTK (Natural Language Toolkit)

A powerful Python library for NLP tasks like:

* Tokenization (word/sentence)
* POS tagging
* Stemming & Lemmatization
* Stopword removal
* N-grams
* Chunking

---

## ✂️ Tokenization

### 🔹 1. Word Tokenization

Splits text into words and punctuation.

```python
from nltk.tokenize import word_tokenize
ai_tokens = word_tokenize(AI)
```

### 🔹 2. Sentence Tokenization

Breaks text into sentences.

```python
from nltk.tokenize import sent_tokenize
AI_sent = sent_tokenize(AI)
```

### 🔹 3. Blankline Tokenization

Splits text on blank lines.

```python
from nltk.tokenize import blankline_tokenize
AI_blank = blankline_tokenize(AI)
```

### 🔹 4. Whitespace Tokenization

Splits only by spaces (does **not** separate punctuation).

```python
from nltk.tokenize import WhitespaceTokenizer
wt = WhitespaceTokenizer().tokenize(AI)
```

### 🔹 5. WordPunct Tokenization

Splits words and punctuation **separately**.

```python
from nltk.tokenize import wordpunct_tokenize
wordpunct_tokenize("AI-powered systems.")  # ['AI', '-', 'powered', 'systems', '.']
```

---

## 🔢 N-Grams

### 🔹 Definitions

* **Bigrams**: 2-word sequences
* **Trigrams**: 3-word sequences
* **N-grams**: n-word sequences

### 🔹 Code Example

```python
from nltk.util import bigrams, trigrams, ngrams
tokens = word_tokenize("hello the best and most beautiful things cannot be seen")

list(bigrams(tokens))
list(trigrams(tokens))
list(ngrams(tokens, 4))
```

---

## 🌱 Stemming

### 🔹 Goal

Reduce words to their **base/root** form. The stemmed word might not be a real word.

### 🔹 Types of Stemmer

#### 1. **Porter Stemmer**

```python
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
stemmer.stem("running")  # "run"
```

#### 2. **Lancaster Stemmer** (More aggressive)

```python
from nltk.stem import LancasterStemmer
LancasterStemmer().stem("studies")  # "study"
```

#### 3. **Snowball Stemmer**

```python
from nltk.stem import SnowballStemmer
SnowballStemmer("english").stem("fishing")  # "fish"
```

#### 4. **Regex Stemmer**

```python
from nltk.stem import RegexpStemmer
RegexpStemmer('ing$|ed$|s$', min=4).stem("running")
```

---

## 📘 Lemmatization

Returns **valid words** using grammar and dictionary rules.

```python
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
lemmatizer.lemmatize("better", pos='a')  # "good"
```

---

## 🛑 Stopwords

Words like “is”, “the”, “and” that don’t add much meaning.

```python
from nltk.corpus import stopwords
stopwords.words('english')  # Also: 'german', 'french', 'marathi' etc.
```

---

## 🔍 Regex in NLP

Used for cleaning text: removing punctuation, digits, special characters.

```python
import re
punctuation = re.compile(r'[-.?!,:;()|0-9]')
cleaned = [punctuation.sub('', word) for word in ai_tokens if punctuation.sub('', word)]
```

---

## 🔤 POS Tagging (Part of Speech)

Labels each word with its grammatical role (noun, verb, adjective, etc.)

```python
from nltk import pos_tag
pos_tag(word_tokenize("AI is transforming the world."))
```

| Tag | Meaning     | Example    |
| --- | ----------- | ---------- |
| NN  | Noun        | dog, apple |
| VB  | Verb (base) | run, eat   |
| JJ  | Adjective   | big, smart |
| RB  | Adverb      | quickly    |
| IN  | Preposition | in, on     |

---

## 🧱 Chunking (Shallow Parsing)

Groups words into phrases based on patterns.

```python
import nltk
sentence = [("the", "DT"), ("dog", "NN"), ("barked", "VBD")]
chunk_grammar = "NP: {<DT>?<JJ>*<NN>}"
chunk_parser = nltk.RegexpParser(chunk_grammar)
tree = chunk_parser.parse(sentence)
tree.draw()
```

---
