from click import prompt
from dotenv import load_dotenv
load_dotenv() ## load all the enviornment variables
import streamlit as st
import os
import _sqlite3
import google.generativeai as genai
## configre our api key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#FUNCTION TO LOAD GOOGLE GEMINI MODEL AND PROVIDE SQL QUERY AS RESPONSE
def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

# function to retreive qyerty from sql database
def read_sql_query(sql, db):
    # Remove Markdown-style code formatting
    clean_sql = sql.strip().replace("```sql", "").replace("```", "")
    
    conn = _sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(clean_sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

## prompt

prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT andd has the following columns - NAME,CLASS,
    SECTION AND MARKS \n\nFor example 1-How many entries of records are present?,
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2- Tell me all the students studying in Data Science class?,
    the SQL command will be something like this SELECT * FROM STUDENT
    where CLASS="Data Science";
    also the sql code should have ``` in beginning or end and sql word in output
    
    """
]

## streamlit app
st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")
question=st.text_input("Input: ",key="input")
submit=st.button("Ask the question")

## if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    data=read_sql_query(response,"student.db")
    st.subheader("The Response is")
    for row in data:
        print(row)
        st.header(row)


