# Claude - Evaluation

**Pages**: 9

---

## Create strong empirical evaluations

**URL**: https://docs.claude.com/en/docs/test-and-evaluate/develop-tests

**Contents**:
- ​Building evals and test cases
  - ​Eval design principles
  - ​Example evals
- ​Grading evals
  - ​Tips for LLM-based grading
- ​Next steps
- Brainstorm evaluations
- Evals cookbook

Task fidelity (sentiment analysis) - exact match evaluation

Consistency (FAQ bot) - cosine similarity evaluation

Relevance and coherence (summarization) - ROUGE-L evaluation

Tone and style (customer service) - LLM-based Likert scale

Privacy preservation (medical chatbot) - LLM-based binary classification

Context utilization (conversation assistant) - LLM-based ordinal scale

Example: LLM-based grading

**Examples**:

```python
import anthropic

tweets = [
    {"text": "This movie was a total waste of time. 👎", "sentiment": "negative"},
    {"text": "The new album is 🔥! Been on repeat all day.", "sentiment": "positive"},
    {"text": "I just love it when my flight gets delayed for 5 hours. #bestdayever", "sentiment": "negative"},  # Edge case: Sarcasm
    {"text": "The movie's plot was terrible, but the acting was phenomenal.", "sentiment": "mixed"},  # Edge case: Mixed sentiment
    # ... 996 more tweets
]

client = a
...
```

```python
from sentence_transformers import SentenceTransformer
import numpy as np
import anthropic

faq_variations = [
    {"questions": ["What's your return policy?", "How can I return an item?", "Wut's yur retrn polcy?"], "answer": "Our return policy allows..."},  # Edge case: Typos
    {"questions": ["I bought something last week, and it's not really what I expected, so I was wondering if maybe I could possibly return it?", "I read online that your policy is 30 days but that seems like it might be out
...
```

```python
from rouge import Rouge
import anthropic

articles = [
    {"text": "In a groundbreaking study, researchers at MIT...", "summary": "MIT scientists discover a new antibiotic..."},
    {"text": "Jane Doe, a local hero, made headlines last week for saving... In city hall news, the budget... Meteorologists predict...", "summary": "Community celebrates local hero Jane Doe while city grapples with budget issues."},  # Edge case: Multi-topic
    {"text": "You won't believe what this celebrity did! ... 
...
```

---

## Define your success criteria

**URL**: https://docs.claude.com/en/docs/test-and-evaluate/define-success

**Contents**:
- ​Building strong criteria
- ​Common success criteria to consider
- ​Next steps
- Brainstorm criteria
- Design evaluations

Example metrics and measurement methods

Example task fidelity criteria for sentiment analysis

Relevance and coherence

Example multidimensional criteria for sentiment analysis

---

## Define your success criteria - Claude Docs

**URL**: https://docs.claude.com/en/docs/test-and-evaluate/define-success

---

## Increase output consistency (JSON mode)

**URL**: https://docs.claude.com/en/docs/test-and-evaluate/strengthen-guardrails/increase-consistency

**Contents**:
- ​Specify the desired output format
- ​Prefill Claude’s response
- ​Constrain with examples
- ​Use retrieval for contextual consistency
- ​Chain prompts for complex tasks

Example: Standardizing customer feedback

Example: Daily sales report

Example: Generating consistent market intelligence

Example: Enhancing IT support consistency

---

## Mitigate jailbreaks and prompt injections

**URL**: https://docs.claude.com/en/docs/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks

**Contents**:
- ​Advanced: Chain safeguards
  - ​Bot system prompt
  - ​Prompt within harmlessness_screen tool

Example: Harmlessness screen for content moderation

Example: Ethical system prompt for an enterprise chatbot

Example: Multi-layered protection for a financial advisor chatbot

---

## Reduce hallucinations

**URL**: https://docs.claude.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-hallucinations

**Contents**:
- ​Basic hallucination minimization strategies
- ​Advanced techniques

Example: Analyzing a merger & acquisition report

Example: Auditing a data privacy policy

Example: Drafting a press release on a product launch

---

## Reduce prompt leak

**URL**: https://docs.claude.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-prompt-leak

**Contents**:
- ​Before you try to reduce prompt leak
- ​Strategies to reduce prompt leak

Example: Safeguarding proprietary analytics

---

## Reducing latency

**URL**: https://docs.claude.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-latency

**Contents**:
- ​How to measure latency
- ​How to reduce latency
  - ​1. Choose the right model
  - ​2. Optimize prompt and output length
  - ​3. Leverage streaming

**Examples**:

```text
import anthropic

client = anthropic.Anthropic()

# For time-sensitive applications, use Claude Haiku 4.5
message = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=100,
    messages=[{
        "role": "user",
        "content": "Summarize this customer feedback in 2 sentences: [feedback text]"
    }]
)
```

---

## Using the Evaluation Tool

**URL**: https://docs.claude.com/en/docs/test-and-evaluate/eval-tool

**Contents**:
- ​Accessing the Evaluate Feature
- ​Generating Prompts
- ​Creating Test Cases
- ​Tips for Effective Evaluation
- ​Understanding and comparing results

Click 'Generate Prompt'

Click on 'Generate Test Case'

Edit generation logic (optional)

Prompt Structure for Evaluation

**Examples**:

```text
In this task, you will generate a cute one sentence story that incorporates two elements: a color and a sound.
The color to include in the story is:
<color>
{{COLOR}}
</color>
The sound to include in the story is:
<sound>
{{SOUND}}
</sound>
Here are the steps to generate the story:
1. Think of an object, animal, or scene that is commonly associated with the color provided. For example, if the color is "blue", you might think of the sky, the ocean, or a bluebird.
2. Imagine a simple action, event
...
```

---
