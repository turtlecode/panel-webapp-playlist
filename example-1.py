

#python -m pip install panel psycopg2-binary sqlalchemy pandas matplotlib plotly


import panel as pn

pn.extension()

app = pn.Column(
    "# 👋 Hello Panel!",
    "This is my **first Panel web application**.",
    "Panel allows you to build web apps using **only Python** 🚀"
)

app.servable()
