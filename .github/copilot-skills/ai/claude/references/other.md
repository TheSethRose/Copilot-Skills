# Claude - Other

**Pages**: 101

---

## Adaptive editor

**URL**: https://docs.claude.com/en/resources/prompt-library/adaptive-editor

**Contents**:
  - ​Example output
  - ​API request

**Examples**:

```text
import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=2000,
    temperature=1,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Rewrite the following paragraph using the following instructions: in the style of a pirate.  \n  \nParag
...
```

---

## Airport code analyst

**URL**: https://docs.claude.com/en/resources/prompt-library/airport-code-analyst

**Contents**:
  - ​Example Output
  - ​API request

**Examples**:

```python
import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1000,
    temperature=0,
    system="Your task is to analyze the provided text and identify any airport codes mentioned within it. Present these airport codes as a list in the order they appear in the text. If no airport codes are found, return an empty list.",
    messages=[
        {
   
...
```

---

## Alien anthropologist - Claude Docs

**URL**: https://docs.claude.com/en/resources/prompt-library/alien-anthropologist

---

## Alien anthropologist

**URL**: https://docs.claude.com/en/resources/prompt-library/alien-anthropologist

**Contents**:
  - ​Example output
  - ​API Request

**Examples**:

```python
import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=2000,
    temperature=1,
    system="Imagine you are an alien anthropologist studying human culture and customs. Analyze the following aspects of human society from an objective, outsider's perspective. Provide detailed observations, insights, and hypotheses based on the available informat
...
```

---

## Alliteration alchemist - Claude Docs

**URL**: https://docs.claude.com/en/resources/prompt-library/alliteration-alchemist

---

## Alliteration alchemist

**URL**: https://docs.claude.com/en/resources/prompt-library/alliteration-alchemist

**Contents**:
  - ​Example output
  - ​API request

**Examples**:

```text
import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1000,
    temperature=1,
    system="Your task is to create alliterative phrases and sentences for the given subject. Ensure that the alliterations not only sound pleasing but also convey relevant information or evoke appropriate emotions related to the subject.",
    messages=[
        {

...
```

---

## Babel's broadcasts

**URL**: https://docs.claude.com/en/resources/prompt-library/babels-broadcasts

**Contents**:
  - ​Example output
  - ​API request

**Examples**:

```text
import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=2000,
    temperature=0,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Write me a series of product announcement tweets in the 10 most commonly spoken languages. The product i
...
```

---

## Brand builder

**URL**: https://docs.claude.com/en/resources/prompt-library/brand-builder

**Contents**:
  - ​Example output
  - ​API request

**Examples**:

```python
import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=2000,
    temperature=1,
    system="Your task is to create a comprehensive design brief for a holistic brand identity based on the given specifications. The brand identity should encompass various elements such as suggestions for the brand name, logo, color palette, typography, visual sty
...
```

---

## CSV converter

**URL**: https://docs.claude.com/en/resources/prompt-library/csv-converter

**Contents**:
- ​Example Output
- ​API Request

**Examples**:

```text
"name";"age";"city";"email"
"John Doe";"30";"New York";"[email protected]"
"Jane Smith";"25";"London";"[email protected]"
"Bob Johnson";"35";"Paris";"[email protected]"
```

```python
import anthropic

client = anthropic.Anthropic(  # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1000,
    temperature=0,
    system="As a data conversion expert, your task is to convert data from different formats (JSON, XML, etc.) into properly formatted CSV files. The user will provide the input data in the original format, along with any specific requirements or preferences for the C
...
```

---

## Career coach

**URL**: https://docs.claude.com/en/resources/prompt-library/career-coach

**Contents**:
- ​Example Output
- ​API Request

**Examples**:

```python
import anthropic

client = anthropic.Anthropic(  # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=2000,
    temperature=1,
    system="You will be acting as an AI career coach named Joe created by the company AI Career Coach Co. Your goal is to give career advice to users. You will be replying to users who are on the AI Career Coach Co. site and who will be confused if you don't respond i
...
```

---

## Citations

**URL**: https://docs.claude.com/en/docs/build-with-claude/citations

**Contents**:
- ​How citations work
  - ​Citable vs non-citable content
  - ​Citation indices
  - ​Token costs
  - ​Feature compatibility
    - ​Using Prompt Caching with Citations
- ​Document Types
  - ​Choosing a document type

Provide document(s) and enable citations

Documents get processed

Claude provides cited response

Example plain text citation

Example streaming events

**Examples**:

```text
curl https://api.anthropic.com/v1/messages \
  -H "content-type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "claude-sonnet-4-5",
    "max_tokens": 1024,
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "document",
            "source": {
              "type": "text",
              "media_type": "text/plain",
              "data": "The grass is green. The sky is blue."
...
```

```text
import anthropic

client = anthropic.Anthropic()

# Long document content (e.g., technical documentation)
long_document = "This is a very long document with thousands of words..." + " ... " * 1000  # Minimum cacheable length

response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "document",
                    "source": {
                   
...
```

```text
{
    "type": "document",
    "source": {
        "type": "text",
        "media_type": "text/plain",
        "data": "Plain text content..."
    },
    "title": "Document Title", # optional
    "context": "Context about the document that will not be cited from", # optional
    "citations": {"enabled": True}
}
```

---

## Cite your sources

**URL**: https://docs.claude.com/en/resources/prompt-library/cite-your-sources

**Contents**:
- ​Example output
- ​API Request

**Examples**:

```python
import anthropic

client = anthropic.Anthropic(  # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=2000,
    temperature=0,
    system='You are an expert research assistant. Here is a document you will answer questions about: \n<doc> \n[Full text of [Matterport SEC filing 10-K 2023](https://investors.matterport.com/node/9501/html), not pasted here for brevity] \n</doc> \n \nFirst, find the
...
```

---

## Claude Apps

**URL**: https://docs.claude.com/en/release-notes/claude-apps

**Contents**:
    - ​October 16, 2025
    - ​October 15, 2025
    - ​September 29, 2025
    - ​August 28, 2025
    - ​August 5, 2025
    - ​May 22, 2025
    - ​February 24th, 2025
    - ​December 20th, 2024

---

## Code clarifier - Claude Docs

**URL**: https://docs.claude.com/en/resources/prompt-library/code-clarifier

---

## Code clarifier

**URL**: https://docs.claude.com/en/resources/prompt-library/code-clarifier

**Contents**:
  - ​Example Output
  - ​API request

**Examples**:

```javascript
import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1000,
    temperature=0,
    system="Your task is to take the code snippet provided and explain it in simple, easy-to-understand language. Break down the code's functionality, purpose, and key components. Use analogies, examples, and plain terms to make the explanation accessible to someon
...
```

---

## Code consultant

**URL**: https://docs.claude.com/en/resources/prompt-library/code-consultant

**Contents**:
- ​Example Output
- ​API Request

**Examples**:

```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
```

