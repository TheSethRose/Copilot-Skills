# Claude - Prompt Engineering

**Pages**: 13

---

## Automatically generate first draft prompt templates

**URL**: https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/prompt-generator

**Contents**:
- ​Next steps
- Start prompt engineering
- Prompt library
- GitHub prompting tutorial
- Google Sheets prompting tutorial

---

## Be clear, direct, and detailed

**URL**: https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/be-clear-and-direct

**Contents**:
- ​How to be clear, contextual, and specific
  - ​Examples
- Prompt library
- GitHub prompting tutorial
- Google Sheets prompting tutorial

Example: Anonymizing customer feedback

Example: Crafting a marketing email campaign

Example: Incident response

---

## Chain complex prompts for stronger performance

**URL**: https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/chain-prompts

**Contents**:
- ​Why chain prompts?
- ​When to chain prompts
- ​How to chain prompts
  - ​Example chained workflows:
  - ​Advanced: Self-correction chains
    - ​Prompt 1
    - ​Prompt 2
    - ​Prompt 3

Example: Self-correcting research summary

Example: Analyzing a legal contract (without chaining)

Example: Analyzing a legal contract (with chaining)

Example: Multitenancy strategy review

---

## Giving Claude a role with a system prompt

**URL**: https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/system-prompts

**Contents**:
- ​Why use role prompting?
- ​How to give Claude a role
- ​Examples
  - ​Example 1: Legal contract analysis
  - ​Example 2: Financial analysis
- Prompt library
- GitHub prompting tutorial
- Google Sheets prompting tutorial

Legal contract analysis without role prompting

Legal contract analysis with role prompting

Financial analysis without role prompting

Financial analysis with role prompting

**Examples**:

```text
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-3-7-sonnet-20250219",
    max_tokens=2048,
    system="You are a seasoned data scientist at a Fortune 500 company.", # <-- role prompt
    messages=[
        {"role": "user", "content": "Analyze this dataset for anomalies: <dataset>{{DATASET}}</dataset>"}
    ]
)

print(response.content)
```

---

## Keep Claude in character with role prompting and prefilling

**URL**: https://docs.claude.com/en/docs/test-and-evaluate/strengthen-guardrails/keep-claude-in-character

Example: Enterprise chatbot for role prompting

---

## Let Claude think (chain of thought prompting) to increase performance

**URL**: https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/chain-of-thought

**Contents**:
- ​Before implementing CoT
  - ​Why let Claude think?
  - ​Why not let Claude think?
- ​How to prompt for thinking
  - ​Examples
- Prompt library
- GitHub prompting tutorial
- Google Sheets prompting tutorial

Example: Writing donor emails (basic CoT)

Example: Writing donor emails (guided CoT)

Example: Writing donor emails (structured guided CoT)

Example: Financial analysis without thinking

Example: Financial analysis with thinking

---

## Long context prompting tips

**URL**: https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/long-context-tips

**Contents**:
- ​Essential tips for long context prompts
- Prompt library
- GitHub prompting tutorial
- Google Sheets prompting tutorial

Example multi-document structure

Example quote extraction

**Examples**:

```text
<documents>
  <document index="1">
    <source>annual_report_2023.pdf</source>
    <document_content>
      {{ANNUAL_REPORT}}
    </document_content>
  </document>
  <document index="2">
    <source>competitor_analysis_q2.xlsx</source>
    <document_content>
      {{COMPETITOR_ANALYSIS}}
    </document_content>
  </document>
</documents>

Analyze the annual report and competitor analysis. Identify strategic advantages and recommend Q3 focus areas.
```

```text
You are an AI physician's assistant. Your task is to help doctors diagnose possible patient illnesses.

<documents>
  <document index="1">
    <source>patient_symptoms.txt</source>
    <document_content>
      {{PATIENT_SYMPTOMS}}
    </document_content>
  </document>
  <document index="2">
    <source>patient_records.txt</source>
    <document_content>
      {{PATIENT_RECORDS}}
    </document_content>
  </document>
  <document index="3">
    <source>patient01_appt_history.txt</source>
    <docu
...
```

---

## Long context prompting tips - Claude Docs

**URL**: https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/long-context-tips

---

## Prefill Claude's response for greater output control

**URL**: https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/prefill-claudes-response

**Contents**:
- ​How to prefill Claude’s response
  - ​Examples
    - ​Example 1: Controlling output formatting and skipping the preamble
    - ​Example 2: Maintaining character in roleplay scenarios
- Prompt library
- GitHub prompting tutorial
- Google Sheets prompting tutorial

Example: Structured data extraction without prefilling

Example: Structured data extraction with prefilling

Example: Maintaining character without role prompting

Example: Maintaining character with role prompting

**Examples**:

```text
import anthropic

client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "What is your favorite color?"},
        {"role": "assistant", "content": "As an AI assistant, I don't have a favorite color, But if I had to pick, it would be green because"}  # Prefill here
    ]
)
```

---

## Use XML tags to structure your prompts

**URL**: https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/use-xml-tags

**Contents**:
- ​Why use XML tags?
- ​Tagging best practices
  - ​Examples
- Prompt library
- GitHub prompting tutorial
- Google Sheets prompting tutorial

Example: Generating financial reports

Example: Legal contract analysis

---

## Use examples (multishot prompting) to guide Claude's behavior

**URL**: https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/multishot-prompting

**Contents**:
- ​Why use examples?
- ​Crafting effective examples
- Prompt library
- GitHub prompting tutorial
- Google Sheets prompting tutorial

Example: Analyzing customer feedback

---

## Use our prompt improver to optimize your prompts

**URL**: https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/prompt-improver

**Contents**:
- ​Before you begin
- ​How the prompt improver works
- ​What you get
- ​How to use the prompt improver
- ​Generate test examples
- ​When to use the prompt improver
- ​Example improvement
- ​Troubleshooting

**Examples**:

```text
From the following list of Wikipedia article titles, identify which article this sentence came from.
Respond with just the article title and nothing else.

Article titles:
{{titles}}

Sentence to classify:
{{sentence}}
```

```text
You are an intelligent text classification system specialized in matching sentences to Wikipedia article titles. Your task is to identify which Wikipedia article a given sentence most likely belongs to, based on a provided list of article titles.

First, review the following list of Wikipedia article titles:
<article_titles>
{{titles}}
</article_titles>

Now, consider this sentence that needs to be classified:
<sentence_to_classify>
{{sentence}}
</sentence_to_classify>

Your goal is to determine
...
```

---

## Use prompt templates and variables

**URL**: https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/prompt-templates-and-variables

**Contents**:
- ​When to use prompt templates and variables
- ​Example prompt template
- ​Next steps
- Generate a prompt
- Apply XML tags
- Claude Console

**Examples**:

```text
Translate this text from English to Spanish: {{text}}
```

---
