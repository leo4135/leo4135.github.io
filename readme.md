## TODO для развертывания проекта

**Шаг первый:**

* Склонируйте репозиторий в свое рабочее окружение

  > git clone https://github.com/leo4135/leo4135.github.io.git

**Шаг второй:**

* Установите виртуальное окружение и зависимости при помощи команд (а также pip):

  > virtualenv python_venv

  > source python_venv/bin/activate

  > pip install mkdocs

* Если не установлен pip:

  > python -m pip install --upgrade pip

**Шаг третий:**

* Локальный запуск:

  > mkdocs serve

![Изображение, демонстрирующее текущий шаг](https://i.imgur.com/P0EXIKj.png)

**Шаг четвертый:**

* Настройка CI/CD через github ACTIONS:

  * Создание новой директории в папке проекта:

    > mkdir .github/workflows

  * Перейти в вышеупомянутую директорию:

    > cd .github/workflows

  * Создать файл с расширением .yml и написать конфигурацию:

    > nano deploy.yml

  * Пример текущей конфигурации:

    ```
    name: Deploy MkDocs and build

    on:
    push:
        branches:
        - main

    jobs:
    build-and-deploy:
        runs-on: ubuntu-latest

        steps:
        # 1. Клонируем репозиторий
        - name: Checkout repository
            uses: actions/checkout@v3

        # 2. Устанавливаем Python
        - name: Setup Python
            uses: actions/setup-python@v4
            with:
            python-version: 3.9

        # 3. Устанавливаем зависимости
        - name: Install dependencies
            run: |
            python -m pip install --upgrade pip
            pip install mkdocs # Добавьте другие зависимости, если они есть

        # 4. Собираем сайт
        - name: Build MkDocs site
            run: mkdocs build

        # 5. Заливаем собранный сайт в ветку main
        - name: Deploy to GitHub Pages
            run: |
            git config user.name "GitHub Actions"
            git config user.email "actions@github.com"
            cp -r site/* ./  # Переносим содержимое из site в корень
            rm -rf site
            git add .
            git commit -m "Deploy MkDocs site via GitHub Actions" || echo "No changes to commit"
            git push origin main 
    ```

**Шаг пятый:**

* Успешный deploy при помощи **github actions**:

  > git add .

  > git commit -m "create config .yml for github actions"

  > git push

   ![Демонстрация изображения с исполнением текущего шага](https://i.imgur.com/qU41iWQ.png)

**Шаг шестой:**

* Кастомизация статического сайта:

  * Установка плагина  mkdocs-macros-plugin для поддержки Jinja2

    > pip install mkdocs-macros-plugin
    
  * Создание в корневой директории файла ***main.py*** для определения глобальных переменных и функций

    ```
    def define_env(env):
    """
    Определение макросов и переменных для MkDocs.
    """
    # Глобальная переменная для шаблонов
    env.variables['author'] = "leo4135"

    # Пример макроса для Markdown
    @env.macro
    def get_author():
        return env.variables['author']
    ```

  * Подключение main.py к проекту mkdocs в .yml:

    ```
      plugins:
         - macros:
              module_name: main
    ```
  
  * Создание директории с кастомизированной темой по примеру:

    ```
    └── my-theme/
      ├── main.html
      ├── css/
      │   └── custom.css
      └── js/
          └── custom.js
    ```

  * 
