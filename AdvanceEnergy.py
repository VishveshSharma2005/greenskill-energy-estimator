import streamlit as st
import matplotlib.pyplot as plt
import io

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Energy Consumption Calculator",
    page_icon="⚡",
    layout="centered"
)

# ---------- TITLE ----------
st.title("⚡ Energy Consumption Calculator")
st.markdown("Calculate your household energy usage based on your home and daily appliance usage.")

# ---------- FORM ----------
with st.form("energy_calculator"):
    st.subheader("📋 Personal Information")
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("Name", placeholder="Your full name")
        age = st.number_input("Age", min_value=1, max_value=120, value=25)
    
    with col2:
        city = st.text_input("City", placeholder="Your city")
        area = st.text_input("Area", placeholder="Your area/locality")
    
    st.subheader("🏠 Housing Details")
    col3, col4 = st.columns(2)
    
    with col3:
        flat_tenament = st.selectbox("Residence Type", ["Flat", "Tenament"])
    
    with col4:
        facility = st.selectbox("Number of Bedrooms", ["1BHK", "2BHK", "3BHK"])
    
    st.subheader("🔌 Appliances Used")
    col5, col6, col7 = st.columns(3)
    with col5:
        ac = st.checkbox("Air Conditioner")
    with col6:
        fridge = st.checkbox("Refrigerator")
    with col7:
        washing_machine = st.checkbox("Washing Machine")
    
    # Optional Appliance Sliders
    st.subheader("⚙️ Appliance Usage Details")
    
    if ac:
        ac_count = st.slider("No. of ACs", 1, 5, 1)
        ac_hours = st.slider("Hours used per day (AC)", 1, 24, 6)
    else:
        ac_count = ac_hours = 0

    if fridge:
        fridge_count = st.slider("No. of Fridges", 1, 3, 1)
        fridge_hours = 24  # Always ON
    else:
        fridge_count = fridge_hours = 0

    if washing_machine:
        wm_count = st.slider("No. of Washing Machines", 1, 2, 1)
        wm_hours = st.slider("Hours used per day (Washing Machine)", 1, 5, 1)
    else:
        wm_count = wm_hours = 0

    submitted = st.form_submit_button("🔍 Calculate Energy Consumption")

# ---------- CALCULATION ----------
if submitted:
    if not name or not city or not area:
        st.error("Please fill in Name, City, and Area.")
    else:
        base_energy = {"1BHK": 2.4, "2BHK": 3.6, "3BHK": 4.8}.get(facility, 0)
        cal_energy = base_energy

        ac_energy = ac_count * ac_hours * 1.5
        fridge_energy = fridge_count * fridge_hours * 0.125
        wm_energy = wm_count * wm_hours * 0.5

        cal_energy += ac_energy + fridge_energy + wm_energy
        monthly_consumption = cal_energy * 30
        monthly_cost = monthly_consumption * 5  # ₹5/kWh
        carbon_emission = cal_energy * 0.92  # kg CO₂/day

        st.success("✅ Calculation Complete!")

        # ---------- METRICS ----------
        col8, col9, col10 = st.columns(3)
        with col8:
            st.metric("Daily Usage", f"{cal_energy:.2f} kWh")
        with col9:
            st.metric("Monthly Usage", f"{monthly_consumption:.2f} kWh")
        with col10:
            st.metric("Est. Monthly Bill", f"₹{monthly_cost:.0f}")

        st.metric("🌍 Daily CO₂ Emission", f"{carbon_emission:.2f} kg")

        # ---------- CHART ----------
        st.subheader("📊 Daily Usage Breakdown")
        labels = ["Base", "AC", "Fridge", "Washing Machine"]
        values = [base_energy, ac_energy, fridge_energy, wm_energy]
        fig, ax = plt.subplots()
        ax.bar(labels, values, color=["#4CAF50", "#2196F3", "#FFC107", "#FF5722"])
        ax.set_ylabel("kWh")
        ax.set_title("Energy Usage by Appliance")
        st.pyplot(fig)

        # ---------- USER DETAILS ----------
        st.subheader("👤 User Summary")
        st.write(f"**Name:** {name}")
        st.write(f"**Age:** {age}")
        st.write(f"**Location:** {area}, {city}")
        st.write(f"**Residence:** {flat_tenament} ({facility})")

        # ---------- REPORT DOWNLOAD ----------
        st.subheader("📥 Download Report")
        report_text = f"""
        Energy Report for {name}
        -------------------------
        Residence: {facility} in {area}, {city}
        Daily Consumption: {cal_energy:.2f} kWh
        Monthly Consumption: {monthly_consumption:.2f} kWh
        Monthly Cost: ₹{monthly_cost:.0f}
        CO₂ Emission (daily): {carbon_emission:.2f} kg

        Appliance Breakdown:
        - Base Energy: {base_energy} kWh
        - AC: {ac_energy:.2f} kWh
        - Fridge: {fridge_energy:.2f} kWh
        - Washing Machine: {wm_energy:.2f} kWh
        """
        st.download_button("📄 Download TXT", report_text, file_name="energy_report.txt")

        # ---------- TIPS ----------
        st.subheader("💡 Energy Saving Tips")
        tips = []
        if ac and ac_hours > 6:
            tips.append("Reduce AC usage or set temperature to 24°C.")
        if fridge and fridge_count > 1:
            tips.append("Consider using one energy-efficient fridge.")
        if washing_machine and wm_hours > 2:
            tips.append("Use quick wash cycles to reduce washing machine usage.")
        tips += [
            "Use LED bulbs instead of incandescent ones.",
            "Unplug devices when not in use.",
            "Use natural daylight when possible.",
        ]
        for tip in tips:
            st.write(f"• {tip}")

# ---------- FOOTER ----------
st.markdown("---")
st.markdown("*This calculator provides an estimate. Real usage may vary based on device models and habits.*")
