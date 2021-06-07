import os

import pandas as pd

### Программа формирования и сохранения .xlsx таблицы


def form_table(id, dictionary):
    if os.path.exists(f'/userfiles/tables/{id}.xlsx'):
        os.remove(f'/userfiles/tables/{id}.xlsx')
    table = pd.DataFrame(dictionary)
    table.to_excel(f'./userfiles/tables/{id}.xlsx', sheet_name='Статистика', index=False)
