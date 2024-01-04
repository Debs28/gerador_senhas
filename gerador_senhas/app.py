import webview
from gerador_senhas import Api

if __name__ == "__main__":
    api = Api()
    window = webview.create_window(
        title="Gerador de Senhas",
        url="assets/index.html",
        width=700,
        height=620,
        x=None,
        y=None,
        resizable=True,
        fullscreen=False,
        js_api=api,
    )
    webview.start()
