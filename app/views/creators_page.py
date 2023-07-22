import random
import json
import streamlit as st
from app.dataset import creators
from app.constants import ATTRIBUTION as attribution
from pprint import PrettyPrinter
pp = PrettyPrinter(indent=4, width=80)


def view(items, total):
    title = f"Marvel Creators ({total})"
    print(title)

    st.title(title)
    st.divider()

    COLS = 4

    count = len(items)

    for i in range(0, count, COLS):
        columns = st.columns(COLS)
        try:
            for n in range(0, COLS):
                item = items[i+n]
                with columns[n]:
                    st.write(item['id'])
                    st.image(item['thumbnail'], width=150)
                    st.write(item['fullName']) 
        except Exception as e:
            print(e)

        st.divider()
    st.write(attribution)

def show():
    items = creators.load()
    total = len(items)
    random_items = random.sample(items, 20)
    view(random_items, total)
