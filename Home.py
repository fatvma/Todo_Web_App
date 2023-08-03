import streamlit as st
import functions


st.set_page_config(layout="wide")
todos=functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todo(todos)


st.title("MY TO-DO APP")
st.subheader("Welcome to my to-do application")
st.write("this app is made to track your productivity")


for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todo(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="",placeholder="Enter a to-do",
              on_change=add_todo, key="new_todo")

# st.session_state