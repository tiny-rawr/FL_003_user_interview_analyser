import streamlit as st
from example_interviews import example_interview

def main():
    if 'interviews' not in st.session_state:
        st.session_state.interviews = []

    st.title('User Interview Analysis')
    st.write('Upload your user interviews, enter the questions you want to ask about the data, and get back a list of quotes that are relevant to the questions you care about.')

    use_example_interview = st.checkbox("Try example interview")

    if use_example_interview:
        interview = st.text_area("", example_interview, height=400, max_chars=50000)
    else:
        interview = st.text_area("Paste in an interview:", '', height=400, max_chars=50000)

    if st.button('Submit'):
        interviews = st.session_state.get('interviews', [])
        if interview not in interviews:
          interviews.append(interview)
          st.session_state.interviews = interviews
          st.success("Interview added successfully!")
        else:
          st.warning("This interview has already been added.")

    if st.session_state.interviews:
        st.subheader('Interviews:')
        interview_options = [f"Interview {i + 1}" for i in range(len(st.session_state.interviews))]
        selected_index = st.selectbox("Select an interview:", options=interview_options, index=0)

        # Convert "Interview X" to the integer X-1
        interview_index = int(selected_index.split()[-1]) - 1

        st.markdown(
            f"""
            <div style="overflow-y: scroll; height: 300px;">
                {st.session_state.interviews[interview_index]}
            </div>
            """,
            unsafe_allow_html=True
        )

if __name__ == '__main__':
    main()