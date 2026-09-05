import math
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="For You ❤️",
    page_icon="❤️"
)

def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return (
        11.8 * math.cos(k)
        - 5 * math.cos(2 * k)
        - 2 * math.cos(3 * k)
        - math.cos(4 * k)
    )

x = []
y = []

for i in range(1000):
    k = i * (2 * math.pi / 1000)

    x.append(hearta(k) * 20)
    y.append(heartb(k) * 20)

fig, ax = plt.subplots()
fig.patch.set_facecolor("black")
ax.set_facecolor("black")

ax.plot(x, y)
ax.set_aspect("equal")
ax.axis("off")

st.pyplot(fig)

st.markdown(
    "<h2 style='text-align:center;'>Happy Birthday ❤️</h2>",
    unsafe_allow_html=True
)
