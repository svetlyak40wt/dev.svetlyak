Ну смотри. Обычно я при отладке чего-либо, запускаю tail … | grep ERROR.

Затем, если вижу интересующую меня ошибку, то порой вынужден отдельно запускать less мой-замечательный.log,  чтобы посмотреть DEBUG или INFO сообщения, предшествующие заинтересовавшему ERROR.

Это неудобно.

Куда проще было бы иметь одну программу, которая бы по дефолту показывала записи уровня ERROR, но позволяла бы тут же увеличить детализацию и почитать DEBUG/INFO сообщения тоже.

А историю надо хранить потому, что записи, предшествующие ERROR, уже в прошлом.

Александр Артёменко
сегодня, 16:37
Конечно, эта проблема во многих случаях решается с помощью CrossFinger логгера. Но иногда есть необходимость писать в лог с максимальной подробностью, а не только в случае каких либо ошибок.
