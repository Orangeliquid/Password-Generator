import streamlit as st
import time
import random

from utils.generator import generate_password
from utils.strength import evaluate_strength, LABEL_COLORS
from models.password_options import PasswordOptions


def handle_generate(options: PasswordOptions):
    password = generate_password(options=options)
    st.session_state["generated_password"] = password

    history = st.session_state["history"]
    history.insert(0, password)
    st.session_state["history"] = history[0:5]

    strength, label = evaluate_strength(password)
    st.session_state["strength"] = strength
    st.session_state["label"] = label

    history_label = st.session_state["history_label"]
    history_label.insert(0, label)
    st.session_state["history_label"] = history_label[0:5]


def clear_generate():
    st.session_state.pop("generated_password", None)
    st.session_state.pop("strength", None)
    st.session_state.pop("label", None)


st.markdown(
    "<div style='color:#ff9400; font-family:monospace; text-align:left; font-style:bold; font-size:48px;'>Orangeliquid</div>",
    unsafe_allow_html=True
)
st.markdown(
    "<div style='color:#fffafa; font-family:monospace; text-align:left; font-style:italic; font-size:28px;'>Password Generator</div>",
    unsafe_allow_html=True
)

st.markdown("----")

if "history" not in st.session_state:
    st.session_state["history"] = []
    st.session_state["history_label"] = []

left_column, right_column = st.columns(2)

with right_column:
    uppercase_prompt = st.checkbox(
        "Uppercase Letters?",
        value=True,
        on_change=clear_generate
    )
    lowercase_prompt = st.checkbox(
        "Lowercase Letters?",
        value=True,
        on_change=clear_generate
    )
    numbers_prompt = st.checkbox(
        "Include Numbers?",
        value=True,
        on_change=clear_generate
    )
    symbols_prompt = st.checkbox(
        "Include Symbols?",
        value=True,
        on_change=clear_generate
    )

with left_column:
    length = st.number_input(
        "How long do you want your password?",
        min_value=8,
        max_value=128,
        value=12,
        step=1,
        key="length",
        on_change=clear_generate
    )

opts = PasswordOptions(
    length=length,
    include_uppercase_letters=uppercase_prompt,
    include_lowercase_letters=lowercase_prompt,
    include_numbers=numbers_prompt,
    include_symbols=symbols_prompt,
)

st.button(
    "Generate Password",
    on_click=lambda: handle_generate(options=opts)
)

if "generated_password" in st.session_state:
    with st.spinner("Generating password..."):
        time.sleep(random.uniform(1, 2))
        st.success("Password generated successfully!")

        st.text_input(
            "Generated Password",
            value=st.session_state["generated_password"],
            disabled=True,
            type="default",
        )

        label_col, score_col = st.columns(2)
        with label_col:
            color = LABEL_COLORS.get(st.session_state['label'], "black")
            st.markdown(
                f"**Strength:**"
                f"<span style='color:{color}; font-family:monospace;'> {st.session_state['label']}</span>",
                unsafe_allow_html=True
            )

        with score_col:
            st.write(f"**Score:** {st.session_state['strength']}/5")

        st.markdown("----")

        if st.session_state["history"]:
            st.write("### Last 5 Generated Passwords")
            history_and_label = zip(st.session_state["history"], st.session_state["history_label"], strict=True)
            for i, (pw, label) in enumerate(history_and_label, 1):
                st.code(f"{pw}", language="bash")

                color = LABEL_COLORS.get(label, "black")
                st.markdown(
                    f"<span style='color:{color}; font-family:monospace;'>{label}</span>", unsafe_allow_html=True
                )
