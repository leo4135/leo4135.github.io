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
