### 1. **Create a Frequency Dictionary from List of Words**sa
   def word_frequency(words):
       freq_dict = {}
       for word in words:
           freq_dict[word] = freq_dict.get(word, 0) + 1
       return freq_dictsa

### 2. **Dictionary Filter by Value**
   def filter_by_value(d, threshold):
       return {k: v for k, v in d.items() if v > threshold}

### 3. **Key with Maximum Value**
   def max_key(d):
       return max(d, key=d.get) if d else None

### 4. **Convert Dictionary to List of Tuples**
   def dict_to_tuples(d):
       return list(d.items())

### 5. **Replace Dictionary Keys with Values from Another Dictionary**
   def replace_keys(d1, d2):
       return {k: d2.get(v, v) for k, v in d1.items()}

### 6. **Count Even and Odd Values in Dictionary**
   def even_odd_count(d):
       even_count = sum(1 for v in d.values() if v % 2 == 0)
       odd_count = len(d) - even_count
    return {'even': even_count, 'odd': odd_count}

### 7. **Check if All Values are Unique**
   def unique_values(d):
       return len(d.values()) == len(set(d.values()))

### 8. **Flatten a Multi-Level Nested Dictionary**
   def flatten(d, parent_key='', sep='.'):
       items = []
       for k, v in d.items():
           new_key = f"{parent_key}{sep}{k}" if parent_key else k
           if isinstance(v, dict):
               items.extend(flatten(v, new_key, sep=sep).items())
           else:
               items.append((new_key, v))
       return dict(items)

### 9. **Remove Key-Value Pairs with None Values**
   def remove_none(d):
       return {k: v for k, v in d.items() if v is not None}

### 10. **Sort Dictionary by Values**
   def sort_by_value(d):
       return dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
