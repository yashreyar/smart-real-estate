import streamlit as st
import numpy as np
import pickle
from PIL import Image
import os

st.set_page_config(page_title="Property Valuation Tool", layout="wide")

st.markdown("### 🏡 Real Estate Valuation Tool")
st.write("Calculates property appraisals based on area, micro-market benchmarks, and structural specifications.")
st.write("---")

@st.cache_resource
def load_saved_artifacts():
    pipeline_path = "../models/sklearn_pipeline.pkl" if os.path.exists("../models") else "models/sklearn_pipeline.pkl"
    if os.path.exists(pipeline_path):
        with open(pipeline_path, "rb") as f:
            return pickle.load(f)
    return None

pipeline = load_saved_artifacts()

# ROW 1: Core Inputs (Full Width Grid)
r1_col1, r1_col2 = st.columns(2, gap="large")
with r1_col1:
    sqft = st.number_input("Super Built-up Area (Sq.Ft.)", min_value=300, max_value=12000, value=1500, step=100)
with r1_col2:
    zipcode = st.selectbox("Location (Pincode)", [
        "121002 (Faridabad - Standard Sectors)", 
        "121004 (Faridabad - Green Fields)", 
        "122011 (Gurugram - Golf Course Road)",
        "122002 (Gurugram - Dwarka Expressway)",
        "201301 (Noida - Central)",
        "110001 (Delhi - Connaught Place)",
        "110016 (Delhi - Hauz Khas)",
        "400001 (Mumbai - South Mumbai)",
        "400053 (Mumbai - Andheri West)",
        "560066 (Bengaluru - Whitefield)"
    ])

st.write("") 

# ROW 2: Specifications and Image Side-by-Side (Equal height alignment)
r2_col1, r2_col2 = st.columns(2, gap="large")

with r2_col1:
    st.markdown("**Property Specifications:**")
    
    # Nested grid to save vertical space
    spec_col1, spec_col2 = st.columns(2)
    with spec_col1:
        bedrooms = st.slider("Bedrooms", 1, 6, 3)
        halls = st.slider("Halls / Living Rooms", 1, 3, 1)
        baths = st.slider("Bathrooms", 1, 5, 2)
    with spec_col2:
        other_rooms = st.slider("Other Rooms (Study/Puja)", 0, 3, 0)
        prop_age = st.slider("Property Age (Years)", 0, 25, 2)
        parking = st.selectbox("Parking Spaces", [0, 1, 2])
        
    furnishing = st.radio("Furnishing", ["Unfurnished", "Semi-Furnished", "Fully Furnished"], horizontal=True)
    floor_type = st.selectbox("Floor Level", ["Low Rise (1-4)", "Mid Rise (5-12)", "High Rise (13+)"])

with r2_col2:
    st.markdown("**Property Image:**")
    uploaded_file = st.file_uploader("Upload Facade Photo", type=["jpg", "jpeg", "png"], label_visibility="collapsed")
    if uploaded_file is not None:
        st.image(uploaded_file, width="stretch")

st.write("---")

# Parsing & Calculation Logic
clean_pincode = zipcode.split()[0]
price_mapping = {
    "121002": 5800.0, "121004": 7500.0, "122011": 21000.0, "122002": 13500.0, 
    "201301": 11000.0, "110001": 38000.0, "110016": 24000.0, "400001": 55000.0, 
    "400053": 31000.0, "560066": 12800.0
}
avg_zipcode_price_per_sqft = price_mapping.get(clean_pincode, 7000.0)

if st.button("Calculate Valuation", type="primary", use_container_width=True):
    if uploaded_file is not None:
        base_valuation = sqft * avg_zipcode_price_per_sqft
        
        img = Image.open(uploaded_file).convert("RGB").resize((224, 224))
        visual_premium = np.mean(np.array(img) / 255.0) * 0.12 
        
        room_multiplier = (bedrooms * 0.04) + (halls * 0.02) + (other_rooms * 0.01)
        furnish_multiplier = 0.0 if furnishing == "Unfurnished" else (0.08 if furnishing == "Semi-Furnished" else 0.18)
        floor_multiplier = 0.0 if "Low" in floor_type else (0.04 if "Mid" in floor_type else 0.10)
        parking_multiplier = 0.04 * parking
        age_depreciation = max(-0.30, -(prop_age * 0.015))
        
        total_multipliers = 1.0 + visual_premium + room_multiplier + (baths * 0.02) + furnish_multiplier + floor_multiplier + parking_multiplier + age_depreciation
        appraisal_value = base_valuation * total_multipliers
        
        def format_inr(num):
            if num >= 10000000: return f"₹{num / 10000000:.2f} Crore"
            if num >= 100000: return f"₹{num / 100000:.2f} Lakh"
            return f"₹{num:,.2f}"
            
        st.markdown(f"#### Appraised Market Value: **{format_inr(appraisal_value)}**")
        
        st.write("")
        m1, m2, m3 = st.columns(3)
        m1.metric("Base Rate", f"₹{avg_zipcode_price_per_sqft:,.0f}/sqft")
        m2.metric("Floor & Room Premium", f"+{(room_multiplier + floor_multiplier)*100:.1f}%")
        m3.metric("Depreciation Factor", f"{age_depreciation*100:.1f}%")
    else:
        st.error("Please upload a property photo to compute valuation coefficients.")