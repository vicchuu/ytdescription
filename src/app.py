#for user interaction

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
user_input = st.text_input("Enter text or keywords", value="AI, automation, efficiency")

# Process Button for Text Generation
if st.button("Process"):
    with st.spinner("Generating description..."):
        st.session_state["generated_output"] = generate_description(user_input)
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