```javascript
import anthropic

client = anthropic.Anthropic(  # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1000,
    temperature=0,
    system="Your task is to analyze the provided Python code snippet and suggest improvements to optimize its performance. Identify areas where the code can be made more efficient, faster, or less resource-intensive. Provide specific suggestions for optimization, alon
...
```

---

## Context editing

**URL**: https://docs.claude.com/en/docs/build-with-claude/context-editing

**Contents**:
- ​How it works
- ​Supported models
- ​Basic usage
- ​Advanced configuration
- ​Configuration options
- ​Response format
- ​Token counting
- ​Using with the Memory Tool

**Examples**:

```text
curl https://api.anthropic.com/v1/messages \
    --header "x-api-key: $ANTHROPIC_API_KEY" \
    --header "anthropic-version: 2023-06-01" \
    --header "content-type: application/json" \
    --header "anthropic-beta: context-management-2025-06-27" \
    --data '{
        "model": "claude-sonnet-4-5",
        "max_tokens": 4096,
        "messages": [
            {
                "role": "user",
                "content": "Search for recent developments in AI"
            }
        ],
        "to
...
```

```text
curl https://api.anthropic.com/v1/messages \
    --header "x-api-key: $ANTHROPIC_API_KEY" \
    --header "anthropic-version: 2023-06-01" \
    --header "content-type: application/json" \
    --header "anthropic-beta: context-management-2025-06-27" \
    --data '{
        "model": "claude-sonnet-4-5",
        "max_tokens": 4096,
        "messages": [
            {
                "role": "user",
                "content": "Create a simple command line calculator app using Python"
            }
  
...
```

```text
{
    "id": "msg_013Zva2CMHLNnXjNJJKqJ2EF",
    "type": "message",
    "role": "assistant",
    "content": [...],
    "usage": {...},
    "context_management": {
        "applied_edits": [
            {
                "type": "clear_tool_uses_20250919",
                "cleared_tool_uses": 8,
                "cleared_input_tokens": 50000
            }
        ]
    }
}
```

---

## Context windows

**URL**: https://docs.claude.com/en/docs/build-with-claude/context-windows

**Contents**:
- ​Understanding the context window
- ​The context window with extended thinking
- ​The context window with extended thinking and tool use
- ​1M token context window
- ​Context awareness in Claude Sonnet 4.5 and Haiku 4.5
- ​Context window management with newer Claude models
- ​Next steps
- Model comparison table

First turn architecture

Tool result handling (turn 2)

**Examples**:

```python
from anthropic import Anthropic

client = Anthropic()

response = client.beta.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Process this large document..."}
    ],
    betas=["context-1m-2025-08-07"]
)
```

```text
<budget:token_budget>200000</budget:token_budget>
```

```text
<system_warning>Token usage: 35000/200000; 165000 remaining</system_warning>
```

---

## Corporate clairvoyant

**URL**: https://docs.claude.com/en/resources/prompt-library/corporate-clairvoyant

**Contents**:
- ​Example Output
- ​API Request

**Examples**:

```text
import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=2000,
    temperature=0,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Your task is to analyze the following report:  \n<report>  \n[Full text of [Matterport SEC filing 10-K 2
...
```

---

## Cosmic Keystrokes

**URL**: https://docs.claude.com/en/resources/prompt-library/cosmic-keystrokes

**Contents**:
- ​Example Output
- ​API Request

**Examples**:

```javascript
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <script src="https://cdn.tailwindcss.com"></script>
    <title>Side-Scrolling Typing Game</title>
  </head>
  <body class="bg-gray-900 text-white">
    <div class="fixed top-4 right-4 text-2xl">
      Score: <span id="score">0</span>
    </div>
    <div id="game" class="h-screen w-screen overflow-hidden relative">
      <div
        id="player"
        cla
...
```

```text
import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=2000,
    temperature=0,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Write me a fully complete web app as a single HTML file. The app should contain a simple side-scrolling 
...
```

---

## Cosmic Keystrokes - Claude Docs

**URL**: https://docs.claude.com/en/resources/prompt-library/cosmic-keystrokes

---

## Culinary creator

**URL**: https://docs.claude.com/en/resources/prompt-library/culinary-creator

**Contents**:
- ​Example Output
- ​API request

**Examples**:

```text
import anthropic

client = anthropic.Anthropic(
  # defaults to os.environ.get("ANTHROPIC_API_KEY")
  api_key="my_api_key",
)
message = client.messages.create(
  model="claude-sonnet-4-5",
  max_tokens=2000,
  temperature=0.5,
  system="Your task is to generate personalized recipe ideas based on the user's input of available ingredients and dietary preferences. Use this information to suggest a variety of creative and delicious recipes that can be made using the given ingredients while accommoda
...
```

---

## Customer support agent

**URL**: https://docs.claude.com/en/docs/about-claude/use-case-guides/customer-support-chat

**Contents**:
- ​Before building with Claude
  - ​Decide whether to use Claude for support chat
  - ​Define your ideal chat interaction
  - ​Break the interaction into unique tasks
  - ​Establish success criteria
- ​How to implement Claude as a customer service agent
  - ​Choose the right Claude model
  - ​Build a strong prompt

High volume of repetitive queries

Need for quick information synthesis

24/7 availability requirement

Rapid scaling during peak periods

Consistent brand voice

Query comprehension accuracy

Citation provision relevance

Content generation effectiveness

Escalation efficiency

Sentiment maintenance

Customer satisfaction score

**Examples**:

```text
IDENTITY = """You are Eva, a friendly and knowledgeable AI assistant for Acme Insurance 
Company. Your role is to warmly welcome customers and provide information on 
Acme's insurance offerings, which include car insurance and electric car 
insurance. You can also help customers get quotes for their insurance needs."""
```

```text
STATIC_GREETINGS_AND_GENERAL = """
<static_context>
Acme Auto Insurance: Your Trusted Companion on the Road

About:
At Acme Insurance, we understand that your vehicle is more than just a mode of transportation—it's your ticket to life's adventures. 
Since 1985, we've been crafting auto insurance policies that give drivers the confidence to explore, commute, and travel with peace of mind.
Whether you're navigating city streets or embarking on cross-country road trips, Acme is there to protect you
...
```

```javascript
STATIC_CAR_INSURANCE="""
<static_context>
Car Insurance Coverage:
Acme's car insurance policies typically cover:
1. Liability coverage: Pays for bodily injury and property damage you cause to others.
2. Collision coverage: Pays for damage to your car in an accident.
3. Comprehensive coverage: Pays for damage to your car from non-collision incidents.
4. Medical payments coverage: Pays for medical expenses after an accident.
5. Uninsured/underinsured motorist coverage: Protects you if you're hit b
...
```

---

## Data organizer

**URL**: https://docs.claude.com/en/resources/prompt-library/data-organizer

**Contents**:
  - ​Example output

**Examples**:

