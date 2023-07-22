import random
import streamlit as st

from app.dataset import comics
from app.constants import ATTRIBUTION as attribution
from app.utils.formatters import formatNumber

def view(items, total):
    count = len(items)
    formatted = formatNumber(total)
    title = f"Marvel Comics ({formatted})"
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
                    st.write(char['id'])
                    st.image(char['thumbnail'], width=150)
                    st.write(char['title'])
        except Exception as e:
            print(e)

        st.divider()
    st.write(attribution)


def show():
    items = comics.load()
    total = len(items)
    random_items = random.sample(items, 20)
    view(random_items, total)
