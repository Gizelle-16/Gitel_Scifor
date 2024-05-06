import streamlit as st
import Diet_Recommendation
import Custom_Recommendation


    
st.set_page_config(
    page_title="Home",
)

def run_home_app():
    st.write("Welcome to the Diet Recommendation System")
    st.sidebar.success("Select what you want.")
    st.markdown(
        """
        A diet recommendation web application using content-based approach with Scikit-Learn and Streamlit.
        This app will help you choose recipes based on your age, weight, height and level of exercise.
        """
    )

    app_mode = st.sidebar.selectbox(
        "Choose the app mode",
        ["Home", "Custom Recommendation", "Diet Recommendation"]
    )

    if app_mode == "Custom Recommendation":
        Custom_Recommendation.app_mode_custom()
        
    elif app_mode == "Diet Recommendation":
        Diet_Recommendation.app_mode_recc()

        

if __name__ == "__main__":
    run_home_app()