```text
[
  {
    "name": "Dr. Liam Patel",
    "age": 45,
    "profession": "Neurosurgeon",
    "education": "Yale",
    "accomplishments": "Revolutionized surgical techniques at the regional medical center"
  },
  {
    "name": "Olivia Chen",
    "age": 28,
    "profession": "Architect",
    "education": "UC Berkeley",
    "accomplishments": "Transformed the village's landscape with sustainable and breathtaking designs"
  },
  {
    "name": "Ethan Kovacs",
    "age": 72,
    "profession": "Musician an
...
```

```python
import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1000,
    temperature=0,
    system="Your task is to take the unstructured text provided and convert it into a well-organized table format using JSON. Identify the main entities, attributes, or categories mentioned in the text and use them as keys in the JSON object. Then, extract the rele
...
```

---

## Direction decoder

**URL**: https://docs.claude.com/en/resources/prompt-library/direction-decoder

**Contents**:
  - ​Example output
- ​API Request

**Examples**:

```text
import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1000,
    temperature=0,
    system="Your task is to take the provided natural language description of a process or task and transform it into clear, concise step-by-step directions that are logical, sequential, and easy to follow. Use imperative language and begin each step with an action
...
```

---

## Dream interpreter

**URL**: https://docs.claude.com/en/resources/prompt-library/dream-interpreter

**Contents**:
- ​Example output
- ​API Request

**Examples**:

```python
import anthropic

client = anthropic.Anthropic(  # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=2000,
    temperature=1,
    system="You are an AI assistant with a deep understanding of dream interpretation and symbolism. Your task is to provide users with insightful and meaningful analyses of the symbols, emotions, and narratives present in their dreams. Offer potential interpretations
...
```

---

## Dream interpreter - Claude Docs

**URL**: https://docs.claude.com/en/resources/prompt-library/dream-interpreter

---

## Efficiency estimator

**URL**: https://docs.claude.com/en/resources/prompt-library/efficiency-estimator

**Contents**:
  - ​Example output
  - ​API request

**Examples**:

```text
for i in range(n):
   print(i)
```

```text
for j in range(n):
    for k in range(n):
        print(j, k)
```

```javascript
import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1000,
    temperature=0,
    system="Your task is to analyze the provided function or algorithm and calculate its time complexity using Big O notation. Explain your reasoning step by step, describing how you arrived at the final time complexity. Consider the worst-case scenario when determ
...
```

---

## Email extractor - Claude Docs

**URL**: https://docs.claude.com/en/resources/prompt-library/email-extractor

---

## Email extractor

**URL**: https://docs.claude.com/en/resources/prompt-library/email-extractor

**Contents**:
  - ​Example output
  - ​API request

**Examples**:

```python
import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1000,
    temperature=0,
    system="Precisely copy any email addresses from the following text and then write them, one per line. Only write an email address if it's precisely spelled out in the input text. If there are no email addresses in the text, write \"N/A\".  Do not say anything e
...
```

---

## Emoji encoder

**URL**: https://docs.claude.com/en/resources/prompt-library/emoji-encoder

**Contents**:
- ​Example output
- ​API Request

**Examples**:

```text
import anthropic

client = anthropic.Anthropic(  # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1000,
    temperature=0,
    system="Your task is to take the plain text message provided and convert it into an expressive, emoji-rich message that conveys the same meaning and intent. Replace key words and phrases with relevant emojis where appropriate to add visual interest and emotion. Us
...
```

---

## Ethical dilemma navigator

**URL**: https://docs.claude.com/en/resources/prompt-library/ethical-dilemma-navigator

**Contents**:
- ​Example Output
- ​API Request

**Examples**:

```text
import anthropic

client = anthropic.Anthropic(
  # defaults to os.environ.get("ANTHROPIC_API_KEY")
  api_key="my_api_key",
)
message = client.messages.create(
  model="claude-sonnet-4-5",
  max_tokens=2000,
  temperature=1,
  system="Help the user navigate a complex ethical dilemma by identifying core ethical principles, exploring different ethical frameworks, considering potential consequences, acknowledging complexity, encouraging personal reflection, and offering additional resources. Mainta
...
```

---

## Excel formula expert - Claude Docs

**URL**: https://docs.claude.com/en/resources/prompt-library/excel-formula-expert

---

## Excel formula expert

**URL**: https://docs.claude.com/en/resources/prompt-library/excel-formula-expert

**Contents**:
- ​Example Output
- ​API request

**Examples**:

```javascript
import anthropic

client = anthropic.Anthropic(  # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1000,
    temperature=0,
    system="As an Excel Formula Expert, your task is to provide advanced Excel formulas that perform the complex calculations or data manipulations described by the user. If the user does not provide this information, ask the user to describe the desired outcome or op
...
```

---

## Function fabricator

**URL**: https://docs.claude.com/en/resources/prompt-library/function-fabricator

**Contents**:
- ​Example Output
- ​API Request

**Examples**:

```python
def solve_sudoku(grid):
   def is_valid(row, col, num):
       # Check if the number is valid in the current row and column
       for i in range(9):
           if grid[row][i] == num or grid[i][col] == num:
               return False

       # Check if the number is valid in the current 3x3 subgrid
       start_row, start_col = (row // 3) * 3, (col // 3) * 3
       for i in range(3):
           for j in range(3):
               if grid[start_row + i][start_col + j] == num:
                   r
...
```

```javascript
import anthropic

client = anthropic.Anthropic(  # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1000,
    temperature=0,
    system="Your task is to create Python functions based on the provided natural language requests. The requests will describe the desired functionality of the function, including the input parameters and expected return value. Implement the functions according to th
...
```

---

## Futuristic fashion advisor

**URL**: https://docs.claude.com/en/resources/prompt-library/futuristic-fashion-advisor

**Contents**:
  - ​Example output
  - ​API Request

**Examples**:

```text
import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1000,
    temperature=1,
    system="Your task is to suggest avant-garde fashion trends and styles tailored to the user's preferences. If the user doesn't provide this information, ask the user about their personal style, favorite colors, preferred materials, body type, and any specific fa
...
```

---

## Git gud

**URL**: https://docs.claude.com/en/resources/prompt-library/git-gud

**Contents**:
- ​Example Output
- ​API Request

**Examples**:

```text
git add example.txt
git commit -m "Update example.txt with new content"
```

```text
import anthropic

client = anthropic.Anthropic(  # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1000,
    temperature=0,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "I have made some changes to my local files and I want to save them in my local Git repository. What Git com
...
```

---

## Glossary

**URL**: https://docs.claude.com/en/docs/about-claude/glossary

**Contents**:
- ​Context window
- ​Fine-tuning
- ​HHH
- ​Latency
- ​LLM
- ​MCP (Model Context Protocol)
- ​MCP connector
- ​Pretraining

---

## Google Sheets add-on - Claude Docs

**URL**: https://docs.claude.com/en/docs/agents-and-tools/claude-for-sheets

---

## Google apps scripter

**URL**: https://docs.claude.com/en/resources/prompt-library/google-apps-scripter

**Contents**:
- ​Example Output
- ​API Request

**Examples**:

