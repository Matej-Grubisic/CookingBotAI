import flet as ft

def main(page: ft.Page):
    page.title = "Cooking Bot AI"
    page.window_maximized = True
    page.theme_mode = "light"
    page.padding = 30

    # Message area (middle section)
    messages = ft.ListView(expand=True, spacing=10, auto_scroll=True)

    # Dropdown (top)
    dropdown = ft.Dropdown(
        label="Choose cooking style",
        options=[
            ft.dropdown.Option("French"),
            ft.dropdown.Option("Italian"),
            ft.dropdown.Option("Asian"),
            ft.dropdown.Option("Mexican"),
        ],
        width=300,
    )

    # Ingredients input (bottom input bar)
    ingredients_input = ft.TextField(
        hint_text="Enter ingredients (e.g. chicken, garlic, rice)...",
        multiline=True,
        min_lines=1,
        max_lines=3,
        expand=True,
    )

    # Respond function (handles button click)
    def respond(e):
        style = dropdown.value
        ingredients = ingredients_input.value.strip()

        if not style:
            messages.controls.append(ft.Text("⚠️ Please select a cooking style.", color="red"))
        elif not ingredients:
            messages.controls.append(ft.Text("⚠️ Please enter some ingredients.", color="red"))
        else:
            # User message
            user_msg = ft.Text(f"🧑‍💻 You: I have {ingredients} and I want a {style} recipe.", weight="bold")
            messages.controls.append(user_msg)

            # Simulated bot response
            bot_msg = ft.Text(f"🤖 Cooking Bot: Here's a {style} recipe using your ingredients:\n[Recipe goes here...]", italic=True)
            messages.controls.append(bot_msg)

        ingredients_input.value = ""
        page.update()

    send_btn = ft.ElevatedButton("Get Recipe", on_click=respond)

    # Layout
    page.add(
        ft.Column(
            [
                ft.Text("🍳 Cooking Bot AI", size=32, weight="bold"),
                dropdown,
                ft.Container(messages, expand=True),
                ft.Row(
                    [ingredients_input, send_btn],
                    alignment=ft.MainAxisAlignment.END,
                ),
            ],
            expand=True,
        )
    )

ft.app(target=main)
