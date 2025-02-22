import streamlit as st

st.markdown(
    """
    <style>
        /* Target selectbox text */
        [data-testid="stSidebar"] [data-baseweb="select"] div {
            font-size: 14px !important;
        }

        /* Target radio button labels */
        [data-testid="stSidebar"] label {
            font-size: 12px !important;
        }

        /* Target input widgets (text inputs, number inputs) */
        [data-testid="stSidebar"] input {
            font-size: 20px !important;
        }

        /*Target slider labels*/
        [data-testid="stSidebar"] div[data-testid="stMarkdownContainer"] p{
            font-size: 20px !important;
        }

    </style>
    """,
    unsafe_allow_html=True,
)

# Example sidebar widgets
st.sidebar.selectbox("Select an option", ["A", "B", "C"])
st.sidebar.radio("Choose one", ["Option 1", "Option 2"])
st.sidebar.text_input("Enter text")
st.sidebar.slider("Pick a number", 0, 100)