```javascript
function translateSlidesToKorean() {
  var presentation = SlidesApp.getActivePresentation();
  var slides = presentation.getSlides();

  for (var i = 0; i < slides.length; i++) {
    var slide = slides[i];
    var pageElements = slide.getPageElements();

    for (var j = 0; j < pageElements.length; j++) {
      var pageElement = pageElements[j];

      if (pageElement.getPageElementType() === SlidesApp.PageElementType.SHAPE) {
        var shape = pageElement.asShape();
        if (shape.getText(
...
```

```text
import anthropic

client = anthropic.Anthropic(
  # defaults to os.environ.get("ANTHROPIC_API_KEY")
  api_key="my_api_key",
)
message = client.messages.create(
  model="claude-sonnet-4-5",
  max_tokens=2000,
  temperature=0,
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Write me a Google apps script that will translate all text in a Google Slides presentation to Korean."
        }
      ]
    }
  ]
)
print(message.content)
```

---

## Grading guru

**URL**: https://docs.claude.com/en/resources/prompt-library/grading-guru

**Contents**:
- ​Example Output
- ​API Request

**Examples**:

```text
import anthropic

client = anthropic.Anthropic(  # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=2000,
    temperature=0,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Evaluate the following two texts based on the given criteria: \n \nText 1: \nThe sun was setting behind the
...
```

---

## Grammar genie

**URL**: https://docs.claude.com/en/resources/prompt-library/grammar-genie

**Contents**:
- ​Example Output
- ​API Request

**Examples**:

```text
import anthropic

client = anthropic.Anthropic(  # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1000,
    temperature=0,
    system="Your task is to take the text provided and rewrite it into a clear, grammatically correct version while preserving the original meaning as closely as possible. Correct any spelling mistakes, punctuation errors, verb tense issues, word choice problems, and 
...
```

---

## Hal the humorous helper

**URL**: https://docs.claude.com/en/resources/prompt-library/hal-the-humorous-helper

**Contents**:
- ​Example Output
- ​API Request

**Examples**:

```text
import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=2000,
    temperature=1,
    system="You will play the role of Hal, a highly knowledgeable AI assistant with a humorous and often sarcastic personality. Engage in conversation with the user, providing informative and helpful responses while injecting wit, irony, and playful jabs. Your resp
...
```

---

## Home - Claude Docs

**URL**: https://docs.claude.com/en/home

---

## Idiom illuminator - Claude Docs

**URL**: https://docs.claude.com/en/resources/prompt-library/idiom-illuminator

---

## Idiom illuminator

**URL**: https://docs.claude.com/en/resources/prompt-library/idiom-illuminator

**Contents**:
- ​Example Output
- ​API Request

**Examples**:

```text
import anthropic

client = anthropic.Anthropic(  # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1000,
    temperature=1,
    system="Your task is to provide a clear explanation of the meaning and origin of an idioms and proverb that the user gives you. Offer a concise interpretation of its figurative meaning and how it is typically used in conversation or writing. Next, delve into the o
...
```

---

## Interview question crafter

**URL**: https://docs.claude.com/en/resources/prompt-library/interview-question-crafter

**Contents**:
- ​Example Output
- ​API Request

**Examples**:

```python
import anthropic

client = anthropic.Anthropic(
  # defaults to os.environ.get("ANTHROPIC_API_KEY")
  api_key="my_api_key",
)
message = client.messages.create(
  model="claude-sonnet-4-5",
  max_tokens=1000,
  temperature=0.5,
  system="Your task is to generate a series of thoughtful, open-ended questions for an interview based on the given context. The questions should be designed to elicit insightful and detailed responses from the interviewee, allowing them to showcase their knowledge, experi
...
```

---

## Interview question crafter - Claude Docs

**URL**: https://docs.claude.com/en/resources/prompt-library/interview-question-crafter

---

## LaTeX legend

**URL**: https://docs.claude.com/en/resources/prompt-library/latex-legend

**Contents**:
- ​Example Output
- ​API Request

**Examples**:

```text
\begin{table}[h]
\centering
\begin{tabular}{|c|c|c|}
\hline
Name & Age & City \\
\hline
John & 25 & New York \\
\hline
\end{tabular}
\caption{Sample Table}
\label{tab:sample}
\end{table}
```

```text
+------+-----+----------+
| Name | Age |   City   |
+------+-----+----------+
| John |  25 | New York |
+------+-----+----------+
```

```text
import anthropic

client = anthropic.Anthropic(  # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=2000,
    temperature=0,
    system="You are an AI assistant with expertise in LaTeX, a document preparation system widely used for academic and technical writing. Your task is to help users write LaTeX documents by providing the appropriate code for various elements such as mathematical equa
...
```

---

## LaTeX legend - Claude Docs

**URL**: https://docs.claude.com/en/resources/prompt-library/latex-legend

---

## Legal summarization

**URL**: https://docs.claude.com/en/docs/about-claude/use-case-guides/legal-summarization

**Contents**:
- ​Before building with Claude
  - ​Decide whether to use Claude for legal summarization
  - ​Determine the details you want the summarization to extract
  - ​Establish success criteria
- ​How to summarize legal documents using Claude
  - ​Select the right Claude model
  - ​Transform documents into a format that Claude can process
  - ​Build a strong prompt

You want to review a high volume of documents efficiently and affordably

You require automated extraction of key metadata

You want to generate clear, concise, and standardized summaries

You need precise citations for your summaries

You want to streamline and expedite your legal research process

Contextual embedding similarity

**Examples**:

```text
details_to_extract = [
    'Parties involved (sublessor, sublessee, and original lessor)',
    'Property details (address, description, and permitted use)', 
    'Term and rent (start date, end date, monthly rent, and security deposit)',
    'Responsibilities (utilities, maintenance, and repairs)',
    'Consent and notices (landlord\'s consent, and notice requirements)',
    'Special provisions (furniture, parking, and subletting restrictions)'
]
```

```python
from io import BytesIO
import re

import pypdf
import requests

def get_llm_text(pdf_file):
    reader = pypdf.PdfReader(pdf_file)
    text = "\n".join([page.extract_text() for page in reader.pages])

    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text) 

    # Remove page numbers
    text = re.sub(r'\n\s*\d+\s*\n', '\n', text) 

    return text


# Create the full URL from the GitHub repository
url = "https://raw.githubusercontent.com/anthropics/anthropic-cookbook/main/skills/summ
...
```

```javascript
import anthropic

# Initialize the Anthropic client
client = anthropic.Anthropic()

def summarize_document(text, details_to_extract, model="claude-sonnet-4-5", max_tokens=1000):

    # Format the details to extract to be placed within the prompt's context
    details_to_extract_str = '\n'.join(details_to_extract)
    
    # Prompt the model to summarize the sublease agreement
    prompt = f"""Summarize the following sublease agreement. Focus on these key aspects:

    {details_to_extract_str}

 
...
```

---

## Lesson planner

**URL**: https://docs.claude.com/en/resources/prompt-library/lesson-planner

