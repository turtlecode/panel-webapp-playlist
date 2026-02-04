
import panel as pn

pn.extension()

app = pn.Column(
    "Column Layout",
    pn.widgets.Button(name="A", button_type="primary"),
    pn.widgets.Button(name="B", button_type="success"),
    pn.widgets.Button(name="C", button_type="warning"),
)


'''
app = pn.Row(
    "Row Layout",
    pn.widgets.Button(name="A", button_type="primary"),
    pn.widgets.Button(name="B", button_type="success"),
    pn.widgets.Button(name="C", button_type="danger"),
)'''

app.servable()
