import sys
from typing import Callable, List
from browser import window, document
import pyfyre
from pyfyre import Style
from pyfyre.nodes import *
from pyfyre.presets import DebugError

pyfyre.PRODUCTION = False

EXAMPLES = [
    {
        'title': "Introduction",
        'children': [
            {
                'title': 'Hello, World',
                'code': """from pyfyre.nodes import Node, Widget, Element, Text

class App(Widget):
    def build(self) -> list[Node]:
        return [
            Element("p",
                lambda: [
                    Text("Hello, World!")
                ]
            )
        ]

# We use this here instead of `render`.
render_playground(lambda: App())"""
            },
            {
                'title': 'Styling',
                'code': """from pyfyre.nodes import Node, Widget, Element, Text

class App(Widget):
    def build(self) -> list[Node]:
        return [
            Element("p",
                lambda: [
                    Text("Nice Styling")
                ],
                attrs={
                    "style": "font-size: 7rem; color: orange;",
                    "class": "more-style-from-scoped-css"
                }
            )
        ]

# We use this here instead of `render`.
render_playground(lambda: App())"""
            },
            {
                'title': 'Nested Components',
                'code': """from pyfyre.nodes import Node, Widget, Element, Text

class App(Widget):
    def build(self) -> list[Node]:
        return [
            Element("div",
                lambda: [
                    Navbar(),
                    Text("Welcome to the Company!"),
                ]
            )
        ]

class Navbar(Widget):
    def build(self) -> list[Node]:
        return [Text("Acme, Inc.")]

# We use this here instead of `render`.
render_playground(lambda: App())"""
            }
        ]
    },
    {
        'title': 'Reactivity',
        'children': [
            {
                'title': 'Reactive Assignments',
                'code': """from pyfyre.nodes import Node, Widget, Element, Text
from pyfyre import State

class App(Widget):
    def __init__(self):
        self.count = State[int](0)
        super().__init__()

    def build(self) -> list[Node]:
   
        def increment(ev):
            self.count.set_value(self.count.value + 1)

        return [
            Button(children=lambda: [
                Text("Clicked ", self.count, " times")
            ], onclick=increment)
        ]

# We use this here instead of `render`.
render_playground(lambda: App())"""
            }
        ]
    }
]

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
            attrs={"class": "flex flex-col-reverse md:flex-row w-full md:h-screen"},
        )

    def build(self) -> List[Node]:

        def category(i):
            _item = EXAMPLES[i]

            def item(i):
                code = _item['children'][i]

                def view(e):
                    window.CodeMirrorAPI.codeMirror.setValue(code['code'])
                
                return Button(children=lambda: [
                    Text(code['title'])
                ], onclick=view)

            return Element("div", lambda: [
                Element('p', lambda: [Text(_item['title'])], attrs={"class": "text-xl font-bold"}),
                ListBuilder(
                    count=len(_item['children']),
                    item_builder=item,
                    attrs={"class": "flex flex-col items-start space-y-1 text-md"}
                )
            ], attrs={"class": "mt-4"})

        return [
            ListBuilder( # Categories Builder
                count=len(EXAMPLES),
                item_builder=category,
                attrs={"class": "w-full md:w-3/12 px-4 mt-1"}
            ),
            Element(
                "div",
                lambda: [
                    TextInput(
                        multiline=True,
                        attrs={"id": "code-editor", "cols": "40", "rows": "5"},
                    )
                ],
                attrs={"class": "flex flex-col w-full md:w-6/12"},
            ),
            Element(
                "div",
                lambda: [
                    Element(
                        "div",
                        styles=[Style(all="initial")],
                        attrs={"id": "output-id"},
                    ),  
                ],
                styles=[Style(overflow="scroll")],
                attrs={"class": "border-l-4 p-2 h-full w-full md:w-6/12"},
            ),
        ]
