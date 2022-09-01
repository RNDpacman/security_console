#### Веб-интерфейс пульта охраны банка

- Отслеживает людей, находящихся в хранилище.
- Отображает все активные пропуска.
- Выводит информацию о всех посещениях любого человека и их продолжительность.
- Слишком долгие посещения помечаются как подозрительные и выводятся на пульт.

### Установка

```
git clone https://github.com/RNDpacman/security_console.git
```

```
cd ./security_console
```

```
python -m venv ./venv
```

```
source ./venv/bin/activate
```

```
pip install --upgrade pip
```

```
pip install -r ./requirements.txt
```

```
python ./main.py
```

Откройте ссылку в браузере
```
http://127.0.0.1:8000
```
