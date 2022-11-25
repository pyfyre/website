/* eslint no-var: 0, no-undef: 0 */

var CodeMirrorAPI = {"codeMirror": null};
var CodeListen = {
    "listeners": [],
    "listen": (listener) => CodeListen.listeners.push(listener),
    "broadcast": () => {
        for (const listener of CodeListen.listeners) {
            listener();
        }
    }
};

window.addEventListener("pyfyreload", () => {
    CodeMirrorAPI.codeMirror = CodeMirror.fromTextArea(
        document.getElementById("code-editor"),
        {
            "lineNumbers": true,
            "mode": "python",
            "tabSize": 4,
            "smartIndent": true,
            "extraKeys": {
                "Tab": (cm) => {
                    cm.replaceSelection("    ", "end");
                },
                "Enter": (cm) => {
                    cm.replaceSelection("\n");
                }
            }
        }
    );
    CodeMirrorAPI.codeMirror.setSize(width = "100%", height = "100%");
    CodeMirrorAPI.codeMirror.on("change", CodeListen.broadcast);
    CodeMirrorAPI.codeMirror.setValue(`from pyfyre.nodes import Node, Widget, Element, Text


class App(Widget):
    def build(self) -> list[Node]:
        return [Element("p", lambda: [Text("Hello, World!")])]


# We use this here instead of \`render\`.
render_playground(lambda: App())
`);
});
