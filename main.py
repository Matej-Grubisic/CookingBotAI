import flet as ft
from API.Agent import run_agent
import json

def main(page: ft.Page):
    page.title = "Cooking Bot AI"
    page.window_maximized = True
    page.theme_mode = "light"
    page.padding = 30

    messages = ft.ListView(expand=True, spacing=10, auto_scroll=True)

    dropdown_style = ft.Dropdown(
        label="Cooking Style",
        options=[
            ft.dropdown.Option("French"),
            ft.dropdown.Option("Italian"),
            ft.dropdown.Option("Asian"),
            ft.dropdown.Option("Mexican"),
        ],
        width=200,
    )

    dropdown_difficulty = ft.Dropdown(
        label="Difficulty",
        options=[
            ft.dropdown.Option("Easy"),
            ft.dropdown.Option("Medium"),
            ft.dropdown.Option("Hard"),
            ft.dropdown.Option("Pro"),
        ],
        width=150,
    )

    ingredients_input = ft.TextField(
        hint_text="Enter ingredients (e.g. chicken, garlic, rice)...",
        multiline=True,
        min_lines=1,
        max_lines=3,
        expand=True,
    )

    def respond(e):
        style = dropdown_style.value
        difficulty = dropdown_difficulty.value
        ingredients = ingredients_input.value.strip()

        if not style or not difficulty:
            messages.controls.append(ft.Text("⚠️ Please select both style and difficulty.", color="red"))
        elif not ingredients:
            messages.controls.append(ft.Text("⚠️ Please enter some ingredients.", color="red"))
        else:
            user_msg = ft.Text(
                f"🧑‍💻 You: I have {ingredients} and want a {difficulty} {style} recipe.",
                weight="bold"
            )
            messages.controls.append(user_msg)

            try:
                input_data = json.dumps({
                    "message": ingredients,
                    "food_style": style,
                    "difficulty": difficulty
                })

                response = run_agent(difficulty, input_data)

                recipe = response if isinstance(response, str) else "❌ Error: Response is not a valid string."

            except Exception as ex:
                recipe = f"❌ Error generating recipe: {str(ex)}"

            bot_msg = ft.Text(
                f"🤖 Cooking Bot:\n{recipe}",
                italic=True
            )
            messages.controls.append(bot_msg)

        ingredients_input.value = ""
        page.update()

    send_btn = ft.ElevatedButton("Get Recipe", on_click=respond)

    page.add(
        ft.Column(
            [
                ft.Text("🍳 Cooking Bot AI", size=32, weight="bold"),
                ft.Row([dropdown_style, dropdown_difficulty], spacing=20),
                ft.Container(messages, expand=True),
                ft.Row([ingredients_input, send_btn], alignment=ft.MainAxisAlignment.END),
            ],
            expand=True,
        )
    )

ft.app(target=main)
