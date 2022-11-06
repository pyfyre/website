from typing import List
from pyfyre.nodes import *
from components import CallToAction


_FEATURES = [
    [
        "Developer friendly",
        "python-logo.png",
        "The language you already know.",
        "PyFyre allows you to develop web apps with the language you already know, "
        "Python, and only Python. Create reactive websites with ease. "
        "Build your apps in minutes, not days.",
        "Show me",
    ],
    [
        "Productive",
        "pypi-logo.jpg",
        "Use CPython packages on the client-side web.",
        "Developers can limitedly use CPython packages on the client-side web. "
        "Develop sites quickly and efficiently with a large selection of packages.",
        "Visit pypi.org/",
    ],
]


class Feature(Widget):
    def __init__(self, index: int) -> None:
        self.index = index
        super().__init__()

    def build(self) -> List[Node]:
        i = self.index
        l0 = "items-start" if i % 2 == 0 else "items-end"
        l1 = "md:flex-row-reverse" if i % 2 == 0 else "md:flex-row"

        return [
            Element(
                "div",
                lambda: [
                    Element(
                        "div",
                        lambda: [
                            Element(
                                "img",
                                attrs={
                                    "class": "object-cover object-center "
                                    "rounded-lg w-52 mx-auto md:w-auto",
                                    "loading": "lazy",
                                    "width": "500",
                                    "height": "500",
                                    "src": _FEATURES[i][1],
                                },
                            )
                        ],
                        attrs={"class": "w-full mb-10 lg:w-1/3 lg:w-3/12 md:w-1/2"},
                    ),
                    Element(
                        "div",
                        lambda: [
                            Element(
                                "p",
                                lambda: [Text(_FEATURES[i][0])],
                                attrs={
                                    "class": "mb-8 text-lg font-semibold tracking-widest "
                                    "text-black uppercase title-font text-[#333333]"
                                },
                            ),
                            Element(
                                "p",
                                lambda: [Text(_FEATURES[i][2])],
                                attrs={
                                    "class": "mb-8 text-2xl font-black tracking-tighter "
                                    "text-black md:text-5xl title-font text-[#333333]"
                                },
                            ),
                            Element(
                                "p",
                                lambda: [Text(_FEATURES[i][3])],
                                attrs={
                                    "class": "mb-8 text-base leading-relaxed text-left "
                                    "text-blueGray-600 text-[#333333]"
                                },
                            ),
                        ],
                        attrs={
                            "class": f"flex flex-col {l0} mb-16 text-left "
                            "lg:flex-grow md:w-1/2 lg:pr-24 md:pr-16 md:mb-0"
                        },
                    ),
                ],
                attrs={
                    "class": f"flex flex-col items-center px-5 py-16 mx-auto {l1} lg:px-28"
                },
            )
        ]


class Home(Widget):
    def build(self) -> List[Node]:
        return [
            Element(
                "div",
                lambda: [
                    Element(
                        "div",
                        lambda: [
                            Element(
                                "div",
                                lambda: [
                                    Element(
                                        "p",
                                        lambda: [Text("The Python Web")],
                                        attrs={
                                            "class": "text-5xl mx-auto font-bold "
                                            "bg-clip-text h-20 text-[#222222] xl:text-7xl"
                                        },
                                    ),
                                    Element(
                                        "p",
                                        lambda: [Text("Frontend Framework")],
                                        attrs={
                                            "class": "text-5xl mx-auto font-bold "
                                            "bg-clip-text h-20 text-transparent "
                                            "bg-gradient-to-r from-cyan-500 to-blue-500 xl:text-7xl"
                                        },
                                    ),
                                ],
                                attrs={"class": "flex flex-col"},
                            ),
                            Element(
                                "p",
                                lambda: [
                                    Text(
                                        "A fast, declarative, and incrementally "
                                        "adoptable Python web frontend framework "
                                        "for building reactive web user interfaces."
                                    )
                                ],
                                attrs={
                                    "class": "text-lg px-10 xl:text-xl mx-auto "
                                    "mt-5 xl:px-52 text-center text-[#3c3c3c]"
                                },
                            ),
                        ],
                        attrs={"class": "flex flex-col w-full mt-28"},
                    ),
                    Element(
                        "div",
                        lambda: [
                            Link(
                                "https://pyfyre-docs.netlify.app/",
                                lambda: [Text("Get started")],
                                attrs={
                                    "class": "bg-[#fab327] w-fit px-5 py-2 "
                                    "text-base rounded-3xl text-white cursor-pointer"
                                },
                            ),
                            RouterLink(
                                "/playground",
                                lambda: [Text("Learn")],
                                attrs={
                                    "class": "bg-[#f1f1f1] w-fit px-5 py-2 "
                                    "text-base rounded-xl text-[#474747] "
                                    "hover:text-[#333333] cursor-pointer"
                                },
                            ),
                        ],
                        attrs={"class": "flex space-x-3 mx-auto mt-20 mb-44"},
                    ),
                ],
                attrs={"class": "flex flex-col w-full h-5/6"},
            ),
            Element("div", lambda: [Feature(i) for i, _ in enumerate(_FEATURES)]),
            CallToAction(
                "Brython",
                "PyFyre is powered by Brython, a Python 3 implementation for client-side web programming.",
                "https://brython.info",
            ),
        ]