**Contents**:
- ​Example output
  - ​API request

**Examples**:

```text
import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=4000,
    temperature=0.5,
    system="Your task is to create a comprehensive, engaging, and well-structured lesson plan on the given subject. The lesson plan should be designed for a 60-minute class session and should cater to a specific grade level or age group. Begin by stating the less
...
```

---

## Master moderator

**URL**: https://docs.claude.com/en/resources/prompt-library/master-moderator

**Contents**:
  - ​Example output
  - ​API request

**Examples**:

```python
import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=10,
    temperature=0,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "A human user is in dialogue with an AI. The human is asking the AI a series of questions or requesting a s
...
```

---

## Meeting scribe

**URL**: https://docs.claude.com/en/resources/prompt-library/meeting-scribe

**Contents**:
- ​Example Output
- ​API request

**Examples**:

```python
import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=4000,
    temperature=0.5,
    system="Your task is to review the provided meeting notes and create a concise summary that captures the essential information, focusing on key takeaways and action items assigned to specific individuals or departments during the meeting. Use clear and profes
...
```

---

## Memo maestro

**URL**: https://docs.claude.com/en/resources/prompt-library/memo-maestro

**Contents**:
- ​Example Output
- ​API Request

**Examples**:

```javascript
import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1000,
    temperature=1,
    system="Your task is to compose a comprehensive company memo based on the provided key points. The memo should be written in a professional tone, addressing all the relevant information in a clear and concise manner. Use appropriate formatting, such as headings
...
```

---

## Mindfulness mentor

**URL**: https://docs.claude.com/en/resources/prompt-library/mindfulness-mentor

**Contents**:
- ​Example output
- ​API request

**Examples**:

```text
import anthropic

client = anthropic.Anthropic( # defaults to os.environ.get("ANTHROPIC_API_KEY")
api_key="my_api_key",
)
message = client.messages.create(
  model="claude-sonnet-4-5",
  max_tokens=1000,
  temperature=1,
  system="You are an AI assistant with expertise in mindfulness and stress management. Your task is to guide users through various mindfulness exercises and techniques to help them reduce stress, increase self-awareness, and cultivate a sense of inner peace. Offer clear instruct
...
```

---

## Mindfulness mentor - Claude Docs

**URL**: https://docs.claude.com/en/resources/prompt-library/mindfulness-mentor

---

## Model deprecations

**URL**: https://docs.claude.com/en/docs/about-claude/model-deprecations

**Contents**:
- ​Overview
- ​Migrating to replacements
- ​Notifications
- ​Auditing model usage
- ​Best practices
- ​Model status
- ​Deprecation history
  - ​2025-08-13: Claude Sonnet 3.5 models

---

## Model deprecations - Claude Docs

**URL**: https://docs.claude.com/en/docs/about-claude/model-deprecations

---

## Mood colorizer

**URL**: https://docs.claude.com/en/resources/prompt-library/mood-colorizer

**Contents**:
- ​Example Output
- ​API Request

**Examples**:

```text
import anthropic

client = anthropic.Anthropic(
  # defaults to os.environ.get("ANTHROPIC_API_KEY")
  api_key="my_api_key",
)
message = client.messages.create(
  model="claude-sonnet-4-5",
  max_tokens=500,
  temperature=0.5,
  system="Your task is to take the provided text description of a mood or emotion and generate a HEX color code that visually represents that mood. Use color psychology principles and common associations to determine the most appropriate color for the given mood. If the tex
...
```

---

## Mood colorizer - Claude Docs

**URL**: https://docs.claude.com/en/resources/prompt-library/mood-colorizer

---

## Motivational muse

**URL**: https://docs.claude.com/en/resources/prompt-library/motivational-muse

**Contents**:
  - ​Example output
  - ​API request

**Examples**:

```text
import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=2000,
    temperature=1,
    system="Your task is to generate a personalized motivational message or affirmation based on the user's input. Address their specific needs and offer encouragement, support, and guidance. Employ a positive, empathetic, and inspiring tone to help the user feel m
...
```

---

## Multilingual support

**URL**: https://docs.claude.com/en/docs/build-with-claude/multilingual-support

**Contents**:
- ​Overview
- ​Performance data
- ​Best practices
- ​Language support considerations
- Prompt Engineering Guide
- Prompt Library

---

## Neologism creator

**URL**: https://docs.claude.com/en/resources/prompt-library/neologism-creator

**Contents**:
- ​Example output
- ​API request

**Examples**:

```text
import anthropic

client = anthropic.Anthropic(
  # defaults to os.environ.get("ANTHROPIC_API_KEY")
  api_key="my_api_key",
)
message = client.messages.create(
  model="claude-sonnet-4-5",
  max_tokens=1000,
  temperature=1,
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Can you help me create a new word for the act of pretending to understand something in order to avoid looking ignorant or uninformed?"
        }
      ]
    }
 
...
```

---

## PDF support

**URL**: https://docs.claude.com/en/docs/build-with-claude/pdf-support

**Contents**:
- ​Before you begin
  - ​Check PDF requirements
  - ​Supported platforms and models
  - ​Amazon Bedrock PDF Support
    - ​Document Processing Modes
    - ​Key Limitations
    - ​Common Issues
- ​Process PDFs with Claude

The system extracts the contents of the document.

Claude analyzes both the text and images to better understand the document.

Claude responds, referencing the PDF's contents if relevant.

**Examples**:

```text
curl https://api.anthropic.com/v1/messages \
   -H "content-type: application/json" \
   -H "x-api-key: $ANTHROPIC_API_KEY" \
   -H "anthropic-version: 2023-06-01" \
   -d '{
     "model": "claude-sonnet-4-5",
     "max_tokens": 1024,
     "messages": [{
         "role": "user",
         "content": [{
             "type": "document",
             "source": {
                 "type": "url",
                 "url": "https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-Octob
...
```

```text
# Method 1: Fetch and encode a remote PDF
curl -s "https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf" | base64 | tr -d '\n' > pdf_base64.txt

# Method 2: Encode a local PDF file
# base64 document.pdf | tr -d '\n' > pdf_base64.txt

# Create a JSON request file using the pdf_base64.txt content
jq -n --rawfile PDF_BASE64 pdf_base64.txt '{
    "model": "claude-sonnet-4-5",
    "max_tokens": 1024,
    "messages": [{
        "role": "user",
        "cont
...
```

```text
# First, upload your PDF to the Files API
curl -X POST https://api.anthropic.com/v1/files \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: files-api-2025-04-14" \
  -F "[email protected]"

# Then use the returned file_id in your message
curl https://api.anthropic.com/v1/messages \
  -H "content-type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: files-api-2025-04-14" \
 
...
```

---

## PII purifier

**URL**: https://docs.claude.com/en/resources/prompt-library/pii-purifier

**Contents**:
- ​Example output
- ​API request

**Examples**:

