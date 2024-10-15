#for user interaction
import os

#setup Langsmith trackin
os.environ["LANGCHAIN_API_KEY"] = "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"
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "GENAIwithLangChain"
os.environ["COHERE_API_KEY"] = "6ZVrRtmctd5QDGCHS9eqQ5v2IMuEapoIj97uVoWR"
os.environ['USER_AGENT'] = 'myagent'
token = "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"
from generateText import generate_description
from translatingText import load_translation_model ,  translate_text
import streamlit as st
# key_words =["coffee" ,"breakup"]
#
# print("******REsult*********")
# result = generate_description(keywords=key_words)
# print(result)
#
#
# token , model = load_translation_model()
# translate_text = translate_text(result,token,model)
#
# print("****************Translated**************")
# print(f"{translate_text}")


# Streamlit app UI
st.title("NLP Generative AI with Translation")

if "generated_output" not in st.session_state:
    st.session_state["generated_output"] = ""
if "translated_output" not in st.session_state:
    st.session_state["translated_output"] = ""
# User input for text/keywords
user_input = st.text_input("Enter text or keywords", value="india independence after 1947")
models = {
    "LLaMA (Meta's LLaMA)": "meta-llama/LLaMA-7b-hf",#meta-llama/Llama-2-7b-chat-hf
    "GPT-J (EleutherAI)": "EleutherAI/gpt-j-6B",
    "GPT-NeoX-20B (EleutherAI)": "EleutherAI/gpt-neox-20b",
    "BLOOM (BigScience)": "bigscience/bloom-1b1",
    "T5 (Text-to-Text Transfer Transformer) small": "t5-small"
}
selected_model = st.selectbox("Select the llm model",
                              options=list(models.keys()))
model_selected = models[selected_model]
# Process Button for Text Generation
if st.button("Process"):
    with st.spinner("Generating description... first time model loading takes some more time."):


        st.session_state["generated_output"] = generate_description(user_input,model_selected,token)
        st.session_state["translated_output"] = ""
        #st.subheader("Generated Output")
        #st.write( st.session_state["generated_output"])

if st.session_state["generated_output"]:
    st.subheader("Generated Output")
    st.write(st.session_state["generated_output"])
        # Dropdown for Language Selection
    language_options = {
            "French": "fr",
            "Spanish": "es",
            "German": "de",
            "Chinese": "zh",
            "Hindi": "hi"
    }

    selected_language = st.selectbox("Select the language to translate the output", options=list(language_options.keys()))


    # Button to translate generated output
    if st.button("Translate"):
        print(f"selected language:{selected_language}")
        with st.spinner(f"Translating to {selected_language}..."):

            target_lang_code = language_options[selected_language]
            token, model = load_translation_model('en', target_lang_code)
            print("token and model is done")
            st.session_state["translated_output"] = translate_text( st.session_state["generated_output"], token ,model)

if st.session_state["translated_output"]:
    st.subheader(f"Translated Output")
    st.write(st.session_state["translated_output"])
# print(f"translated text :{translated_output}")
#             st.subheader(f"Translated Output in {selected_language}")
#             st.write(translated_output)
