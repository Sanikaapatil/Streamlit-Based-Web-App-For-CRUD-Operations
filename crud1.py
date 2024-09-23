import mysql.connector
import streamlit as st

# Establish a connection to MySQL Server

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="momopanda",
    database="crud_new1"


)
mycursor=mydb.cursor()
print("Connection Established")

# Create Streamlit App

def main():
    st.title("CRUD Operations With MySQL");

    # Display Options for CRUD Operations
    option=st.sidebar.selectbox("Select an Operation",("Create","Read","Update","Delete"))
    # Perform Selected CRUD Operations
    if option=="Create":
        st.subheader("Create a Record")
        name=st.text_input("Enter Name")
        amount = st.number_input("Enter Amount")
        status = st.text_input("Enter Status")
        mobilenumber = st.text_input("Enter Mobilenumber")
        email=st.text_input("Enter Email")
        if st.button("Create"):
            sql= "insert into users(name,amount,status,mobilenumber,email) values(%s,%s,%s,%s,%s)"
            val= (name,amount,status,mobilenumber,email)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Record Created Successfully!!!")



    elif option=="Read":
        st.subheader("Read Records")
        mycursor.execute("select * from users")
        result = mycursor.fetchall()
        for row in result:
            st.write(row)



    elif option=="Update":
        st.subheader("Update a Record")
        id=st.number_input("Enter ID",min_value=1)
        name=st.text_input("Enter New Name")
        amount=st.number_input("Enter New Amount")
        status= st.text_input("Enter New Status")
        mobilenumber = st.text_input("Enter New Mobilenumber")
        email = st.text_input("Enter New Email")

        if st.button("Update"):
            sql="update users set name=%s, amount=%s, status=%s, mobilenumber=%s, email=%s where id =%s"
            val=(name,amount,status,mobilenumber,email,id)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Record Updated Successfully!!!")




    elif option=="Delete":
        st.subheader("Delete a Record")
        id=st.number_input("Enter ID",min_value=1)
        if st.button("Delete"):
            sql="delete from users where id =%s"
            val=(id,)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Record Deleted Successfully!!!")


if __name__ == "__main__":
    main()








