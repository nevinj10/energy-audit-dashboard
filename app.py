import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Energy Audit Dashboard", layout="wide")

st.title("⚡ Energy Audit Dashboard")

# Sidebar Navigation
st.sidebar.title("Energy Audit Sections")

section = st.sidebar.radio(
    "",
    ["🏫 College Energy Audit", "🏭 Industry Energy Audit"]
)

# =====================================================
# COLLEGE ENERGY AUDIT
# =====================================================

if section == "🏫 College Energy Audit":

    st.header("🏫 Jyothi Engineering College Energy Audit")

    col1,col2,col3,col4 = st.columns(4)

    col1.metric("Monthly Electricity Consumption","24,988 kWh")
    col2.metric("Solar Generation","11,691 kWh")
    col3.metric("Power Factor","0.96")
    col4.metric("Contract Demand","160 kVA")

    st.write("""
This section presents the electricity consumption and energy performance of Jyothi Engineering College.
Electricity is supplied from KSEB at 11 kV and distributed through a 400 kVA transformer.
The campus also operates rooftop solar PV systems to reduce grid electricity consumption.
""")

    st.divider()

    # Monthly Energy Consumption
    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    energy = [23000,24000,24988,25500,24500,23500,25000,25200,24800,24300,23800,24988]

    energy_df = pd.DataFrame({
        "Month":months,
        "Energy (kWh)":energy
    })

    # Electricity Distribution
    labels = [
        "Eastern Academic Block",
        "Western Academic Block",
        "Admin Block",
        "Pump & Substation",
        "Hostels & Other Loads"
    ]

    distribution = [13.8,14.1,13.7,18.1,40.4]

    dist_df = pd.DataFrame({
        "Section":labels,
        "Share":distribution
    })

    col1,col2 = st.columns(2)

    with col1:
        fig = px.line(
            energy_df,
            x="Month",
            y="Energy (kWh)",
            title="Monthly Electricity Consumption",
            markers=True,
            height=300
        )
        st.plotly_chart(fig, use_container_width=True)

        st.write("""
**Explanation:**  
The average monthly electricity consumption of the college is approximately **24,988 kWh**.
""")

    with col2:
        fig = px.pie(
            dist_df,
            names="Section",
            values="Share",
            title="Electricity Consumption Distribution",
            height=300
        )
        st.plotly_chart(fig, use_container_width=True)

        st.write("""
**Explanation:**  
Hostels and auxiliary loads consume the highest share (**40.4%**) of electricity.
""")

    st.divider()

    # Solar Performance
    solar_df = pd.DataFrame({
        "System":["80 kW Solar","60 kW Solar"],
        "Generation":[3.58,2.72]
    })

    # Energy Saving Measures
    saving_df = pd.DataFrame({
        "Measure":[
            "LED Replacement",
            "BLDC Fans",
            "Efficient Pumps",
            "Inverter AC"
        ],
        "Savings":[10685,26880,14038,4347]
    })

    col3,col4 = st.columns(2)

    with col3:
        fig = px.bar(
            solar_df,
            x="System",
            y="Generation",
            title="Solar PV Performance",
            height=300
        )
        st.plotly_chart(fig, use_container_width=True)

        st.write("""
**Explanation:**  
The 80 kW solar PV system produces **3.58 kWh/kWp/day**, which is higher than the 60 kW system.
""")

    with col4:
        fig = px.bar(
            saving_df,
            x="Measure",
            y="Savings",
            title="Energy Saving Measures",
            height=300
        )
        st.plotly_chart(fig, use_container_width=True)

        st.write("""
**Explanation:**  
Energy conservation measures can reduce electricity consumption by approximately **55,950 kWh/year**.
""")

    st.divider()

    st.subheader("🔎 Findings")

    st.write("""
• Average monthly electricity consumption: **24,988 kWh**  
• Solar generation: **11,691 kWh/month**  
• Maximum demand recorded: **157 kVA**  
• Contract demand: **160 kVA**  
• Average power factor: **0.96 lagging**
""")

    st.subheader("💡 Recommendations")

    st.write("""
• Install **50 kVAr Automatic Power Factor Correction (APFC) panel**  
• Replace fluorescent lamps with **LED lighting systems**  
• Replace ceiling fans with **BLDC fans**  
• Replace old pump sets with **energy efficient pumps**  
• Replace old AC units with **inverter AC systems**
""")

# =====================================================
# INDUSTRY ENERGY AUDIT
# =====================================================

elif section == "🏭 Industry Energy Audit":

    st.header("🏭 Industry Energy Audit")

    col1,col2,col3,col4 = st.columns(4)

    col1.metric("Contract Demand","60 kVA")
    col2.metric("Maximum Demand","55.33 kVA")
    col3.metric("Power Factor","1.0")
    col4.metric("Monthly Consumption","8,362 kWh")

    st.write("""
This section presents the energy performance of the audited industrial facility.
The system operates with stable electrical loading and efficient power factor management.
""")

    st.divider()

    months = ["Nov","Dec","Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct"]
    demand = [52.9,51.3,48.1,45.0,44.2,52.5,50.0,55.3,46.9,47.3,51.5,51.9]

    demand_df = pd.DataFrame({
        "Month":months,
        "Demand":demand
    })

    tariff_df = pd.DataFrame({
        "Component":["Energy Charges","Demand Charges","Other"],
        "Share":[68,28,4]
    })

    col1,col2 = st.columns(2)

    with col1:
        fig = px.line(
            demand_df,
            x="Month",
            y="Demand",
            title="Demand Analysis",
            markers=True,
            height=300
        )

        fig.add_hline(y=60, line_dash="dash", line_color="red")

        st.plotly_chart(fig, use_container_width=True)

        st.write("""
**Explanation:**  
The maximum demand recorded was **55.33 kVA**, which is below the contract demand of **60 kVA**.
""")

    with col2:
        fig = px.pie(
            tariff_df,
            names="Component",
            values="Share",
            title="Electricity Cost Distribution",
            height=300
        )

        st.plotly_chart(fig, use_container_width=True)

        st.write("""
**Explanation:**  
Energy charges contribute **68% of the electricity bill**, followed by demand charges.
""")

    st.divider()

    solar_df = pd.DataFrame({
        "Parameter":["Energy Saving","Financial Saving"],
        "Value":[72000,648000]
    })

    fig = px.bar(
        solar_df,
        x="Parameter",
        y="Value",
        title="Solar PV Installation Benefits",
        height=300
    )

    st.plotly_chart(fig, use_container_width=True)

    st.write("""
Installing a **40 kW rooftop solar PV system** can save approximately **72,000 kWh per year**
and reduce electricity costs by **₹6,48,000 annually**.
""")

    st.divider()

    st.subheader("🔎 Findings")

    st.write("""
• Maximum demand recorded: **55.33 kVA**  
• Contract demand: **60 kVA**  
• Average power factor maintained at **unity (1.0)**  
• Average monthly electricity consumption: **8,362 kWh**
""")

    st.subheader("💡 Recommendations")

    st.write("""
• Maintain **APFC panel in automatic mode**  
• Monitor **maximum demand continuously**  
• Maintain **phase load balancing**  
• Monitor **harmonics due to non-linear loads**  
• Install **40 kW rooftop solar PV system**
""")
