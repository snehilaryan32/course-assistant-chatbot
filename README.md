# Course Assistant Chatbot

This is a Streamlit application that acts as a course advisor chatbot, leveraging OpenAI's GPT-3.5-turbo model. The chatbot reads course data from a JSON file and provides recommendations based on user input.

## Features

- **Interactive Chat Interface**: Communicate with the chatbot in a chat-like interface.
- **Course Recommendations**: The chatbot uses the provided course data to recommend courses and answer questions.
- **Dynamic Conversations**: The chatbot can ask for more information to provide better recommendations.

## Installation

1. **Clone the repository**:

```bash
git clone https://github.com/your-repo/course-assistant-chatbot.git
cd course-assistant-chatbot
```

2. **Install The Dependencies**
```bash
pip install streamlit openai
```

3. **Setup secrets.toml file in .streamlit directory**
```bash
mkdir .streamlit
```

```
OPENAI_API_KEY="ADD YOUR API KEY"
```
