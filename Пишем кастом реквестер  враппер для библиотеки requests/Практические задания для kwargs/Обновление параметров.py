def update_settings(default_settings, **kwargs):
    default_settings.update(kwargs)
    return default_settings





default_settings = {"theme": "light", "notifications": True}
print(update_settings(default_settings, theme="dark", volume=80))
# Вывод: {'theme': 'dark', 'notifications': True, 'volume': 80}