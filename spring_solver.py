import streamlit as st
import math

st.set_page_config(page_title="Spring Stretch Solver", page_icon="https://imgur.com/a/6tWJySg", layout="centered")

st.markdown(
    "<h1 style='text-align: center;'>Spring Stretch Solver</h1>",
    unsafe_allow_html=True
)
st.markdown("<div style='text-align: center;'>Calculates the stretch distance 'x' of a spring using this equation:</div>",
    unsafe_allow_html=True
)
st.latex(r"x = \sqrt{\frac{m \left[\frac{\Delta d \cdot g}{2 \sin(\theta)\cos(\theta)}\right]}{k}}")

st.divider()

col1, col2 = st.columns(2)

with col1:
    m = st.number_input(
        "Mass — m (kg)",
        min_value=0.0,
        value=1.0,
        step=0.1,
        format="%.4f",
        help="Mass of the object in kilograms"
    )
    delta_d = st.number_input(
        "Displacement — Δd (m)",
        min_value=0.0,
        value=1.0,
        step=0.01,
        format="%.4f",
        help="Displacement value in metres"
    )
    g = st.number_input(
        "Gravitational acceleration — g (m/s²)",
        min_value=0.0,
        value=9.81,
        step=0.01,
        format="%.4f",
        help="Typically 9.81 m/s² on Earth"
    )

with col2:
    theta_deg = st.number_input(
        "Angle — θ (degrees)",
        min_value=0.1,
        max_value=89.9,
        value=45.0,
        step=0.1,
        format="%.2f",
        help="Angle in degrees (must not be 0° or 90°)"
    )
    k = st.number_input(
        "Spring constant — k (N/m)",
        min_value=0.001,
        value=10.0,
        step=0.1,
        format="%.4f",
        help="Spring constant in Newtons per metre"
    )

st.divider()

# Calculation
theta_rad = math.radians(theta_deg)
sin_theta = math.sin(theta_rad)
cos_theta = math.cos(theta_rad)
denominator_trig = 2 * sin_theta * cos_theta  # = sin(2θ)

if denominator_trig == 0:
    st.error("⚠️ sin(2θ) = 0 at this angle — division by zero. Try a different angle.")
else:
    bracket = (delta_d * g) / denominator_trig
    inside_sqrt = (m * bracket) / k

    if inside_sqrt < 0:
        st.error("⚠️ The value inside the square root is negative. Check your inputs.")
    else:
        x = math.sqrt(inside_sqrt)

        # Result
st.markdown(f"<h2 style='text-align: center;'>Stretch the spring to a lenth of x = {x:.6f}m</h2>", unsafe_allow_html=True)

        # Step-by-step breakdown
with st.expander("Calculation Breakdown"):
        st.markdown(f"**Step 1 — Trig functions:**")
        st.markdown(f"- sin({theta_deg}°) = `{sin_theta:.6f}`")
        st.markdown(f"- cos({theta_deg}°) = `{cos_theta:.6f}`")

        st.markdown(f"**Step 2 — Multiply inside brackets:**")
        st.markdown(f"- 2 × sin(θ) × cos(θ) = `{denominator_trig:.6f}`")
        st.markdown(f"- Δd × g = {delta_d} × {g} = `{delta_d * g:.6f}`")

        st.markdown(f"**Step 3 — Divide (resolve bracket):**")
        st.markdown(f"- Δd·g / (2·sin·cos) = `{bracket:.6f}`")

        st.markdown(f"**Step 4 — Multiply by m, divide by k:**")
        st.markdown(f"- m × bracket / k = {m} × {bracket:.6f} / {k} = `{inside_sqrt:.6f}`")

        st.markdown(f"**Step 5 — Square root:**")
        st.markdown(f"- x = √{inside_sqrt:.6f} = **`{x:.6f} m`**")