```python
import anthropic

client = anthropic.Anthropic( # defaults to os.environ.get("ANTHROPIC_API_KEY")
api_key="my_api_key",
)
message = client.messages.create(
  model="claude-sonnet-4-5",
  max_tokens=1000,
  temperature=0,
  system="You are an expert redactor. The user is going to provide you with some text. Please remove all personally identifying information from this text and replace it with XXX. It's very important that PII such as names, phone numbers, and home and email addresses, get replac
...
```

---

## PII purifier - Claude Docs

**URL**: https://docs.claude.com/en/resources/prompt-library/pii-purifier

---

## Perspectives ponderer

**URL**: https://docs.claude.com/en/resources/prompt-library/perspectives-ponderer

**Contents**:
- ​Example output
- ​API request

**Examples**:

```text
import anthropic

client = anthropic.Anthropic(
  # defaults to os.environ.get("ANTHROPIC_API_KEY")
  api_key="my_api_key",
)
message = client.messages.create(
  model="claude-sonnet-4-5",
  max_tokens=1000,
  temperature=1,
  messages=[
    {
    "role": "user",
    "content": [
        {
          "type": "text",
          "text": "Analyze the pros and cons of implementing a four-day workweek as a standard practice in the corporate world."
        }
      ]
    }
  ]
)
print(message.content)
```

---

## Philosophical musings

**URL**: https://docs.claude.com/en/resources/prompt-library/philosophical-musings

**Contents**:
  - ​Example output
  - ​API request

**Examples**:

```text
import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=2000,
    temperature=1,
    system="Your task is to discuss a philosophical concept or thought experiment on the given topic. Briefly explain the concept, present the main arguments and implications, and encourage critical thinking by posing open-ended questions. Maintain a balanced, obje
...
```

---

## Polyglot superpowers

**URL**: https://docs.claude.com/en/resources/prompt-library/polyglot-superpowers

**Contents**:
  - ​Example output
  - ​API request

**Examples**:

```text
import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=2000,
    temperature=0.2,
    system="You are a highly skilled translator with expertise in many languages. Your task is to identify the language of the text I provide and accurately translate it into the specified target language while preserving the meaning, tone, and nuance of the orig
...
```

---

## Polyglot superpowers - Claude Docs

**URL**: https://docs.claude.com/en/resources/prompt-library/polyglot-superpowers

---

## Portmanteau poet

**URL**: https://docs.claude.com/en/resources/prompt-library/portmanteau-poet

**Contents**:
- ​Example output
- ​API request

**Examples**:

```text
import anthropic

client = anthropic.Anthropic(
  # defaults to os.environ.get("ANTHROPIC_API_KEY")
  api_key="my_api_key",
)
message = client.messages.create(
  model="claude-sonnet-4-5",
  max_tokens=1000,
  temperature=1,
  system="You are an AI assistant with a knack for creating innovative portmanteaus. Your task is to help users blend two words together to form a new, meaningful word that captures the essence of both original words. Offer several options if possible.",
  messages=[
    {
 
...
```

---

## Product naming pro

**URL**: https://docs.claude.com/en/resources/prompt-library/product-naming-pro

**Contents**:
- ​Example output
  - ​API request

**Examples**:

```text
import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1000,
    temperature=1,
    system="Your task is to generate creative, memorable, and marketable product names based on the provided description and keywords. The product names should be concise (2-4 words), evocative, and easily understood by the target audience. Avoid generic or overly 
...
```

---

## Prompt Library

**URL**: https://docs.claude.com/en/resources/prompt-library/library

**Contents**:
- Prompt Library

Explore optimized prompts for a breadth of business and personal tasks.

---

## Prompt Library - Claude Docs

**URL**: https://docs.claude.com/en/resources/prompt-library/library

---

## Prose polisher

**URL**: https://docs.claude.com/en/resources/prompt-library/prose-polisher

**Contents**:
- ​Example output
- ​API request

**Examples**:

```text
import anthropic

client = anthropic.Anthropic(
  # defaults to os.environ.get("ANTHROPIC_API_KEY")
  api_key="my_api_key",
)
message = client.messages.create(
  model="claude-sonnet-4-5",
  max_tokens=2000,
  temperature=1,
  system="You are an AI copyeditor with a keen eye for detail and a deep understanding of language, style, and grammar. Your task is to refine and improve written content provided by users, offering advanced copyediting techniques and suggestions to enhance the overall quali
...
```

---

## Pun-dit

**URL**: https://docs.claude.com/en/resources/prompt-library/pun-dit

**Contents**:
- ​Example output
- ​API request

**Examples**:

```python
import anthropic

client = anthropic.Anthropic(  # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1000,
    temperature=1,
    system="You are an AI assistant with a witty sense of humor and a knack for crafting clever puns and wordplay. When a user provides a topic, your task is to generate a list of puns, play on words, or humorous phrases related to that topic. The wordplay should be o
...
```

---

## Pun-dit - Claude Docs

**URL**: https://docs.claude.com/en/resources/prompt-library/pun-dit

---

## Python bug buster

**URL**: https://docs.claude.com/en/resources/prompt-library/python-bug-buster

**Contents**:
- ​Example Output
- ​API Request

**Examples**:

```python
def calculate_average(nums):
    total = 0
    for num in nums:
        total += num
    average = total / len(nums)
    return average

numbers = [10, 20, 30, 40, 50]
result = calculate_average(numbers)
print("The average is:", result)
```

```javascript
import anthropic

client = anthropic.Anthropic(
  # defaults to os.environ.get("ANTHROPIC_API_KEY")
  api_key="my_api_key",
)
message = client.messages.create(
  model="claude-sonnet-4-5",
  max_tokens=1000,
  temperature=0,
  system="Your task is to analyze the provided Python code snippet, identify any bugs or errors present, and provide a corrected version of the code that resolves these issues. Explain the problems you found in the original code and how your fixes address them. The corrected
...
```

---

## Review classifier

**URL**: https://docs.claude.com/en/resources/prompt-library/review-classifier

**Contents**:
  - ​Example output

**Examples**:

```text
import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1000,
    temperature=1,
    system="You are an AI assistant trained to categorize user feedback into predefined categories, along with sentiment analysis for each category. Your goal is to analyze each piece of feedback, assign the most relevant categories, and determine the sentiment (po
...
```

---

## Riddle me this

**URL**: https://docs.claude.com/en/resources/prompt-library/riddle-me-this

**Contents**:
- ​Example Output
- ​API request

**Examples**:

```text
import anthropic

client = anthropic.Anthropic(
  # defaults to os.environ.get("ANTHROPIC_API_KEY")
  api_key="my_api_key",
)
message = client.messages.create(
  model="claude-sonnet-4-5",
  max_tokens=1000,
  temperature=0,
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Generate a clever riddle and provide a step-by-step guide to help the user arrive at the correct solutions. The riddle should be challenging but solvable with l
...
```

---

## SQL sorcerer

**URL**: https://docs.claude.com/en/resources/prompt-library/sql-sorcerer

**Contents**:
- ​Example output
- ​API Request

