import streamlit as st
from example_interviews import example_interview

def main():
    st.title('User Interview Analysis')

    st.write('Upload your user interviews, enter the questions you want to ask about the data and get back a list of quotes that are relevant to the questions you care about.')

    use_example_interview = st.checkbox("Try example interview")

    if use_example_interview:
        interview = st.text_area("", example_interview, height=600, max_chars=50000)
    else:
        interview = st.text_area("Paste in an interview:", '', height=600, max_chars=50000)

    if st.button('Submit'):
        st.subheader('Interview:')
        st.markdown(
            f"""
            <div style="overflow-y: scroll; height: 300px;">
                {interview}
            </div>
            """,
            unsafe_allow_html=True
        )

if __name__ == '__main__':
    main()