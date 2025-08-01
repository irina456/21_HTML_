from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    """
    Этот класс обрабатывает входящие HTTP-запросы.
    Он наследует функциональность от BaseHTTPRequestHandler.
    """

    def do_GET(self) -> None:
        """Обработчик GET-запросов. Отправляет HTML-файл, если он найден,
        или сообщение об ошибке 404, если файл не найден.
        """
        try:
            # Пытаемся открыть и прочитать файл contacts.html
            with open("contacts.html", "rb") as file:
                file_content = file.read()

            # Если файл открылся успешно, отправляем ответ 200 OK
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(file_content)  # Отправляем содержимое файла клиенту

        except FileNotFoundError:
            # Если файл не найден, отправляем ответ 404 Not Found
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"File not found")

if __name__ == "__main__":
    # Создаем HTTP-сервер, прослушивающий указанный хост и порт
    webServer = HTTPServer((hostName, serverPort), MyServer)

    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Запускаем сервер в бесконечном цикле, пока он не будет остановлен вручную
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Обрабатываем прерывание с клавиатуры (Ctrl+C)
        pass

    webServer.server_close()  # Закрываем сервер
    print("Server stopped.")
