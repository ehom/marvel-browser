import streamlit as st

from app.views import series_page
from app.views import creators_page
from app.views import chars_page


menu_items = {
    "About": "A sample app featuring content from Marvel",
    "Get Help": "https://github.com/ehom",
    "Report a bug": "https://github.com/ehom"
}


def main(): 
    st.set_page_config(page_title="Marvel Browser",
                       page_icon="\u24c2", menu_items=menu_items)

    with st.sidebar:
        st.header("Marvel Browser")
        selection = st.radio("View", ["Characters", "Series", "Creators"])

    if selection == "Series":
        series_page.show()
    elif selection == "Creators":
        creators_page.show()
    else:
        chars_page.show()


if __name__ == "__main__":
    main()
