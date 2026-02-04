
import panel as pn

pn.extension()

# Create multiple cards
card1 = pn.Card(
    pn.Column(
        "📦 Product A",
        "Price: $29",
        pn.widgets.Button(name="Buy", button_type="primary"),
    ),
    title="Product A"
)

card2 = pn.Card(
    pn.Column(
        "📦 Product B",
        "Price: $49",
        pn.widgets.Button(name="Buy", button_type="success"),
    ),
    title="Product B"
)

card3 = pn.Card(
    pn.Column(
        "📦 Product C",
        "Price: $19",
        pn.widgets.Button(name="Buy", button_type="warning"),
    ),
    title="Product C"
)

card4 = pn.Card(
    pn.Column(
        "📦 Product D",
        "Price: $99",
        pn.widgets.Button(name="Buy", button_type="danger"),
    ),
    title="Product D"
)

# GridBox with cards inside
grid = pn.GridBox(
    card1,
    card2,
    card3,
    card4,
    ncols=2
)

app = pn.Column(
    "# 🛒 Product Dashboard",
    "Select a product from the cards below:",
    grid
)

app.servable()

