#PyLearn - Machine Larning Library
Библиотека предоставяща модули в които са имплементирани machine learning алгоритми (подобна на а scikit-learn)

##Backlog
 - Линейна регресия (със и без регуляризация)
 - Логистична регресия (със и без регуляризация)
 - Support vector machine
 - Decision trees (nice to have)
 - Невронна мрежа (nice to have)
 - Random forrest (nice to have)
 - Feature scaling (отделен модул за preprocessing на входните данни)
 - Автоматично избиране на learning rate (nice to have)
 - Модул за визуализация данните и функциите които библиотеката е "оптимизирала" (nice to have)
 - Оптимизация на произволен модел*

Задачите отбелязани с nice to have се надявам да мога да имплементирам, но очаквам да не успея.

##Оптимизация на произволен модел
 - Приема
   - модел (инстанция на клас имащ метода predict())
   - примерни входни данни за predict функцията
   - примерни изходни данни за predict функцията
 - Връща
   - сотйнсти на пропъртитата на модела за които функцията predict най-добре приближава примерните данни.

Предполагам че този модул ще работи по бавно от останалите, но предоставя доста удобен интерфейс и ще е удобен за тестване.

##3rd party модули
 - Numpy (за бърза работа с матрици)
 - Matplotlib
