from typing import List
from browser import DOMEvent, window
from pyfyre import Style
from pyfyre.nodes import *


class Header(Widget):
    def __init__(self) -> None:
        super().__init__(
            attrs={
                "class": "bg-white border-gray-200 px-2 "
                "sm:px-4 py-2.5 border-b-2 sticky top-0"
            },
            styles=[Style(z_index="1000")],
        )

    def build(self) -> List[Node]:
        def go_to_repo(event: DOMEvent) -> None:
            window.location.href = "https://github.com/pyfyre/pyfyre"

        return [
            Element(
                "div",
                lambda: [
                    Element(
                        "div",
                        lambda: [
                            RouterLink(
                                "/",
                                lambda: [
                                    Element(
                                        "img",
                                        attrs={
                                            "class": "w-10",
                                            "src": "/pyfyre-logo.jpg",
                                        },
                                    )
                                ],
                            )
                        ],
                        attrs={"class": "flex"},
                    ),
                    Element(
                        "div",
                        lambda: [
                            Element(
                                "div",
                                lambda: [
                                    Link(
                                        "https://pyfyre-docs.netlify.app/",
                                        lambda: [Text("Documentation")],
                                        attrs={
                                            "class": "block py-2 pr-4 pl-3 "
                                            "text-base text-black md:bg-transparent "
                                            "md:text-black md:p-0 cursor-pointer"
                                        },
                                    ),
                                    RouterLink(
                                        "/playground",
                                        lambda: [Text("Playground")],
                                        attrs={
                                            "class": "block py-2 pr-4 pl-3 "
                                            "text-base text-black md:bg-transparent "
                                            "md:text-black md:p-0 cursor-pointer"
                                        },
                                    ),
                                ],
                                attrs={"class": "invisible flex space-x-5 lg:visible"},
                            ),
                            Button(
                                go_to_repo,
                                lambda: [
                                    Element(
                                        "img",
                                        attrs={
                                            "class": "w-7 h-auto",
                                            "src": "https://cdn-icons-png.flaticon.com/512/25/25231.png",
                                        },
                                    )
                                ],
                                styles=[Style(cursor="pointer")],
                                attrs={"class": "mr-3"},
                            ),
                        ],
                        attrs={"class": "flex items-center space-x-5"},
                    ),
                ],
                attrs={"class": "flex flex-wrap justify-between items-center mx-auto"},
            )
        ]


class CallToAction(Widget):
    def __init__(self, title: str, desc: str, link: str) -> None:
        self.title = title
        self.desc = desc
        self.link = link

        super().__init__(
            attrs={
                "class": "flex flex-col w-full h-3/6 justify-center mx-auto "
                "bg-gradient-to-r from-[#4568dc] to-[#b06ab3] text-white p-10"
            }
        )

    def build(self) -> List[Node]:
        return [
            Element(
                "p",
                lambda: [Text(self.title)],
                attrs={"class": "text-md font-bold"},
            ),
            Element(
                "p",
                lambda: [Text(self.desc)],
                attrs={"class": "text-3xl w-4/6 font-normal"},
            ),
            Element(
                "div",
                lambda: [
                    Link(
                        self.link,
                        lambda: [Text(f"Visit {self.link}")],
                        attrs={
                            "class": "bg-transparent border border-white "
                            "w-fit px-5 py-2 text-base rounded-3xl cursor-pointer "
                            "hover:bg-white hover:text-[#222222]",
                            "target": "_blank",
                        },
                    )
                ],
                attrs={"class": "mt-5"},
            ),
        ]
