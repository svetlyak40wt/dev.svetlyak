Title: Следите за Release Notes приложений на AppStore
Slug: tracking-appstore
Date: 2015-03-04 10:00
Category: texts
Tags: allmychanges, ios, appstore
Lang: ru

Минувшей ночью, я запилил крутую финчу на [AllMyChanges][]. Но предпосылкой к тому, стало то, что некоторое время назад был произведен серьезный рефакторинг кодобазы. Тот рефакторинг позволял легко и просто добавлять новые источники ченьджлогов (можно, я буду дальше называть их летописями?), и парсеры. Качатели летописей и их парсеры, в [AllMyChanges][] никак не связаны, а сам процесс организован с помощью конвеера, куда подается изначальный URL, а на выходе мы получаем описания версии.

Важно то, что вся эта машинерия позволяет легко расширять область действия сервиса. И вот на днях, я увидел на [stackoverflow вопрос][st-question]: "могу ли я как-то отслеживать развитие iOS приложения, не устанавливая его на устройство?" Вопрос остался без ответа, но я подумал: "Ведь наверняка у AppStore есть API, позволяющий показывать раздел «что нового» при обновлении приложения! Так почему бы не собирать летопись приложения, используя это API???"

Сказано — сделано. Или нет, не так! Быстро сказка сказывается, да не быстро дело делается.

Простенький API у AppStore есть, и прототип новой фичи был готов уже через полчаса. Но оказалось, что ручка отдает только описание последней версии приложения, а способа вытащить всю летопись – нет. Но хочется же, чтобы все было по уму!

Спустя пару часов [анализа и ковыряния в AppStore][https-proxy], у меня появился второй прототип, который и был выкачен в прод. К сожалению, он теперь использует не только API, a еще и немного regexp магии, чтобы вынимать данные из html.

Но с точки зрения пользователя, работает все очень просто.

Через контекстное меню:

![](https://img-fotki.yandex.ru/get/15567/13558447.f/0_b2c7f_9910ce74_M.png)

Или дропдаун:

![](https://img-fotki.yandex.ru/get/5110/13558447.f/0_b2c7e_55b034ce_L.png)

Выбираем пункт меню "Copy Link".

Затем открываем [AllMyChanges][], вставляем URL в строку поиска и жмем SEARCH.

Сервис сам скачает летопись приложения и предложит начать отслеживать её.

Вот так все просто.  
Полагаю, следующие на очереди – Debian/Ubuntu пакеты, надо кому?

[AllMyChanges]: http://allmychanges.com
[st-question]: http://stackoverflow.com/questions/24838765/app-store-api-for-release-notes-updates
[https-proxy]: http://www.cocoanetics.com/2010/12/how-to-spy-on-the-web-traffic-of-any-app/
