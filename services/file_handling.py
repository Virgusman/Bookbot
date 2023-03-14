BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    new_size = size
    if text[start+size-1:start+size+1] == "..":
        new_size = new_size - 2
    line: str = text[start: start + new_size]
    end: int = 0
    for simvol in [',','.','!',':',';','?']:
        ind: int = line.rfind(simvol)
        if ind > end:
            end = ind
    line = line[0:end+1]
    return [line, len(line)]



# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    f = open(path, 'r', encoding="utf8")
    line: str = f.read()
    marker = 0
    count = 1
    while marker < len(line):
        l, s  = _get_part_text(line,marker,PAGE_SIZE)
        book[count] = l.lstrip()
        count+=1
        marker+=s
    f.close()


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(BOOK_PATH)