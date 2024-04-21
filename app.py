import streamlit as st
import streamlit.components.v1 as stc

html_temp= """
            <div style="padding:10px; background-color:#3872fb;border-radius:10px">
                <h1>Employee Promotion Prediction App</h1>
                <h4>This website belongs to HR Team</h4>
            </div>
            """

desc_temp= """
                ### Employee Promotion Prediction App
                This app is used by HR Team to help predict wether
                an employee get a promotion or not

                ### App Content
                - Exploratory Data Analysis
                - Machine Leraning Section
            """
def main ():
    stc.html(html_temp)

    menu = ["Home", "EDA", "ML Section"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        st.markdown(desc_temp, unsafe_allow_html=True)
    elif choice == "EDA":
        #Run EDA:
        print("EDA")
    elif choice == "ML Section":
        #Run ML
        print("ML App")

if __name__ == '__main__':
    main()
    