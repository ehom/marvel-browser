import streamlit as st

from app.views import series_page
from app.views import creators_page
from app.views import chars_page
from app.views import comics_page


menu_items = {
    "About": "A sample app featuring content from Marvel",
    "Get Help": "https://github.com/ehom/marvel-browser/blob/main/README.md",
    "Report a bug": "https://github.com/ehom/marvel-browser/issues"
}


def main(): 
    superhero = "\U0001F9B8"

    st.set_page_config(page_title="Marvel Browser",
                       page_icon=superhero, menu_items=menu_items)

    with st.sidebar:
        st.header("Marvel Browser")
        selection = st.radio("View", ["Comics", "Characters", "Creators", "Series"])

    if selection == "Series":
        series_page.show()
    elif selection == "Creators":
        creators_page.show()
    elif selection == "Comics":
       comics_page.show()
    else:
        chars_page.show()


if __name__ == "__main__":
    main()
