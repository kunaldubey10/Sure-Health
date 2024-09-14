import streamlit as st

st.set_page_config(page_title="Sure Health" , page_icon="💪🏻")
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
st.markdown('<div class="custom-title">Welcome to NutriTrack! 🥗📊</div>', unsafe_allow_html=True)

st.sidebar.success("Select an option.")

# Sidebar
st.sidebar.title("Table of Content")
page = st.sidebar.selectbox("Navigate",["Home", "Quick Look", "Deficient", "Excess", "About"])

# Nutritional deficiencies and their details
deficiencies = {
    "Iron": {
        "description": "Essential for the production of hemoglobin. Deficiency can lead to anemia.",
        "symptoms": ["Fatigue", "Weakness", "Paleness", "Shortness of breath", "Dizziness"],
        "cure_foods": ["Red meat", "Beans", "Lentils", "Spinach"]
    },
    "Vitamin D": {
        "description": "Important for bone health and immune function. Deficiency can cause bone pain and weakness.",
        "symptoms": ["Bone pain", "Muscle weakness", "Fatigue", "Depression"],
        "cure_foods": ["Fatty fish", "Fortified dairy products", "Egg yolks"]
    },
    "Vitamin B12": {
        "description": "Necessary for nerve function and red blood cell production. Deficiency can lead to fatigue and neurological issues.",
        "symptoms": ["Fatigue", "Weakness", "Numbness", "Tingling", "Difficulty walking"],
        "cure_foods": ["Meat", "Dairy products", "Eggs", "Fortified cereals"]
    },
    "Calcium": {
        "description": "Crucial for maintaining strong bones and teeth. Deficiency can lead to osteoporosis.",
        "symptoms": ["Bone pain", "Muscle cramps", "Numbness", "Tingling"],
        "cure_foods": ["Dairy products", "Leafy green vegetables", "Fortified plant-based milks"]
    },
    "Vitamin C": {
        "description": "Important for immune function and skin health. Deficiency can cause scurvy and poor wound healing.",
        "symptoms": ["Bleeding gums", "Skin rashes", "Fatigue", "Joint pain"],
        "cure_foods": ["Citrus fruits", "Strawberries", "Bell peppers", "Broccoli"]
    },
    "Vitamin A": {
        "description": "Important for vision, immune function, and skin health. Deficiency can lead to night blindness and immune deficiencies.",
        "symptoms": ["Night blindness", "Dry skin", "Frequent infections"],
        "cure_foods": ["Carrots", "Sweet potatoes", "Spinach", "Kale"]
    },
    "Vitamin E": {
        "description": "Acts as an antioxidant and helps protect cells from damage. Deficiency can cause nerve and muscle damage.",
        "symptoms": ["Muscle weakness", "Vision problems", "Immune system problems"],
        "cure_foods": ["Nuts", "Seeds", "Spinach", "Broccoli"]
    },
    "Vitamin K": {
        "description": "Necessary for blood clotting and bone health. Deficiency can lead to excessive bleeding and weakened bones.",
        "symptoms": ["Easy bruising", "Excessive bleeding", "Bone fractures"],
        "cure_foods": ["Leafy green vegetables", "Broccoli", "Brussels sprouts", "Green peas"]
    },
    "Folate (Vitamin B9)": {
        "description": "Essential for DNA synthesis and repair. Deficiency can cause anemia and birth defects.",
        "symptoms": ["Fatigue", "Weakness", "Headaches", "Irritability"],
        "cure_foods": ["Leafy green vegetables", "Legumes", "Fortified cereals", "Citrus fruits"]
    },
    "Magnesium": {
        "description": "Important for muscle and nerve function, as well as bone health. Deficiency can cause muscle cramps and fatigue.",
        "symptoms": ["Muscle cramps", "Fatigue", "Nausea", "Loss of appetite"],
        "cure_foods": ["Nuts", "Seeds", "Whole grains", "Leafy green vegetables"]
    },
    "Zinc": {
        "description": "Vital for immune function and wound healing. Deficiency can lead to hair loss and impaired immunity.",
        "symptoms": ["Hair loss", "Delayed wound healing", "Loss of appetite", "Impaired taste"],
        "cure_foods": ["Meat", "Shellfish", "Legumes", "Seeds"]
    },
    "Copper": {
        "description": "Helps with iron absorption and the formation of red blood cells. Deficiency can cause anemia and bone abnormalities.",
        "symptoms": ["Anemia", "Fatigue", "Weak bones", "Cold intolerance"],
        "cure_foods": ["Shellfish", "Nuts", "Seeds", "Whole grains"]
    },
    "Selenium": {
        "description": "An antioxidant that helps protect cells from damage. Deficiency can cause heart disease and immune system dysfunction.",
        "symptoms": ["Fatigue", "Weakness", "Hair loss", "Heart problems"],
        "cure_foods": ["Brazil nuts", "Seafood", "Meat", "Whole grains"]
    },
    "Potassium": {
        "description": "Helps maintain fluid balance and proper muscle and nerve function. Deficiency can cause weakness and irregular heartbeat.",
        "symptoms": ["Muscle weakness", "Fatigue", "Irregular heartbeat", "Leg cramps"],
        "cure_foods": ["Bananas", "Potatoes", "Spinach", "Avocados"]
    },
    "Iodine": {
        "description": "Essential for thyroid function. Deficiency can lead to goiter and hypothyroidism.",
        "symptoms": ["Goiter", "Fatigue", "Weight gain", "Cold intolerance"],
        "cure_foods": ["Iodized salt", "Seafood", "Dairy products", "Eggs"]
    },
    "Chromium": {
        "description": "Enhances insulin action and glucose metabolism. Deficiency can lead to insulin resistance and weight gain.",
        "symptoms": ["Weight gain", "Insulin resistance", "High blood sugar"],
        "cure_foods": ["Meat", "Whole grains", "Nuts", "Broccoli"]
    },
    "Omega-3 Fatty Acids": {
        "description": "Important for heart health and brain function. Deficiency can lead to dry skin and mood disorders.",
        "symptoms": ["Dry skin", "Fatigue", "Mood swings", "Depression"],
        "cure_foods": ["Fatty fish", "Flaxseeds", "Chia seeds", "Walnuts"]
    },
    "Manganese": {
        "description": "Involved in bone formation and metabolism. Deficiency can lead to bone deformities and poor growth.",
        "symptoms": ["Bone deformities", "Poor growth", "Skin rashes"],
        "cure_foods": ["Whole grains", "Nuts", "Leafy green vegetables", "Tea"]
    },
    "Choline": {
        "description": "Important for liver function and brain development. Deficiency can cause liver damage and cognitive issues.",
        "symptoms": ["Liver damage", "Memory issues", "Fatigue"],
        "cure_foods": ["Eggs", "Meat", "Fish", "Brussels sprouts"]
    },
    "Vitamin B6": {
        "description": "Important for protein metabolism and cognitive function. Deficiency can cause anemia and neurological issues.",
        "symptoms": ["Anemia", "Depression", "Confusion", "Irritability"],
        "cure_foods": ["Poultry", "Fish", "Bananas", "Potatoes"]
    },
    "Vitamin B3 (Niacin)": {
        "description": "Aids in energy production and DNA repair. Deficiency can cause pellagra, characterized by dermatitis, diarrhea, and dementia.",
        "symptoms": ["Dermatitis", "Diarrhea", "Dementia"],
        "cure_foods": ["Poultry", "Fish", "Whole grains", "Legumes"]
    },
    "Vitamin B5 (Pantothenic Acid)": {
        "description": "Essential for the synthesis of coenzyme A, which is involved in energy metabolism. Deficiency can cause fatigue and digestive issues.",
        "symptoms": ["Fatigue", "Digestive issues", "Irritability"],
        "cure_foods": ["Eggs", "Avocados", "Whole grains", "Legumes"]
    }
}

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
    if app_mode == "Home":
    logo_path = "D:\family photo.png"
    logo_base64 = get_image_as_base64(logo_path)
    st.markdown(f"""
        <div style="text-align: center;">
            <img src="{image_url}" width="500" style="border-radius: 8px;" />
        </div>
    """, unsafe_allow_html=True)
    st.title("Welcome to our Nutrition and Macros Tracker!")
    st.write("""
    Welcome to our Nutrition Tracker System! 🥗📊

    Our mission is to help you monitor and improve your nutritional intake efficiently. Input your daily food consumption, and our system will analyze it to track nutritional deficiencies and provide personalized recommendations. Let's work together to achieve a balanced and healthier diet!

    ### How It Works
    1. **Input Your Diet:** Go to the **Track Nutrition** page and enter your daily food intake.
    2. **Analysis:** Our system will process your input using advanced algorithms to identify any nutritional deficiencies and assess your overall diet.
    3. **Results:** View detailed results and receive tailored recommendations to enhance your nutritional balance.

    ### Why Choose Us?
    - **Precision:** Our system employs advanced data analysis techniques for accurate nutrition tracking.
    - **User-Friendly:** Intuitive and straightforward interface for a seamless experience.
    - **Fast and Effective:** Get actionable insights and recommendations quickly to make informed dietary choices.

    ### Get Started
    Click on the **Track Nutrition** page in the sidebar to input your daily diet and discover how our Nutrition Tracker System can help you achieve a healthier lifestyle!

    ### About Us
    Learn more about our project, meet our team, and understand our mission on the **About** page.

    """)

