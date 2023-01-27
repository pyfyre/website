from typing import List
from pyfyre import render
from pyfyre.nodes import *
from components import Header
from home import Home
from playground import Playground

class HomePage(Widget):
    def build(self) -> List[Node]:
        return [Header(), Home()]

class PlaygroundPage(Widget):
    def build(self) -> List[Node]:
        return [Header(), Playground()]

render(
    {
        "/": lambda: HomePage(),
        "/playground": lambda: PlaygroundPage(),
    }
)
