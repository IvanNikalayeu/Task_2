# Task_2 Pandas
Датасет собран из базы данных переписи 1994 года и содержит данные о доходах.
Информация о данных:

age: continuous.

workclass: Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked.

fnlwgt: continuous.

education: Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, * Masters,
1st-4th, 10th, Doctorate, 5th-6th, Preschool.

education-num: continuous.

marital-status: Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, 
Married-AF-spouse.

occupation: Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, 
Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces.

relationship: Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried.

race: White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black.

sex: Female, Male.

capital-gain: continuous.

capital-loss: continuous.

hours-per-week: continuous.

native-country: United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, 
Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, 
Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, 
Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands.

salary: >50K,<=50K

Проведите анализ данных при помощи Pandas выполнив поставленные задачи.

1. Посчитайте, сколько мужчин и женщин (признак sex) представлено в этом датасете
2. Каков средний возраст мужчин (признак age) по всему датасету?
3. Какова доля граждан Соединенных Штатов (признак *native-country*)?
4. Рассчитайте среднее значение и среднеквадратичное отклонение возраста тех, кто получает 
более 50K в год (признак salary) и тех, кто получает менее 50K в год
5. Правда ли, что люди, которые получают больше 50k, имеют минимум высшее образование?
(признак education – Bachelors, Prof-school, Assoc-acdm, Assoc-voc, Masters или Doctorate)
6. Выведите статистику возраста для каждой расы (признак race) и каждого пола. Используйте groupby и describe. 
Найдите таким образом максимальный возраст мужчин расы Asian-Pac-Islander.
7. Среди кого больше доля зарабатывающих много (>50K): среди женатых или холостых мужчин (признак marital-status)? 
Женатыми считаем тех, у кого marital-status начинается с Married 
(Married-civ-spouse, Married-spouse-absent или Married-AF-spouse), остальных считаем холостыми.
8. Какое максимальное число часов человек работает в неделю 
(признак hours-per-week)? Сколько людей работают такое количество часов и каков среди них процент зарабатывающих много?
9. Посчитайте среднее время работы (hours-per-week) зарабатывающих мало и много (salary) 
для каждой страны (native-country).
10. Сгруппируйте людей по возрастным группам young, adult, retiree, где:
young соответствует 16-35 лет
adult - 35-70 лет
retiree - 70-100 лет
Проставьте название соответсвтуещей группы для каждого человека в новой колонке AgeGroup
11. Определите количество зарабатывающих >50K в каждой из возрастных групп (колонка AgeGroup), 
а также выведите название возрастной группы, в которой чаще зарабатывают больше 50К (>50K)
12. Сгруппируйте людей по типу занятости (колонка occupation) и определите количество людей в каждой группе. 
После чего напишите функциюю фильтрации filter_func, которая будет возвращать только те группы, 
в которых средний возраст (колонка age) не больше 40 и в которых все работники отрабатывают 
более 5 часов в неделю (колонка hours-per-week)


# Task_2 NumPy

