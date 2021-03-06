Title: Долой Evernote, да здравствуют простые решения!
Slug: no-more-evernote
Date: 2014-12-09 14:48
Category: texts
Tags: productivity
Lang: ru

Сегодня я расскажу про то, как Evernote вывел меня из себя, и я решил написать очередной велосипед.

А дело было так
---------------

После недавнего апгрейда, Evernote (программа где я храню разнообразные заметки и через которую проходят многие мои TODO записи), стал не только страшно выглядеть, но и страшно глючить. Самый неприятный баг состоял в том, что в какой-то момент он просто прекращал показывать текст заметки. Кликаешь на нее, а экран пустой. Перезапуск не помогал. Точнее помогал, но через какое-то время -- через час, два или сутки. Короче -- полный кошмар.

Тогда я подумал, что хватит терпеть, буду все заметки вести в виде org-mode и маркдаун текстовых заметок. Заодно и бэкапить их будет проще -- прямо на гитхаб или еще куда.

Единственная загвоздка
----------------------

Это как воспроизвести свой рабочий процесс с этим новым инструментом? Основных проблемы две:

1. У Evernote есть мобильный клиент, и иногда было удобно на нем добавлять новые небольшие заметочки или фотографии, а так же, в случае необходимости, обращаться к старым записям. Org-mode же, как и emacs, работает только на большом компьютере. Максимум, что можно сделать, это экспортировать заметки в веб. Это в каком-то виде у меня уже сделано -- так автоматически экспортируется TODO на день, и я могу смотреть его даже с мобильника. Для всего архива заметок придется делать либо вебинтерфейс, либо простое приложение, которое позволит читать страницы в оффлайне. Пока что думаю остановиться на простой веб-версии. Может вообще генерить статику с помощью чего-то вроде mkdocs или sphinx? Пока не решил окончательно.

2. Часто я добавлял новые задания в TODO лист, отправляя email на специальный эвернотовский адрес. Эти письма попадали в специальную папку, откуда их забирал IFFT и генерил RSS. А RSS уже читал org-mode, складывая все новые записи в Inbox. Такая вот цепочка. К счастью, её довольно просто повторить, написав небольшой скриптик, который будет вычитывать новые записи по Imap из отдельной папки, и генерить локальный RSS feed.

Вывод
-----

Еще может быть отдельная проблема с поиском по заметкам. Надо поисследовать как org-mode ищет по русскоязычным текстам, и сравнить с Evernote. Но в целом, задача вполне реализуемой. И главное, все части механизма будут в моих руках.
