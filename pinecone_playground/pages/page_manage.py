import streamlit as st
import pinecone

from .base import Page
from .. import utils


class PageManage(Page):
    title = "Manage Pinecone Indexes"

    def __init__(self, app):
        super().__init__(app)

    def render_list_indexes(self, container):
        with container:
            st.subheader("List Pinecone indexes")

            st.code("""pinecone.list_indexes()""")
            if st.button("Run", key="list indexes"):
                with st.spinner("Running..."):
                    indexes = pinecone.list_indexes()
                with st.beta_expander("Output", True):
                    st.json(indexes)

    def render_create_index(self, container):
        with container:
            st.subheader("Create a Pinecone index")

            # input index name
            self.cmp_input_index_name(st.beta_container(), key="create index")

            # show code
            index_name = self.app.store.pinecone.index_name
            st.code(f"""pinecone.create_index("{index_name}")""")
            if st.button("Run", key="create index"):
                result = {}
                with st.spinner("Running..."):
                    try:
                        with utils.redirect_stderr("info"):
                            result = pinecone.create_index(index_name)
                    except Exception as e:
                        st.exception(e)
                with st.beta_expander("Output", True):
                    st.json(result)

    def render_delete_index(self, container):
        with container:
            st.subheader("Delete a Pinecone index")

            self.cmp_input_index_name(st.beta_container(), key="delete index")

            index_name = self.app.store.pinecone.index_name
            st.code(f"""pinecone.delete_index("{index_name}")""")
            if st.button("Run", key="delete index"):
                result = {}
                with st.spinner("Running..."):
                    try:
                        with utils.redirect_stderr("info"):
                            result = pinecone.delete_index(index_name)
                    except Exception as e:
                        st.exception(e)
                with st.beta_expander("Output", True):
                    st.json(result)

    def render_describe_index(self, container):
        with container:
            st.subheader("Describe a Pinecone index")

            self.cmp_input_index_name(st.beta_container(), key="describe index")

            index_name = self.app.store.pinecone.index_name
            st.code(f"""pinecone.describe_index("{index_name}")""")
            if st.button("Run", key="describe index"):
                result = {}
                with st.spinner("Running..."):
                    try:
                        result = pinecone.describe_index(index_name)
                    except Exception as e:
                        st.exception(e)
                with st.beta_expander("Output", True):
                    st.json(result)

    def cmp_input_index_name(self, container, key=None):
        with container:
            index_name = self.app.store.pinecone.index_name or ""
            index_name = st.text_input("Enter the index name", key=key or "index name", value=index_name)
            self.app.store.pinecone.index_name = index_name

    def render(self):
        st.header(self.title)
        self.render_list_indexes(st.beta_container())
        self.render_create_index(st.beta_container())
        self.render_delete_index(st.beta_container())
        self.render_describe_index(st.beta_container())
