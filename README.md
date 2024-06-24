# Course Assistant Chatbot

This is a Streamlit application that acts as a course advisor chatbot, leveraging OpenAI's GPT-3.5-turbo model. The chatbot reads course data from a JSON file and provides recommendations based on user input.

## Features

- **Useful Responses**: The chatbot generates detailed and relevant course recommendations, summaries, and prerequisites to help students make informed decisions. Unlike a generic chatbot, it utilizes a specific course catalog provided in the JSON file, ensuring personalized and accurate advice based on the actual courses available.
- **Variety of Queries**: The chatbot can handle a wide range of queries, including specific course details, topic overviews, prerequisite information, and general course advice.
- **Interactive Chat Interface**: Communicate with the chatbot in a chat-like interface.
- **Course Recommendations**: The chatbot uses the provided course data to recommend courses and answer questions.
- **Dynamic Conversations**: The chatbot can ask for more information to provide better recommendations.

## Watch the Demo Video

[![Ollama Installation Video]([https://img.youtube.com/vi/Af362vPLuVQ/0.jpg)](https://www.youtube.com/watch?v=Af362vPLuVQ](https://www.youtube.com/watch?v=MMxdLhb5eeI))


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

3. **Setup secrets.toml file**
Store your OpenAI API key in Streamlit secrets. Create a file named .streamlit/secrets.toml with the following content:
```bash
OPENAI_API_KEY="ADD YOUR API KEY"
```

4. **Run the streamlit app**
Make sure you are in the root directory of the repository
```bash
streamlit run app.py
```

5. **Interact With the chatbot**
Open your web browser and navigate to http://localhost:8501. Start chatting with the course assistant to get course recommendations and more information.
