
import panel as pn

pn.extension()

card1 = pn.Card(
    pn.Column(
        pn.pane.Image("image-1.png", width=300),
        "👟 Sneaker Model A",
        "Price: $89",
        pn.widgets.Button(name="Buy", button_type="primary"),
    ),
    title="Sneaker A"
)

card2 = pn.Card(
    pn.Column(
        pn.pane.Image("image-2.png", width=300),
        "👟 Running Shoe B",
        "Price: $109",
        pn.widgets.Button(name="Buy", button_type="success"),
    ),
    title="Running Shoe B"
)

card3 = pn.Card(
    pn.Column(
        pn.pane.Image("image-3.png", width=300),
        "👟 Casual Shoe C",
        "Price: $69",
        pn.widgets.Button(name="Buy", button_type="warning"),
    ),
    title="Casual Shoe C"
)

grid = pn.GridBox(
    card1, card2, card3,
    ncols=3
)

app = pn.Column(
    "# 👟 Shoe Gallery",
    "Three different shoes loaded from local images:",
    grid
)

app.servable()
