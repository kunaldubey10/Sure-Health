import streamlit as st
import numpy as np
import pickle

# Set page configuration
st.set_page_config(page_title="Sure Health", page_icon="💪🏻")

# Define custom CSS for title styling
custom_css = """
    <style>
        .custom-title {
            font-size: 48px;
            font-weight: bold;
            color: #4CAF50;
            text-align: center;
            margin-top: 20px;
            margin-bottom: 20px;
        }
    </style>
"""

# Inject the custom CSS into the Streamlit app
st.markdown(custom_css, unsafe_allow_html=True)

# Use HTML to apply the custom CSS class
st.markdown('<div class="custom-title">Sure Health 🥗📊</div>', unsafe_allow_html=True)

st.sidebar.success("Select an option.")

# Sidebar
st.sidebar.title("Table of Content")
page = st.sidebar.selectbox("Navigate", ["Home", "Know Your BMI", "Medical History", "Health Insurance", "About"])

# Load the health insurance model
with open('insurance_model.pkl', 'rb') as f:
    model = pickle.load(f)


# Home page
if page == "Home":
    st.markdown("""
    <style>
    .sidebar .sidebar-content {
        background: rgba(255, 255, 255, 0.9);
    }
    </style>
    """, unsafe_allow_html=True)

    # Add a welcome image
    st.markdown(f"""
        <div style="text-align: center;">
            <img src="D:/health insurance/family photo.png" width="500" style="border-radius: 8px;" />
        </div>
    """, unsafe_allow_html=True)
    st.title("Welcome to Sure Health Insurace Comparison!")
    st.write("""
   Welcome to Sure Health Insurace Comparison!🥗📊

   Welcome to our Health Insurance Predictor, your personalized guide to choosing the right health insurance plan. We understand that navigating the complex world of health insurance can be overwhelming, so we’ve created a solution that simplifies the process and provides tailored recommendations based on your unique needs.


   
### Why Choose Us:
- *Personalized Recommendations:* We focus on your individual needs, offering suggestions that align with your health and financial situation.
- *Advanced AI Analysis:* Our cutting-edge AI technology ensures that the recommendations are accurate and based on the latest data trends.
- *User-Friendly Experience:* With a simple and intuitive interface, finding the right health insurance has never been easier.
- *Time-Saving:* No more endless research or confusing comparisons—get a tailored recommendation in just a few clicks.


1.*Fill Out the Form:* Complete the health insurance form with your personal and medical information. This helps our AI analyze your specific needs.
2. *Receive Your Recommendation:* Once you've submitted your details, our system will process the information and provide you with a personalized health insurance plan recommendation.
3. *Review and Decide:* Review the suggested plans and choose the one that best fits your requirements. If needed, you can always modify your input data for a revised recommendation.

Start today and let us help you find the best health insurance plan tailored to your needs!
    """)

elif page == "Know Your BMI":
    age = st.number_input('Enter your age:', min_value=0, max_value=120, value=0)
    height_cm = st.number_input('Enter your height (cm):', min_value=30, max_value=250, value=30)
    weight_kg = st.number_input('Enter your weight (kg):', min_value=30, max_value=300, value=30)
    if st.button('Show Results'):
        def calculate_bmi(height_cm, weight_kg):
            height_m = height_cm / 100
            bmi = weight_kg / (height_m ** 2)
            return bmi

        bmi = calculate_bmi(height_cm, weight_kg)

        st.subheader('Your BMI')
        st.markdown(f'Your BMI is: *{bmi:.2f}*')
    
        if bmi < 18.5:
            st.markdown("<p style='color: aqua;'>You are classified as underweight.</p>", unsafe_allow_html=True)
        elif 18.5 <= bmi < 24.9:
            st.markdown("<p style='color: greenyellow;'>You have a normal weight.</p>", unsafe_allow_html=True)
        elif 25 <= bmi < 29.9:
            st.markdown("<p style='color: darkorange;'>You are classified as overweight.</p>", unsafe_allow_html=True)
        else:
            st.markdown("<p style='color: red;'>You are classified as obese.</p>", unsafe_allow_html=True)


