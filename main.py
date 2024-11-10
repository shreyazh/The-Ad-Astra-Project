import streamlit as st
import datetime
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.set_page_config(layout="wide", initial_sidebar_state="expanded")
st.title("The Ad Astra Project")

st.markdown("""
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
        }
        .tab {
            background-color: #337ab7;
            color: #fff;
            padding: 10px;
            border-radius: 5px;
        }
        .tab:hover {
            background-color: #23527c;
        }
        .header {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .subheader {
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 5px;
        }
        .card {
            background-color: #fff;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .card:hover {
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
        }
    </style>
""", unsafe_allow_html=True)

try:
    st.sidebar.image("Ad astra_20241110_213644_0000.png", width=100)
except Exception as e:
    st.sidebar.write("Logo not found.")

st.sidebar.header("Navigation")
selected = st.sidebar.selectbox("", ["Dashboard", "Tasks", "Calendar", "Notes", "Time Tracking", "Collaboration", "Settings", "Study Tracker", "Walk Tracker", "Gym Tracker", "Calorie Tracker"])
tab_dashboard, tab_tasks, tab_calendar, tab_notes, tab_time_tracking, tab_collaboration, tab_settings, tab_study, tab_walk, tab_gym, tab_calorie = st.tabs([
    "Dashboard", 
    "Tasks", 
    "Calendar", 
    "Notes", 
    "Time Tracking", 
    "Collaboration", 
    "Settings", 
    "Study Tracker", 
    "Walk Tracker", 
    "Gym Tracker", 
    "Calorie Tracker"
])

with tab_dashboard:
    st.subheader("Dashboard")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Tasks", 10)
    with col2:
        st.metric("Study Sessions", 5)
    with col3:
        st.metric("Walks", 3)
      
with tab_notes:
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
with tab_time_tracking:
    st.subheader("Time Tracking")
    time_df = pd.DataFrame({
        "Task": ["Task 1", "Task 2", "Task 3"],
        "Time": [5, 3, 2],
    })
    st.write(time_df)
    fig = go.Figure(data=[go.Pie(labels=time_df["Task"], values=time_df["Time"])])
    st.plotly_chart(fig)

with tab_tasks:
    st.subheader("Task Management")
    task_df = pd.DataFrame({
        "Task": ["Task 1", "Task 2", "Task 3"],
        "Priority": ["High", "Medium", "Low"],
        "Due Date": ["2024-03-15", "2024-03-20", "2024-03-25"],
    })
    st.write(task_df)
    with st.form("task_form"):
        task_name = st.text_input("Task Name")
        task_priority = st.selectbox("Priority", ["High", "Medium", "Low"])
        task_due_date = st.date_input("Due Date")
        submit_button = st.form_submit_button("Add Task")
        if submit_button:
            task_df = task_df._append({"Task": task_name, "Priority": task_priority, "Due Date": task_due_date}, ignore_index=True)

with tab_study:
    st.subheader("Study Tracker")
    study_df = pd.DataFrame({
        "Date": ["2024-03-15", "2024-03-16", "2024-03-17"],
        "Study Time": [2, 3, 4],
        "Subject": ["Math", "Science", "History"],
    })
    st.write(study_df)
    with st.form("study_form"):
        study_date = st.date_input("Date")
        study_time = st.number_input("Study Time (hours)")
        study_subject = st.selectbox("Subject", ["Math", "Science", "History"])
        submit_button = st.form_submit_button("Add Study Session")
        if submit_button:
            study_df = study_df._append({"Date": study_date, "Study Time": study_time, "Subject": study_subject}, ignore_index=True)

with tab_walk:
    st.subheader("Walk Tracker")
    walk_df = pd.DataFrame({    "Date": ["2024-03-15", "2024-03-16", "2024-03-17"],
    "Distance": [2, 3, 4],
    "Time": [30, 45, 60],
})

st.write(walk_df)

with st.form("walk_form"):
    walk_date = st.date_input("Date")
    walk_distance = st.number_input("Distance (km)")
    walk_time = st.number_input("Time (minutes)")
    submit_button = st.form_submit_button("Add Walk")
    if submit_button:
        walk_df = walk_df._append({"Date": walk_date, "Distance": walk_distance, "Time": walk_time}, ignore_index=True)

with tab_settings:
    st.subheader("Settings")
    st.write("Coming soon!")

with tab_gym:
    st.subheader("Gym Tracker")
    gym_df = pd.DataFrame({
        "Date": ["2024-03-15", "2024-03-16", "2024-03-17"],
        "Exercise": ["Bench Press", "Squats", "Deadlifts"],
        "Weight": [100, 150, 200],
        "Reps": [8, 10, 12],
    })
    st.write(gym_df)
    with st.form("gym_form"):
        gym_date = st.date_input("Date")
        gym_exercise = st.selectbox("Exercise", ["Bench Press", "Squats", "Deadlifts"])
        gym_weight = st.number_input("Weight (kg)")
        gym_reps = st.number_input("Reps")
        submit_button = st.form_submit_button("Add Gym Session")
        if submit_button:
            gym_df = gym_df._append({"Date": gym_date, "Exercise": gym_exercise, "Weight": gym_weight, "Reps": gym_reps}, ignore_index=True)

with tab_calendar:
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


with tab_calorie:
    st.subheader("Calorie Tracker")
    calorie_df = pd.DataFrame({
        "Date": ["2024-03-15", "2024-03-16", "2024-03-17"],
        "Calories": [2000, 2500, 3000],
    })
    st.write(calorie_df)
    with st.form("calorie_form"):
        calorie_date = st.date_input("Date")
        calorie_intake = st.number_input("Calories")
        submit_button = st.form_submit_button("Add Calorie Intake")
        if submit_button:
            calorie_df = calorie_df._append({"Date": calorie_date, "Calories": calorie_intake}, ignore_index=True)

with tab_collaboration:
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

st.sidebar.caption("Made with love by Shreyash")

