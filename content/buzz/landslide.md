Title: Презентация из Markdown/ReST
Slug: landslide
Date: 2010-12-09 08:53
Category: reviews
Tags: python, tools
Lang: ru

Как сделать презентацию из Markdown или ReST документа? Легко!

Парень с фамилией, прямо как из книг Терри Праттчета, Адам Заплетал,
написал на питончике [конвертор][Landslide], который берет один или несколько документов в
формате Markdown или ReST. И компилирует из них HTML5 презентацию.

На самом деле, контрибьюторов у этого проекта много больше, да и написан он не
с нуля, а основывается на шаблоне Марчина Вичери (юзабелиста из Google). Есть
такой проект: [http://slides.html5rocks.com/][1] полагаю, он и является
прототипом [Landslide][Landslide].

![](http://adamzap.com/random/landslide.png)

Я установил себе этот пакетик в virtualenv и немного поигрался. Могу с
уверенностью сказать — последний раз я был в таком восторге от инструмента
обработки текстов, когда открыл для себя LaTeX!

Одним из положительных моментов подобного способа создания презентации, я
считаю то, что тот же самый документ можно читать как обычный текст, или,
например, сгенерировать из него PDF, что, кстати Landslide тоже умеет.

P.S. — и что особенно приятно, в презентацию можно встраивать код и он будет
симпатично подсвечен согласно синтаксису используемого языка.

[1]: http://slides.html5rocks.com/
[Landslide]: http://adamzap.com/random/landslide.html