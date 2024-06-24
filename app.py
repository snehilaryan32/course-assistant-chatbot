from openai import OpenAI
import streamlit as st
import json

st.title("Course Assistant")
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

json_file_path = "courses.json"
with open(json_file_path, "r") as f:
    course_data = str(json.load(f))

# course_data = json_content.dumps()

prompt_init = f'''Hello You are a course advisor. Accoring to the prompt use the following information
                to reccomend courses to the student : {course_data}. Feel free to ask more questions to get more information 
                and provide better recommendations. Provide a summary of the course description, topics and 
                technologies taught and the pre requisites required to take the course.
                '''


if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"
    

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": prompt_init}
    ]

for message in st.session_state.messages:
    if message["role"] in ["user", "assistant"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)

    st.session_state.messages.append({"role": "assistant", "content": response})