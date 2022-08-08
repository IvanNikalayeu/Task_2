# Task_2
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