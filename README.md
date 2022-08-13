# schedule-bot-kpk
[![GitHub issues](https://img.shields.io/github/issues/Foxius/schedule-bot-kpk?style=plastic)](https://github.com/Foxius/schedule-bot-kpk/issues) [![GitHub stars](https://img.shields.io/github/stars/Foxius/schedule-bot-kpk)](https://github.com/Foxius/schedule-bot-kpk/stargazers) [![GitHub forks](https://img.shields.io/github/forks/Foxius/schedule-bot-kpk)](https://github.com/Foxius/schedule-bot-kpk/network)

**Описание:** Бот, отсылающий в телеграмм расписание для отдельных групп Копейского Политехнического Техникума

## Алгоритм работы для разработчика

1 - Открываем файл `bot.py`

2 - В 11 строке (выделенной рамкой из комментариев) меняем значение токена на свое, полученое в BotFather. Получится нечто: `bot = telebot.TeleBot('цифарки:оченьмногослучайныхбуквнаанглийском')`

3 - Для того чтобы загрузить новое расписание - стери строки старого в файле `data.xlsx` и введи новое по образу и подобию

## Адаптация под своё учебное заведение

Для адаптации под свой техникум или универ - вам необходимо заменить названия групп в `data.xlsx` и в файлах `year20.py`,`year21.py`,`year22.py`. Названия файлов означают год, в котором та или иная группа поступила. Импортируется в основной файл при помощи `import yearXX *` (без расширения .py). Если что то непонятно по адаптации - то пишите issues, вместе разберемся

## Алгоритм работы для юзера

1 - Зайдите в бота и нажмите на /start

2 - Увидев приветственное сообщение, выберите группу, для получения расписания, или иную команду

![photorepo0](https://media.discordapp.net/attachments/927545383612203018/1008023931799732275/unknown.png)
