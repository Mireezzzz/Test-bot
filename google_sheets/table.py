import gspread


def add_result(id: int, name: str, answers: list[str], path: str | None = None):
    res = [id, name]
    res += [ans[0] for ans in answers]
    gc = gspread.service_account(filename=path)
    sh = gc.open("Результаты")
    worksheet = sh.sheet1
    worksheet.append_row(res)


def get_answer(path: str | None = None):
    gc = gspread.service_account(filename=path)
    sh = gc.open("Результаты")
    worksheet = sh.sheet1
    values_list = worksheet.row_values(1)
    return values_list[2:]