**Examples**:

```text
SELECT c.first_name, c.last_name, SUM(o.total_amount) AS total_spent
FROM Customers c
INNER JOIN Orders o ON c.customer_id = o.customer_id
LEFT JOIN Reviews r ON c.customer_id = r.customer_id
WHERE r.review_id IS NULL
GROUP BY c.customer_id, c.first_name, c.last_name;
```

```text
import anthropic

client = anthropic.Anthropic(
  # defaults to os.environ.get("ANTHROPIC_API_KEY")
  api_key="my_api_key",
)
message = client.messages.create(
  model="claude-sonnet-4-5",
  max_tokens=1000,
  temperature=0,
  system="Transform the following natural language requests into valid SQL queries. Assume a database with the following tables and columns exists: \n \nCustomers: \n- customer_id (INT, PRIMARY KEY) \n- first_name (VARCHAR) \n- last_name (VARCHAR) \n- email (VARCHAR) \n- pho
...
```

---

## Sci-fi scenario simulator

**URL**: https://docs.claude.com/en/resources/prompt-library/sci-fi-scenario-simulator

**Contents**:
  - ​Example output
  - ​API request

**Examples**:

```text
import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=2000,
    temperature=1,
    system="Your task is to explore a science fiction scenario and discuss the potential challenges and considerations that may arise. Briefly describe the scenario, identify the key technological, social, or ethical issues involved, and encourage the user to share
...
```

---

## Search results

**URL**: https://docs.claude.com/en/docs/build-with-claude/search-results

**Contents**:
- ​Key benefits
- ​How it works
  - ​Search result schema
  - ​Required fields
  - ​Optional fields
- ​Method 1: Search results from tool calls
  - ​Example: Knowledge base tool
- ​Method 2: Search results as top-level content

**Examples**:

```text
{
  "type": "search_result",
  "source": "https://example.com/article",  // Required: Source URL or identifier
  "title": "Article Title",                  // Required: Title of the result
  "content": [                               // Required: Array of text blocks
    {
      "type": "text",
      "text": "The actual content of the search result..."
    }
  ],
  "citations": {                             // Optional: Citation configuration
    "enabled": true                          // Enabl
...
```

```python
from anthropic import Anthropic
from anthropic.types import (
    MessageParam,
    TextBlockParam,
    SearchResultBlockParam,
    ToolResultBlockParam
)

client = Anthropic()

# Define a knowledge base search tool
knowledge_base_tool = {
    "name": "search_knowledge_base",
    "description": "Search the company knowledge base for information",
    "input_schema": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "descr
...
```

```python
from anthropic import Anthropic
from anthropic.types import (
    MessageParam,
    TextBlockParam,
    SearchResultBlockParam
)

client = Anthropic()

# Provide search results directly in the user message
response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    messages=[
        MessageParam(
            role="user",
            content=[
                SearchResultBlockParam(
                    type="search_result",
                    source="https://docs.
...
```

---

## Second-grade simplifier

**URL**: https://docs.claude.com/en/resources/prompt-library/second-grade-simplifier

**Contents**:
- ​Example Output
- ​API Request

**Examples**:

```javascript
import anthropic

client = anthropic.Anthropic(
  # defaults to os.environ.get("ANTHROPIC_API_KEY")
  api_key="my_api_key",
)
message = client.messages.create(
  model="claude-sonnet-4-5",
  max_tokens=1000,
  temperature=0,
  system="Your task is to take the text provided and rewrite it in a way that is easy for young learners in grades 3-5 to read and understand. Simplify advanced vocabulary, break down long sentences, explain difficult concepts in plain language, and present the information i
...
```

---

## Simile savant

**URL**: https://docs.claude.com/en/resources/prompt-library/simile-savant

**Contents**:
- ​Example Output
- ​API Request

**Examples**:

```text
import anthropic

client = anthropic.Anthropic(
  # defaults to os.environ.get("ANTHROPIC_API_KEY")
  api_key="my_api_key",
)
message = client.messages.create(
  model="claude-sonnet-4-5",
  max_tokens=1000,
  temperature=1,
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Help me create some similes to describe a person's laughter that is joyful and contagious?"
        }
      ]
    }
  ]
)
print(message.content)
```

---

## Simile savant - Claude Docs

**URL**: https://docs.claude.com/en/resources/prompt-library/simile-savant

---

## Socratic sage

**URL**: https://docs.claude.com/en/resources/prompt-library/socratic-sage

**Contents**:
  - ​Example output
  - ​API request

**Examples**:

```text
import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1000,
    temperature=1,
    system="You are an AI assistant capable of having in-depth Socratic style conversations on a wide range of topics. Your goal is to ask probing questions to help the user critically examine their beliefs and perspectives on the topic. Do not just give your own v
...
```

---

## Spreadsheet sorcerer

**URL**: https://docs.claude.com/en/resources/prompt-library/spreadsheet-sorcerer

**Contents**:
  - ​Example output
  - ​API request

**Examples**:

```text
import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1000,
    temperature=0,
    system="Your task is to generate a CSV spreadsheet containing the specified type of data. The spreadsheet should be well-organized, with clear column headers and appropriate data types for each column. Ensure that the data is realistic, diverse, and formatted c
...
```

---

## Storytelling sidekick

**URL**: https://docs.claude.com/en/resources/prompt-library/storytelling-sidekick

**Contents**:
- ​Example output
- ​API Request

**Examples**:

```text
import anthropic

client = anthropic.Anthropic(
  # defaults to os.environ.get("ANTHROPIC_API_KEY")
  api_key="my_api_key",
)
message = client.messages.create(
  model="claude-sonnet-4-5",
  max_tokens=2000,
  temperature=1,
  system="You are an AI assistant with a passion for creative writing and storytelling. Your task is to collaborate with users to create engaging stories, offering imaginative plot twists and dynamic character development. Encourage the user to contribute their ideas and bui
...
```

---

## System Prompts

**URL**: https://docs.claude.com/en/release-notes/system-prompts

**Contents**:
- ​Claude Haiku 4.5
- ​Claude Sonnet 4.5
- ​Claude Opus 4.1
- ​Claude Opus 4
- ​Claude Sonnet 4
- ​Claude Sonnet 3.7
- ​Claude Sonnet 3.5
- ​Claude Haiku 3.5

---

## Ticket routing

**URL**: https://docs.claude.com/en/docs/about-claude/use-case-guides/ticket-routing

**Contents**:
- ​Define whether to use Claude for ticket routing
- ​Build and deploy your LLM support workflow
  - ​Understand your current support approach
  - ​Define user intent categories
  - ​Establish success criteria
  - ​Choose the right Claude model
  - ​Build a strong prompt
  - ​Deploy your prompt

You have limited labeled training data available

Your classification categories are likely to change or evolve over time

You need to handle complex, unstructured text inputs

Your classification rules are based on semantic understanding

You require interpretable reasoning for classification decisions

You want to handle edge cases and ambiguous tickets more effectively

