import sys
from typing import Callable
from browser import window, document
from pyfyre import Style
from pyfyre.nodes import *
from pyfyre.presets import DebugError


def render_playground(node_builder: Callable[[], Node]) -> None:
    out = document.select_one("#output-id")
    out.clear()

    try:
        node = node_builder()
    except Exception:
        node = DebugError(*sys.exc_info())

    if isinstance(node, Element):
        node.build_children()

    out.attach(node.dom)


class Playground(Widget):
    def __init__(self) -> None:
        def code_listener() -> None:
            try:
                exec(window.CodeMirrorAPI.codeMirror.getValue())
            except Exception:
                out = document.select_one("#output-id")
                out.clear()
                error = DebugError(*sys.exc_info())
                error.build_children()
                out.attach(error.dom)

        window.CodeListen.listen(code_listener)
        super().__init__(
            styles=[Style(height="calc(100vh - 62px)")],
            attrs={"class": "flex flex-row w-full h-screen"},
        )

    def build(self) -> list[Node]:
        return [
            Element(
                "div",
                lambda: [
                    TextInput(
                        multiline=True,
                        attrs={"id": "code-editor", "cols": "40", "rows": "5"},
                    )
                ],
                attrs={"class": "flex flex-col w-6/12"},
            ),
            Element(
                "div",
                lambda: [
                    Element(
                        "div",
                        attrs={
                            "class": "p-2 h-full w-full",
                            "id": "output-id",
                        },
                    ),
                ],
                styles=[Style(overflow="scroll", width="50%")],
                attrs={"class": "border-l-4"},
            ),
        ]
