"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc

docs_url = "https://yunwoong.tistory.com/"
filename = f"{config.app_name}/{config.app_name}.py"


class State(pc.State):
    """The app state."""
    pass


def index() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.heading("Welcome to Home!", font_size="2em"),
            pc.box("I am very excited and looking forward to using pynecone."),
            pc.link(
                "Go to my blog!",
                href=docs_url,
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    "color": "rgb(107,99,246)",
                },
            ),
            spacing="1.5em",
            font_size="2em",
        ),
        padding_top="10%",
    )


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)
app.compile()