elif page == "Quick Look":
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
        st.markdown(f'Your BMI is: **{bmi:.2f}**')
    
        if bmi < 18.5:
            st.markdown("<p style='color: aqua;'>You are classified as underweight.</p>", unsafe_allow_html=True)
        elif 18.5 <= bmi < 24.9:
            st.markdown("<p style='color: greenyellow;'>You have a normal weight.</p>", unsafe_allow_html=True)
        elif 25 <= bmi < 29.9:
            st.markdown("<p style='color: darkorange;'>You are classified as overweight.</p>", unsafe_allow_html=True)
        else:
            st.markdown("<p style='color: red;'>You are classified as obese.</p>", unsafe_allow_html=True)

# deficient page
elif page == "Deficient":
    st.title("Common Nutritional Deficiencies")

    # Search box for deficiencies page
    search_term_def = st.text_input("Search for a deficiency:")

    # Filter deficiencies based on the search term
    filtered_deficiencies = {k: v for k, v in deficiencies.items() if search_term_def.lower() in k.lower()}

    if filtered_deficiencies:
        for nutrient, details in filtered_deficiencies.items():
            st.subheader(nutrient)
            st.write("### Description")
            st.write(details["description"])
            st.write("### Symptoms")
            for symptom in details["symptoms"]:
                st.write(f"- {symptom}")
            st.write("### Foods rich in this nutrient:")
            for food in details["cure_foods"]:
                st.write(f"- {food}")
    else:
        st.write("No results found. Try searching for a different term.")

