### На основе протестированных требований к странице авторизации компании "Ростелеком",  
### созданы позитивные и негативные тестовые сценарии, с использованием техник тест-дизайна  
#### Тестовые сценарии:
EXP-001  
Перенаправление пользователя на страницу Личного кабинета при успешной регистрации по почте  
pytest -v -s tests/test_exp_001.py --alluredir results  
allure serve results  
EXP-002  
Перенаправление пользователя на страницу Личного кабинета при успешной регистрации по телефону  
pytest -v -s tests/test_exp_002.py --alluredir results  
allure serve results  
EXP-003  
Перенаправление пользователя на страницу Личного кабинета при успешной авторизации по телефону  
pytest -v -s tests/test_exp_003.py  
EXP-004  
Перенаправление пользователя на страницу Личного кабинета при успешной авторизации по почте  
pytest -v -s tests/test_exp_004.py  
EXP-005  
Проверка валидации поля "Имя" на странице регистрации при вводе минимального количества корректных символов  
pytest -v -s tests/test_exp_005.py  
EXP-006  
Проверка валидации поля "Имя" на странице регистрации при вводе корректных символов в количестве 1/2 максимального диапазона
pytest -v -s tests/test_exp_006.py  
EXP-007	
Проверка валидации поля "Имя" на странице регистрации при вводе максимального количества корректных символов  
pytest -v -s tests/test_exp_007.py  
EXP-008  
Проверка валидации поля "Фамилия" на странице регистрации при вводе минимального количества корректных символов  
pytest -v -s tests/test_exp_008.py  
EXP-009  
Проверка валидации поля "Фамилия" на странице регистрации при вводе корректных символов в количестве 1/2 максимального диапазона  
pytest -v -s tests/test_exp_009.py  
EXP-010  
Проверка валидации поля "Фамилия" на странице регистрации при вводе максимального количества корректных символов  
pytest -v -s tests/test_exp_010.py  
EXP-011  
Проверка валидации поля "Имя" на странице регистрации при вводе некорректных количества символов в количестве меньше минимального значения  
pytest -v -s tests/test_exp_011.py  
EXP-012  
Проверка валидации поля "Имя" на странице регистрации при вводе некорректного количества символов в количестве больше максимального диапазона  
pytest -v -s tests/test_exp_012.py  
EXP-013  
Проверка валидации поля "Имя" на странице регистрации при вводе пустого значения  
pytest -v -s tests/test_exp_013.py  
EXP-014  
Проверка валидации поля "Имя" на странице регистрации при вводе некорректных данных в виде спецсимволов  
pytest -v -s tests/test_exp_014.py  
EXP-015  
Проверка валидации поля "Имя" на странице регистрации при вводе некорректных данных состоящих из латиницы  
pytest -v -s tests/test_exp_015.py  
EXP-016  
Проверка валидации поля "Фамилия" на странице регистрации при вводе некорректного количества символов в количестве меньше минимального значения  
pytest -v -s tests/test_exp_016.py  
EXP-017  
Проверка валидации поля "Фамилия" на странице регистрации при вводе некорректного количества символов в количестве больше максимального диапазона  
pytest -v -s tests/test_exp_017.py  
EXP-018  
Проверка валидации поля "Фамилия" на странице регистрации при вводе пустого значения  
pytest -v -s tests/test_exp_018.py  
EXP-019  
Проверка валидации поля "Фамилия" на странице регистрации при вводе некорректных данных в виде спецсимволов  
pytest -v -s tests/test_exp_019.py  
EXP-020  
Проверка валидации поля "Фамилия" на странице регистрации при вводе некорректных данных состоящих из латиницы  
pytest -v -s tests/test_exp_020.py  
EXP-021  
Проверка валидации поля "Подтверждение пароля" на странице регистрации при вводе несовпадающих данных  
pytest -v -s tests/test_exp_021.py
