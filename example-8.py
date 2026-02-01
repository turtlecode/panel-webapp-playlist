import panel as pn

pn.extension()

# Username input
username_input = pn.widgets.TextInput(
    name="Username",
    placeholder="Enter your username"
)

# Password input (masked)
password_input = pn.widgets.PasswordInput(
    name="Password",
    placeholder="Enter your password"
)

# Login button
login_button = pn.widgets.Button(
    name="Login",
    button_type="primary"
)

# Output area
output = pn.pane.Markdown("Please enter your username and password.")

# Login function
def check_login(event):
    username = username_input.value.strip()
    password = password_input.value.strip()

    if username == "turtle" and password == "turtle":
        output.object = "✅ **Welcome, Turtle!** 🐢"
    else:
        output.object = "❌ Username or password is incorrect."

# Attach event to button
login_button.on_click(check_login)

# Layout
app = pn.Column(
    "# 🔐 Simple Login Screen",
    "Enter your credentials to log in.",
    username_input,
    password_input,
    login_button,
    output
)

app.servable()
