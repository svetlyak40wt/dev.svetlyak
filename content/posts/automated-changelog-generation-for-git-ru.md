Title: Автогенерация ChangeLog файла из GIT, SVN and CVS
Slug: automated-changelog-generation-for-git
Date: 2008-10-22 06:15
Tags: tools,git,cvs,svn
Category: texts
Lang: ru
Description: Устали писать ChangeLog? Используйте правильные инструменты, и ваши волосы станут гладкими и шелковистыми.

Сегодня я решил создать ChangeLog для одного из моих проектов, и начал искать решение для автоматизации этого процесса. Раньше я использовал скрипт [cvs2cl][1], но оказалось, что похожие инструменты есть и для Git.

Погуглив несколько минут, я нашел утилитку gitlog-to-changelog в пакете gnulib. Вот ссылка на скачивание [gitlog-to-changelog из репозитория gnulib][2].

Просто скачайте скрипт и разместите где-нибудь в PATH. И не забудьте сделать этот Perl скрипт исполняемым. Кроме того, необходима последняя версия Git. Я обнаружил, что подойдет любая версия выше 1.5.3.

Также, вы можете заинтересоваться подобным инструментом для SVN. Он называется [svn2log][3].

   [1]: http://www.red-bean.com/cvs2cl/
   [2]: http://git.savannah.gnu.org/gitweb/?p=gnulib.git;a=blob_plain;f=build-aux/gitlog-to-changelog;hb=HEAD
   [3]: http://www.core.com.pl/svn2log/