# Excess page
elif page == "Excess":
    st.title("Foods Rich in Essential Nutrients")

    # Nutrient-rich foods
    rich_foods = {
        "Iron": ["Red meat", "Beans", "Lentils", "Spinach"],
        "Vitamin D": ["Fatty fish", "Fortified dairy products", "Egg yolks"],
        "Vitamin B12": ["Meat", "Dairy products", "Eggs", "Fortified cereals"],
        "Calcium": ["Dairy products", "Leafy green vegetables", "Fortified plant-based milks"],
        "Vitamin C": ["Citrus fruits", "Strawberries", "Bell peppers", "Broccoli"],
        "Vitamin A": ["Carrots", "Sweet potatoes", "Spinach", "Kale"],
        "Vitamin E": ["Nuts", "Seeds", "Spinach", "Broccoli"],
        "Vitamin K": ["Leafy green vegetables", "Broccoli", "Brussels sprouts", "Green peas"],
        "Folate (Vitamin B9)": ["Leafy green vegetables", "Legumes", "Fortified cereals", "Citrus fruits"],
        "Magnesium": ["Nuts", "Seeds", "Whole grains", "Leafy green vegetables"],
        "Zinc": ["Meat", "Shellfish", "Legumes", "Seeds"],
        "Copper": ["Shellfish", "Nuts", "Seeds", "Whole grains"],
        "Selenium": ["Brazil nuts", "Seafood", "Meat", "Whole grains"],
        "Potassium": ["Bananas", "Potatoes", "Spinach", "Avocados"],
        "Iodine": ["Iodized salt", "Seafood", "Dairy products", "Eggs"],
        "Chromium": ["Meat", "Whole grains", "Nuts", "Broccoli"],
        "Omega-3 Fatty Acids": ["Fatty fish", "Flaxseeds", "Chia seeds", "Walnuts"],
        "Manganese": ["Whole grains", "Nuts", "Leafy green vegetables", "Tea"],
        "Choline": ["Eggs", "Meat", "Fish", "Brussels sprouts"],
        "Vitamin B6": ["Poultry", "Fish", "Bananas", "Potatoes"],
        "Vitamin B3 (Niacin)": ["Poultry", "Fish", "Whole grains", "Legumes"],
        "Vitamin B5 (Pantothenic Acid)": ["Eggs", "Avocados", "Whole grains", "Legumes"]
    }

    # Search box for rich foods page
    search_term_rich = st.text_input("Search for Rich Foods:")

    # Filter foods based on the search term
    filtered_rich_foods = {k: v for k, v in rich_foods.items() if search_term_rich.lower() in k.lower()}

    if filtered_rich_foods:
        for nutrient, foods in filtered_rich_foods.items():
            st.subheader(f"Foods rich in {nutrient}")
            for food in foods:
                st.write(f"- {food}")
    else:
        st.write("No results found. Try searching for a different term.")

# About page
elif page == "About":
    st.title("About This App")
    st.write("""
    This app is designed to raise awareness about nutrition deficiencies and help users make informed dietary choices. 
    Nutrition is a critical aspect of maintaining overall health, and understanding common deficiencies can help individuals 
    take steps to address their nutritional needs. If you have specific dietary concerns, please consult with a healthcare provider.
    """)

# Run the app
if __name__ == "__main__":
    st.write("*Use the sidebar to navigate through our website.")
