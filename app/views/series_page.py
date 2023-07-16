import json
import random
import streamlit as st
from app.constants import ATTRIBUTION as attribution
from pprint import PrettyPrinter
pp = PrettyPrinter(indent=4, width=80)


class Model:
    def __init__(self):
        self._items = self.get_items()

    def get_items(self):
        with open("app/dataset/series.json") as f:
            items = json.load(f)
            # pp.pprint(items)
            count = len(items)
        return items

    @property
    def items(self):
        return self._items


def view(items, total):
    title = f"Marvel Comics Series ({total})"
    print(title)

    st.title(title)
    st.divider()

    for item in items:
        st.write(item['title'])
        st.image(item['thumbnail'], width=150)
        st.write(item['id'])
        if item['description']:
            st.write("**Description**:")
            st.write(item['description'])
        st.divider()
    st.write(attribution)

def show():
    items = Model().items
    total = len(items)
    random_items = random.sample(items, 20)
    view(random_items, total)
