import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Energy Consumption Calculator",
    page_icon="⚡",
    layout="centered"
)

# Main title
st.title("⚡ Energy Consumption Calculator")
st.markdown("Calculate your household energy consumption based on your living space and appliances.")

# Create a form for better user experience
with st.form("energy_calculator"):
    # Personal Information Section
    st.subheader("📋 Personal Information")
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("Enter your name:", placeholder="Your full name")
        age = st.number_input("Enter your age:", min_value=1, max_value=120, value=25)
    
    with col2:
        city = st.text_input("Enter your city:", placeholder="Your city")
        area = st.text_input("Enter your area name:", placeholder="Your area/locality")
    
    # Housing Information Section
    st.subheader("🏠 Housing Information")
    col3, col4 = st.columns(2)
    
    with col3:
        flat_tenament = st.selectbox(
            "Type of residence:",
            ["Flat", "Tenament"],
            help="Select whether you live in a flat or tenament"
        )
    
    with col4:
        facility = st.selectbox(
            "Number of bedrooms:",
            ["1BHK", "2BHK", "3BHK"],
            help="Select your housing configuration"
        )
    
    # Appliances Section
    st.subheader("🔌 Appliances")
    col5, col6, col7 = st.columns(3)
    
    with col5:
        ac = st.checkbox("Air Conditioner", help="Do you use an AC?")
    
    with col6:
        fridge = st.checkbox("Refrigerator", help="Do you use a fridge?")
    
    with col7:
        washing_machine = st.checkbox("Washing Machine", help="Do you use a washing machine?")
    
    # Submit button
    submitted = st.form_submit_button("Calculate Energy Consumption", type="primary")
    
    if submitted:
        # Validation
        if not name or not city or not area:
            st.error("Please fill in all required fields (Name, City, Area)")
        else:
            # Calculate energy consumption
            cal_energy = 0
            
            # Base energy calculation based on BHK
            if facility == "1BHK":
                cal_energy += 2 * 0.4 + 2 * 0.8  # 2.4 kWh
            elif facility == "2BHK":
                cal_energy += 3 * 0.4 + 3 * 0.8  # 3.6 kWh
            elif facility == "3BHK":
                cal_energy += 4 * 0.4 + 4 * 0.8  # 4.8 kWh
            
            # Add appliance energy consumption
            if ac:
                cal_energy += 3
            if fridge:
                cal_energy += 3
            if washing_machine:
                cal_energy += 3
            
            # Display results
            st.success("✅ Calculation Complete!")
            
            # Results section
            st.subheader("📊 Results")
            
            # Create metrics display
            col8, col9, col10 = st.columns(3)
            
            with col8:
                st.metric(
                    label="Daily Energy Consumption",
                    value=f"{cal_energy:.1f} kWh",
                    help="Total daily energy consumption"
                )
            
            with col9:
                monthly_consumption = cal_energy * 30
                st.metric(
                    label="Monthly Consumption",
                    value=f"{monthly_consumption:.1f} kWh",
                    help="Estimated monthly energy consumption"
                )
            
            with col10:
                # Assuming average rate of ₹5 per kWh
                monthly_cost = monthly_consumption * 5
                st.metric(
                    label="Estimated Monthly Cost",
                    value=f"₹{monthly_cost:.0f}",
                    help="Estimated monthly electricity cost"
                )
            
            # Detailed breakdown
            st.subheader("📋 Detailed Breakdown")
            
            # Create breakdown data
            breakdown_data = []
            base_energy = 0
            
            if facility == "1BHK":
                base_energy = 2.4
            elif facility == "2BHK":
                base_energy = 3.6
            elif facility == "3BHK":
                base_energy = 4.8
            
            breakdown_data.append(f"• Base consumption ({facility}): {base_energy} kWh")
            
            if ac:
                breakdown_data.append("• Air Conditioner: 3.0 kWh")
            if fridge:
                breakdown_data.append("• Refrigerator: 3.0 kWh")
            if washing_machine:
                breakdown_data.append("• Washing Machine: 3.0 kWh")
            
            for item in breakdown_data:
                st.write(item)
            
            # User information summary
            st.subheader("👤 User Information")
            st.write(f"**Name:** {name}")
            st.write(f"**Age:** {age} years")
            st.write(f"**Location:** {area}, {city}")
            st.write(f"**Residence:** {flat_tenament} ({facility})")
            
            # Energy efficiency tips
            st.subheader("💡 Energy Saving Tips")
            tips = [
                "Use LED bulbs instead of incandescent bulbs",
                "Set AC temperature to 24°C or higher",
                "Unplug appliances when not in use",
                "Use natural light during the day",
                "Regular maintenance of appliances improves efficiency"
            ]
            
            for tip in tips:
                st.write(f"• {tip}")

# Footer
st.markdown("---")
st.markdown("*This calculator provides estimates based on average consumption patterns. Actual consumption may vary.*")