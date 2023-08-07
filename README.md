# FunBox
Небольшое API, сохраняющее уникальные домены при передачи по api/append и возвращающие список с возможностью фильтрации по времени.

# api/append
Request
`````{
            "links": [
                "https://ya.ru",
                "https://ya.ru?q=123",
                "fuuuuuuunbox.ru",
                "funbox.ru",
                "https://stackoverflow.com/questions/11828270/how-to-exit-the-vim-editor"
            ]
        }
`````
Response
``{
    "status": 201
}``

# api/get_sites?from=1545221231&to=1545217638
Если не передавать GET параметры будет возвращен полный список уникальных доменов

Request ``{}``

Response 
`````
{
    "domain": [
        "funbox.ru",
        "fuuuuuuunbox.ru",
        "stackoverflow.com",
        "ya.ru"
    ],
    "status": 200
}
`````