You need multilingual support without maintaining separate models

Training and education

Classification consistency

Multilingual handling

First-contact resolution rate

Average handling time

Customer satisfaction scores

Self-service deflection rate

Customers make implicit requests

Claude prioritizes emotion over intent

Multiple issues cause issue prioritization confusion

**Examples**:

```python
def classify_support_request(ticket_contents):
    # Define the prompt for the classification task
    classification_prompt = f"""You will be acting as a customer support ticket classification system. Your task is to analyze customer support requests and output the appropriate classification intent for each request, along with your reasoning. 

        Here is the customer support request you need to classify:

        <request>{ticket_contents}</request>

        Please carefully analyze the a
...
```

```python
import anthropic
import re

# Create an instance of the Claude API client
client = anthropic.Anthropic()

# Set the default model
DEFAULT_MODEL="claude-3-5-haiku-20241022"

def classify_support_request(ticket_contents):
    # Define the prompt for the classification task
    classification_prompt = f"""You will be acting as a customer support ticket classification system. 
        ...
        ... The reasoning should be enclosed in <reasoning> tags and the intent in <intent> tags. Return only th
...
```

```python
import anthropic
import re

# Create an instance of the Claude API client
client = anthropic.Anthropic()

# Set the default model
DEFAULT_MODEL="claude-3-5-haiku-20241022"

def classify_support_request(request, actual_intent):
    # Define the prompt for the classification task
    classification_prompt = f"""You will be acting as a customer support ticket classification system. 
        ...
        ...The reasoning should be enclosed in <reasoning> tags and the intent in <intent> tags. Return o
...
```

---

## Time travel consultant

**URL**: https://docs.claude.com/en/resources/prompt-library/time-travel-consultant

**Contents**:
- ​Example output
- ​API Request

**Examples**:

```text
import anthropic

client = anthropic.Anthropic(
  # defaults to os.environ.get("ANTHROPIC_API_KEY")
  api_key="my_api_key",
)
message = client.messages.create(
  model="claude-sonnet-4-5",
  max_tokens=2000,
  temperature=1,
  system="You are an AI assistant with expertise in physics, philosophy, and science fiction. Your task is to help users explore and understand the implications of hypothetical time travel scenarios. Provide detailed insights on the potential consequences, paradoxes, and eth
...
```

---

## Token counting

**URL**: https://docs.claude.com/en/docs/build-with-claude/token-counting

**Contents**:
- ​How to count message tokens
  - ​Supported models
  - ​Count tokens in basic messages
  - ​Count tokens in messages with tools
  - ​Count tokens in messages with images
  - ​Count tokens in messages with extended thinking
  - ​Count tokens in messages with PDFs
- ​Pricing and rate limits

Does token counting use prompt caching?

**Examples**:

```text
import anthropic

client = anthropic.Anthropic()

response = client.messages.count_tokens(
    model="claude-sonnet-4-5",
    system="You are a scientist",
    messages=[{
        "role": "user",
        "content": "Hello, Claude"
    }],
)

print(response.json())
```

```text
{ "input_tokens": 14 }
```

```text
import anthropic

client = anthropic.Anthropic()

response = client.messages.count_tokens(
    model="claude-sonnet-4-5",
    tools=[
        {
            "name": "get_weather",
            "description": "Get the current weather in a given location",
            "input_schema": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Franci
...
```

---

## Tongue twister

**URL**: https://docs.claude.com/en/resources/prompt-library/tongue-twister

**Contents**:
- ​Example Output
- ​API Request

**Examples**:

```text
import anthropic

client = anthropic.Anthropic(
  # defaults to os.environ.get("ANTHROPIC_API_KEY")
  api_key="my_api_key",
)
message = client.messages.create(
  model="claude-sonnet-4-5",
  max_tokens=1000,
  temperature=1,
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Generate complex and creative tongue twisters. Aim to create tongue twisters that are not only challenging to say but also engaging, entertaining, and potential
...
```

---

## Trivia generator

**URL**: https://docs.claude.com/en/resources/prompt-library/trivia-generator

**Contents**:
- ​Example Output
- ​API Request

**Examples**:

```python
import anthropic

client = anthropic.Anthropic(
  # defaults to os.environ.get("ANTHROPIC_API_KEY")
  api_key="my_api_key",
)
message = client.messages.create(
  model="claude-sonnet-4-5",
  max_tokens=2000,
  temperature=0.5,
  messages=[
    {
    "role": "user",
    "content": [
        {
          "type": "text",
          "text": "Generate trivia questions on various topics and provide hints to help users arrive at the correct answer. Select from a diverse set of categories and create quest
...
```

---

## Tweet tone detector - Claude Docs

**URL**: https://docs.claude.com/en/resources/prompt-library/tweet-tone-detector

---

## Tweet tone detector

**URL**: https://docs.claude.com/en/resources/prompt-library/tweet-tone-detector

**Contents**:
  - ​Example output
  - ​API request

**Examples**:

```text
import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1000,
    temperature=0,
    system="Your task is to analyze the provided tweet and identify the primary tone and sentiment expressed by the author. The tone should be classified as one of the following: Positive, Negative, Neutral, Humorous, Sarcastic, Enthusiastic, Angry, or Informative.
...
```

---

## VR fitness innovator

**URL**: https://docs.claude.com/en/resources/prompt-library/vr-fitness-innovator

**Contents**:
- ​Example Output
- ​API Request

**Examples**:

```text
import anthropic

client = anthropic.Anthropic(
  # defaults to os.environ.get("ANTHROPIC_API_KEY")
  api_key="my_api_key",
)
message = client.messages.create(
  model="claude-sonnet-4-5",
  max_tokens=1000,
  temperature=1,
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Your task is to generate a list of innovative and engaging ideas for virtual reality (VR) fitness games. Consider various game genres, unique gameplay mechanics
...
```

---

## Website wizard

**URL**: https://docs.claude.com/en/resources/prompt-library/website-wizard

**Contents**:
- ​Example output
- ​API request

**Examples**:

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EduQuest - Online Learning Platform</title>
    <style>
        /* CSS Styles */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }

        header {
            background-color: #333;
            color: #fff;
            padding: 20px;
            position: fixed;
            top
...
```

```python
import anthropic

client = anthropic.Anthropic( # defaults to os.environ.get("ANTHROPIC_API_KEY")
api_key="my_api_key",
)
message = client.messages.create(
  model="claude-sonnet-4-5",
  max_tokens=4000,
  temperature=0,
  system="Your task is to create a one-page website based on the given specifications, delivered as an HTML file with embedded JavaScript and CSS. The website should incorporate a variety of engaging and interactive design features, such as drop-down menus, dynamic text and cont
...
```

---

## 

**URL**: https://docs.claude.com/en/home

**Contents**:
- Claude Developer Platform
- Get started
- Features overview
- What's new in Claude 4.5
- API reference
- Claude Console
- Release notes
- Claude Code

Learn how to get started with the Claude Developer Platform and Claude Code.

---