1. Дан случайный массив, поменять знак у элементов, значения которых между 3 и 8
2. Заменить максимальный элемент случайного массива на 0
3. Построить прямое произведение массивов (все комбинации с каждым элементом). На вход подается двумерный массив
4. Даны 2 массива A (8x3) и B (2x2). Найти строки в A, которые содержат элементы из каждой строки в B, независимо от порядка элементов в B
5. Дана 10x3 матрица, найти строки из неравных значений (например строка [2,2,3] остается, строка [3,3,3] удаляется)
6. Дан двумерный массив. Удалить те строки, которые повторяются
Для каждой из следующих задач (1-5) нужно привести 2 реализации – одна без использования numpy (cчитайте, что там, где на входе или выходе должны быть numpy array, будут просто списки), а вторая полностью векторизованная с использованием numpy (без использования питоновских циклов/map/list comprehension).
Замечание 1. Можно считать, что все указанные объекты непустые (к примеру, в задаче 1 на диагонали матрицы есть ненулевые элементы).
Замечание 2. Для большинства задач решение занимает не больше 1-2 строк.
7. Задача 1: Подсчитать произведение ненулевых элементов на диагонали прямоугольной матрицы. Например, для X = np.array([[1, 0, 1], [2, 0, 2], [3, 0, 3], [4, 4, 4]]) ответ 3.
8. Задача 2: Даны два вектора x и y. Проверить, задают ли они одно и то же мультимножество. Например, для x = np.array([1, 2, 2, 4]), y = np.array([4, 2, 1, 2]) ответ True.
9. Задача 3: Найти максимальный элемент в векторе x среди элементов, перед которыми стоит ноль. Например, для x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0]) ответ 5.
10. Задача 4: Реализовать кодирование длин серий (Run-length encoding). Для некоторого вектора x необходимо вернуть кортеж из двух векторов одинаковой длины. Первый содержит числа, а второй - сколько раз их нужно повторить. Например, для x = np.array([2, 2, 2, 3, 3, 3, 5]) ответ (np.array([2, 3, 5]), np.array([3, 3, 1])).
11. Задача 5: Даны две выборки объектов - X и Y. Вычислить матрицу евклидовых расстояний между объектами. Сравните с функцией scipy.spatial.distance.cdist по скорости работы.
Задача 6: CrunchieMunchies *
Вы работаете в отделе маркетинга пищевой компании MyCrunch, которая разрабатывает новый вид вкусных, полезных злаков под названием CrunchieMunchies.
Вы хотите продемонстрировать потребителям, насколько полезны ваши хлопья по сравнению с другими ведущими брендами, поэтому вы собрали данные о питании нескольких разных конкурентов.
Ваша задача - использовать вычисления Numpy для анализа этих данных и доказать, что ваши СrunchieMunchies - самый здоровый выбор для потребителей.
12. Просмотрите файл cereal.csv. Этот файл содержит количества калорий для различных марок хлопьев. Загрузите данные из файла и сохраните их как calorie_stats.
13. В одной порции CrunchieMunchies содержится 60 калорий. Насколько выше среднее количество калорий у ваших конкурентов?
Сохраните ответ в переменной average_calories и распечатайте переменную в терминале
14. Корректно ли среднее количество калорий отражает распределение набора данных? Давайте отсортируем данные и посмотрим.
Отсортируйте данные и сохраните результат в переменной calorie_stats_sorted. Распечатайте отсортированную информацию
15. Похоже, что большинство значений выше среднего. Давайте посмотрим, является ли медиана наиболее корректным показателем набора данных.
Вычислите медиану набора данных и сохраните свой ответ в median_calories. Выведите медиану, чтобы вы могли видеть, как она сравнивается со средним значением.
16. В то время как медиана показывает, что по крайней мере половина наших значений составляет более 100 калорий, было бы более впечатляюще показать, что значительная часть конкурентов имеет более высокое количество калорий, чем CrunchieMunchies.
Рассчитайте различные процентили и распечатайте их, пока не найдете наименьший процентиль, превышающий 60 калорий. Сохраните это значение в переменной nth_percentile.
17. Хотя процентиль показывает нам, что у большинства конкурентов количество калорий намного выше, это неудобная концепция для использования в маркетинговых материалах.
Вместо этого давайте подсчитаем процент хлопьев, в которых содержится более 60 калорий на порцию. Сохраните свой ответ в переменной more_calories и распечатайте его
18. Это действительно высокий процент. Это будет очень полезно, когда мы будем продвигать CrunchieMunchies. Но один вопрос заключается в том, насколько велики различия в наборе данных? Можем ли мы сделать обобщение, что в большинстве злаков содержится около 100 калорий или разброс еще больше?
Рассчитайте величину отклонения, найдя стандартное отклонение, Сохраните свой ответ в calorie_std и распечатайте на терминале. Как мы можем включить эту ценность в наш анализ?
19. Напишите короткий абзац, в котором кратко изложите свои выводы и то, как, по вашему мнению, эти данные могут быть использованы в интересах Mycrunch при маркетинге CrunchieMunchies.
