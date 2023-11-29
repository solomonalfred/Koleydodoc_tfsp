class ERROR:
    OK = 0
    BAD_INPUT = 1
    BAD_PARAMS = 2
    BAD_MODEL = 3

MSG_ERROR = {
    ERROR.BAD_INPUT: "Недостаточно данных",
    ERROR.BAD_PARAMS: "Просим прощения, что-то не так на сервере",
    ERROR.BAD_MODEL: "Просим прощения, что-то не так на сервере"
}

class APIInputDataTypes:
    TEXT_TEXT = "text/text"
    FILE_DOCX = "file/docx"


class APIOutputDataTypes:
    JSON_SIMPLE = "json/simple"
    JSON_TAGGED = "json/tagged"
    FILE_DOCX = "file/docx"

class APILanguage:
    ENG = "lang/eng"
    RUS = "lang/rus"

class Tags:
    NEUTRAL = 0
    WARNING = 1