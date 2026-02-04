
import panel as pn

pn.extension()

app = pn.Tabs(
    ("Home", pn.Column(
        "🏠 Home Page",
        pn.widgets.Button(name="Go", button_type="primary")
    )),
    ("Settings", pn.Column(
        "⚙️ Settings",
        pn.widgets.Toggle(name="Dark Mode", button_type="success")
    )),
    ("Profile", pn.Column(
        "👤 Profile",
        pn.widgets.Button(name="Save", button_type="warning")
    )),
)

app.servable()
