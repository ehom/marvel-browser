import random
import streamlit as st

from app.dataset import heroes


def view(items, total):
    count = len(items)
    title = f"Marvel Characters ({total})"
    print(title)

    st.title(title)
    st.divider()

    COLS = 4

    count = len(items)

    for i in range(0, count, COLS):
        columns = st.columns(4)
        try:
            for n in range(0, COLS):
                char = items[i+n]
                with columns[n]:
                    st.write(char['name'])
                    st.image(char['thumbnail'], width=150)
                    st.write(char['id'])
        except Exception as e:
            print(e)

        st.divider()


def show():
    chars = heroes.load()
    total = len(chars)
    random_items = random.sample(chars, 20)
    view(random_items, total)
