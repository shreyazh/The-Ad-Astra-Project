import streamlit as st
import datetime
import pandas as pd
import numpy as np
import plotly.graph_objects as go


st.set_page_config(layout="wide", initial_sidebar_state="expanded")
st.title("Productivity Hub")


selected = st.sidebar.selectbox("Navigation", ["Dashboard", "Tasks", "Calendar", "Notes", "Time Tracking", "Collaboration", "Settings"])


if selected == "Dashboard":
    st.write("Welcome to your Productivity Hub!")
    col1, col2, col3 = st.columns(3)
    col1.metric("Tasks", 10, delta="5 new tasks")
    col2.metric("Upcoming Events", 3, delta="2 events today")
    col3.metric("Time Tracked", "5h 30m", delta="1h 30m")


if selected == "Tasks":
    st.subheader("Task Management")
    task_df = pd.DataFrame({
        "Task": ["Task 1", "Task 2", "Task 3"],
        "Priority": ["High", "Medium", "Low"],
        "Due Date": ["2024-03-15", "2024-03-20", "2024-03-25"],
        "Status": ["To-Do", "In Progress", "Done"],
    })
    st.write(task_df)
    with st.form("task_form"):
        task_name = st.text_input("Task Name")
        task_priority = st.selectbox("Priority", ["High", "Medium", "Low"])
        task_due_date = st.date_input("Due Date")
        submit_button = st.form_submit_button("Add Task")
        if submit_button:
            task_df = task_df._append({"Task": task_name, "Priority": task_priority, "Due Date": task_due_date, "Status": "To-Do"}, ignore_index=True)



if selected == "Calendar":
    st.subheader("Calendar")
    calendar_date = st.date_input("Select Date")
    events_df = pd.DataFrame({
        "Event": ["Event 1", "Event 2", "Event 3"],
        "Start Date": ["2024-03-15", "2024-03-20", "2024-03-25"],
        "End Date": ["2024-03-16", "2024-03-21", "2024-03-26"],
    })
    st.write(events_df)
    with st.form("event_form"):
        event_name = st.text_input("Event Name")
        event_start_date = st.date_input("Start Date")
        event_end_date = st.date_input("End Date")
        submit_button = st.form_submit_button("Add Event")
        if submit_button:
            events_df = events_df._append({"Event": event_name, "Start Date": event_start_date, "End Date": event_end_date}, ignore_index=True)


if selected == "Notes":
    st.subheader("Note-Taking")
    note_df = pd.DataFrame({
        "Note": ["Note 1", "Note 2", "Note 3"],
        "Content": ["This is note 1", "This is note 2", "This is note 3"],
    })
    st.write(note_df)
    with st.form("note_form"):
        note_name = st.text_input("Note Name")
        note_content = st.text_area("Note Content")
        submit_button = st.form_submit_button("Add Note")
        if submit_button:
            note_df = note_df._append({"Note": note_name, "Content": note_content}, ignore_index=True)


if selected == "Time Tracking":
    st.subheader("Time Tracking")
    time_df = pd.DataFrame({
        "Task": ["Task 1", "Task 2", "Task 3"],
        "Time": [5, 3, 2],
    })
    st.write(time_df)
    fig = go.Figure(data=[go.Pie(labels=time_df["Task"], values=time_df["Time"])])
    st.plotly_chart(fig)


if selected == "Collaboration":
    st.subheader("Collaboration")
    collab_df = pd.DataFrame({
        "Member": ["Member 1", "Member 2", "Member 3"],
        "Role": ["Admin", "Editor", "Viewer"],
    })
    st.write(collab_df)
    with st.form("collab_form"):
        collab_member = st.text_input("Member Name")
        collab_role = st.selectbox("Role", ["Admin", "Editor", "Viewer"])
        submit_button = st.form_submit_button("Add Member")
        if submit_button:
            collab_df = collab_df._append({"Member": collab_member, "Role": collab_role}, ignore_index=True)

if selected == "Settings":
    st.subheader("Settings")
    st.write("Coming soon!")

st.sidebar.caption("Made with love by Shreyash")