elif page == "Medical History":
    st.title("Medical History and Health Advice")
    st.write("""
    Welcome to the Medical History section. Please provide details about your previous health conditions, 
    and we will offer general advice based on your medical history.
    """)
    st.subheader("Please enter your medical history")
    age = st.number_input("Enter your age", min_value=0, max_value=120, step=1)
    weight = st.number_input("Enter your weight (in kg)", min_value=0.0, max_value=300.0, step=0.1)
    height = st.number_input("Enter your height (in cm)", min_value=0, max_value=250, step=1)
    st.subheader("Previous Medical Conditions")

    conditions = ["None", "Diabetes", "Heart Disease", "Hypertension", "Asthma", "Obesity", "Cancer"]
    medical_condition = st.multiselect("Select any previous or current medical conditions", conditions)
    medications = st.text_input("Are you currently on any medications? If yes, please specify:")

    smoking = st.selectbox("Do you smoke?", ["Yes", "No"])
    alcohol = st.selectbox("Do you consume alcohol?", ["Yes", "No"])

    if st.button("Get Health Advice"):
        st.subheader("Your Medical Summary")
        st.write(f"*Age*: {age}")
        st.write(f"*Weight*: {weight} kg")
        st.write(f"*Height*: {height} cm")
        st.write(f"*Medical Conditions*: {', '.join(medical_condition) if medical_condition else 'None'}")
        st.write(f"*Medications*: {medications if medications else 'None'}")
        st.write(f"*Smoking*: {smoking}")
        st.write(f"*Alcohol Consumption*: {alcohol}")
        
        # Providing advice based on input
        st.subheader("Health Advice")

        if age > 50 and "Heart Disease" in medical_condition:
            st.warning("Since you're above 50 and have a history of heart disease, regular cardiovascular check-ups are important. Consider adopting a low-fat diet and engage in mild physical activity.")
        elif "Diabetes" in medical_condition:
            st.warning("Managing diabetes with proper diet, exercise, and regular blood sugar monitoring is critical. Avoid high-sugar foods and prioritize whole grains and vegetables.")
        elif weight / ((height/100) ** 2) > 30:
            st.warning("Your BMI suggests obesity. It’s important to maintain a balanced diet and engage in regular physical activity to reduce the risk of associated conditions like diabetes and hypertension.")
        elif smoking == "Yes":
            st.warning("Smoking is harmful to your health. Consider quitting to reduce the risk of respiratory diseases, heart disease, and cancer.")
        elif alcohol == "Yes":
            st.warning("Excessive alcohol consumption can lead to liver damage and other health complications. Moderation is key.")
        else:
            st.success("Your medical history appears stable. Continue maintaining a healthy lifestyle with a balanced diet, regular physical activity, and routine check-ups.")

elif page == "Health Insurance":
    st.title("Health Insurance Cost Prediction")

    # Input fields for health insurance prediction
    age = st.number_input('Age:', min_value=0, max_value=120, value=30)
    sex = st.selectbox('Sex:', ['male', 'female'])
    bmi = st.number_input('BMI:', min_value=0.0, max_value=100.0, value=25.0)
    children = st.number_input('Number of children/dependents:', min_value=0, max_value=10, value=0)
    smoker = st.selectbox('Smoker:', ['yes', 'no'])

    # Predict button
    if st.button('Predict Insurance Cost'):
        # Create a feature vector for prediction
        features = np.array([[age, 1 if sex == 'male' else 0, bmi, children, 1 if smoker == 'yes' else 0, 0]])

        # Predict insurance cost
        prediction = model.predict(features)[0]
        
        st.subheader('Predicted Insurance Cost')
        st.write(f'The estimated insurance cost is: ${prediction:.2f}')

elif page == "About":
    st.title("About Us")
    st.write("""
    ### Team
    - **Avinash Verma **: Frontend Developer
    - **Harsh**: Frontend Developer
    - **Kunal**: Backend Developer and Machine Learning Developer 

    ### Mission
    Our mission is to use technology to improve health outcomes and provide people with better policy

    ### Contact
    For any inquiries or feedback, please reach out to us at: kunaldubeyslp@gmail.com
    """)
