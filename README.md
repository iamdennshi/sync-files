### Описание

Скрипт синхронизации файлов и директорий


### Установка

```sh
git clone git@github.com:iamdennshi/sync-files.git
cd sync-files
python -m venv venv
./venv/Scripts/activate
pip install -r ./requirements.txt
```


### Использование
> Если в директории назначения присутсвуют файлы, которых нет в источнике, то при синхронизации они удаляются

`py main.py` или через батник `sync.bat`

### Конфигурация

В файле `config.py` указать пару источник и назначение

```py
paths = {
  "source": "target",
  "source1": "target1"
}
```
