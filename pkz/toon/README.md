# TOON Format Exploration

This experiment explores the [TOON format](https://github.com/toon-format/toon-python) and its application in LLM contexts to reduce token usage while maintaining readability and structure.

## What is TOON Format?

TOON (Tabular Object Notation) is a compact data serialization format designed for efficient representation of structured and tabular data. It achieves significant token savings compared to traditional formats like JSON while remaining human-readable.

### Example

```toon
[5]{id,name,age,city}:
  1,Alice,30,New York
  2,Bob,25,San Francisco
  3,Charlie,35,Los Angeles
  4,Diana,28,Chicago
  5,Eve,32,Boston
```

## Experiment Structure

### 1. Format Comparison (`01_toon_format.ipynb`)

Compares token usage across different data formats:
- JSON (pretty-printed and compact)
- XML
- YAML
- CSV
- TOON

Tests three different data structures:
- **Example 1**: Simple user data (5 records)
- **Example 2**: Financial statistics from Thai Stock Exchange (11 metrics × 4 time periods)
- **Example 3**: Complex nested objects (YouTube analytics report)

### 2. LLM Integration (`02_llm_with_toon.ipynb`)

Tests how LLMs handle TOON format input/output through systematic testing:
- Test 1: TOON input, no examples or templates
- Test 2: TOON input with format examples
- Test 3: TOON input with output templates
- Test 4: TOON input with both examples and templates
- Test 5: Traditional CSV → JSON approach (baseline)

## Key Findings

### Token Usage Efficiency

| Data Type | TOON vs JSON Compact | TOON vs JSON Pretty |
|-----------|---------------------|---------------------|
| Simple tabular (Example 1) | **-28.41%** | **-62.28%** |
| Financial data (Example 2) | **-90.23%** | **-90.64%** |
| Nested objects (Example 3) | **+3.21%** | **-33.90%** |

**Key Insights:**
- TOON excels with **tabular/structured data**, achieving 28-90% token reduction
- CSV is slightly more efficient for simple tables, but TOON provides better structure
- For deeply nested objects, JSON compact may be comparable or slightly better
- The savings are most dramatic with repetitive structured data (financial tables, analytics)

### LLM Compatibility

| Test Scenario | Input Tokens | Output Tokens | Valid TOON Output? |
|--------------|--------------|---------------|-------------------|
| No guidance | 603 | 750 | ✗ No |
| Example only | 642 | 562 | ✗ No |
| Template only | 666 | 657 | ✗ No |
| Both example + template | 705 | 502 | ✓ **Yes** |
| CSV → JSON (baseline) | 553 | 768 | N/A |

**Key Insights:**
- LLMs require **both format examples and output templates** to generate valid TOON
- When properly instructed, TOON reduces output tokens by **~35%** vs JSON
- Without proper guidance, LLMs default to JSON format
- Total token savings (input + output) can reach **~10%** even with added instruction overhead

### Practical Recommendations

**Use TOON format when:**
- Working with tabular data (financial reports, analytics, datasets)
- Data has uniform structure across multiple records
- Token efficiency is critical (API costs, context window limits)
- Both sender and receiver understand the format

**Stick with JSON when:**
- Data structures are deeply nested and irregular
- Interoperability with existing systems is required
- Team is unfamiliar with TOON format
- Token savings would be minimal (<10%)

**LLM Integration Best Practices:**
1. Always provide TOON format examples in the system prompt
2. Include explicit output templates showing the expected structure
3. Use tab delimiters for better token efficiency with Thai language data
4. Test with your specific LLM to verify format compliance

## Files Structure

```
pkz/toon/
├── README.md                    # This file
├── 01_toon_format.ipynb        # Format comparison experiments
├── 02_llm_with_toon.ipynb      # LLM integration tests
├── data/
│   ├── example1.csv            # Thai financial data
│   └── example2.json           # YouTube analytics data
└── module/
    ├── format_comparator.py    # Format conversion and comparison
    ├── token_counter.py        # Token counting utilities
    └── prompt.py               # LLM prompt templates
```

## Usage Examples

### Converting Data to TOON

```python
from toon_format import encode, decode

data = [
    {"id": 1, "name": "Alice", "age": 30},
    {"id": 2, "name": "Bob", "age": 25}
]

toon_text = encode(data)
print(toon_text)
# Output:
# [2]{id,name,age}:
#   1,Alice,30
#   2,Bob,25

# Convert back to Python objects
original_data = decode(toon_text)
```

### Comparing Token Usage

```python
from pkz.toon.module.format_comparator import FormatComparator

comparator = FormatComparator()
comparator.print_comparison(data, include_csv=True, include_xml=True)
```

### Using with LLMs

```python
from pkz.toon.module.prompt import prep_prompts
from toon_format import encode

# Convert data to TOON
data_toon = encode(data)

# Prepare prompts with examples and templates
prompts = prep_prompts(
    data_input=data_toon,
    data_format="TOON",
    toon_format_example="[2]{metric,value}:\n  ROA,2.5\n  ROE,9.2",
    toon_output_template="results[N]{field1,field2}:\n  ..."
)

# Send to LLM
response = llm.generate(
    system_prompt=prompts["system_prompt"],
    user_prompt=prompts["user_prompt"]
)
```

## Conclusion

TOON format is a powerful tool for reducing token usage in LLM applications, particularly when working with structured/tabular data. The format can achieve 30-90% token savings compared to JSON for appropriate use cases. However, successful LLM integration requires careful prompt engineering with both format examples and output templates.

For this specific experiment with Thai financial data, we observed:
- **~90% reduction** in input tokens vs JSON
- **~35% reduction** in output tokens when properly instructed
- **~10% overall savings** when accounting for instruction overhead

The trade-off between token efficiency and implementation complexity should be evaluated based on your specific use case, data characteristics, and LLM familiarity.

## References

- [TOON Format Official Repository](https://github.com/toon-format/toon-python)
- [Token usage tested with GPT-4o tokenizer](https://platform.openai.com/tokenizer)