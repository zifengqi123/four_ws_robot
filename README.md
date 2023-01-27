# ROS-four_ws_navigation-src

## установка пакетов

<p align="center">
<img src="imgs/skelet.JPG">
</p>

```bash
cd
mkdir ~/four_ws_navigation
cd ~/four_ws_navigation
git clone https://github.com/5met4nka/ROS-four_ws_navigation-src.git
mv ROS-four_ws_navigation-src src
cd src
cp -r four_ws_stage ~/.gazebo/models
rm -r four_ws_stage
cd ..
catkin_make
cd
```

в случае использование zsh

```bash
echo "source ~/four_ws_navigation/devel/setup.zsh" >> ~/.zshrc
```

или в случает bash

```bash
echo "source ~/four_ws_navigation/devel/setup.bash" >> ~/.bashrc
```

* замечание: ROS может видеть только один ws, поэтому комментим настройку запуска других ws при помощи символа "#"

## запуск навигации

```bash
roslaunch robot_launch launch_navigation_simulation.launch
```

```bash
roslaunch navigation_params navigation.launch
```

## запуск локализации

```bash
roslaunch robot_launch launch_simulation_for_localization.launch
```

```bash
roslaunch navigation_params localization.launch
```

## запуск gmapping

```bash
roslaunch robot_launch launch_simulation_for_map_creation.launch
```

```bash
roslaunch gmapping rviz_slam_gmapping_view.launch
```
сохранение карты в файл

```bash
cd ~/four_ws_navigation/src/navigation_params/map
```

```bash
rosrun map_server map_saver -f four_ws_map
```

## параметры AMCL

[официальная документация](http://wiki.ros.org/amcl)

### общие параметры фильтра

`min_particles (int, default: 100)` - определяет минимально допустимое количество частиц

`max_particles (int, default: 5000)` - определяет максимально допустимое количество частиц

`kld_err (double, default: 0.01)` - относится к максимальному порогу ошибки, используемому в процессе выборки KLD. Процесс отбора проб KLD используется для адаптации количества частиц, используемых в алгоритме локализации по методу Монте-Карло, на основе распределения частиц. параметр "kld_err" устанавливает пороговое значение для максимально допустимой ошибки в распределении частиц. если ошибка превышает этот порог, количество частиц будет увеличено для повышения точности локализации. и наоборот, если ошибка ниже этого порога и количество частиц превышает порог "kld_z", количество частиц будет уменьшено для повышения эффективности вычислений. проще говоря, параметр kld_err используется для контроля баланса между количеством частиц и точностью локализации

`kld_z (double, default: 0.99)` - определяет порог для максимально допустимого количества частиц в измерении "z", выше которого количество частиц будет уменьшено. цель состоит в том, чтобы поддерживать достаточное количество частиц, избегая при этом их слишком большого количества, что может замедлить процесс локализации

`update_min_d (double, default: 0.2 meters)` - определяет поступательное движение, необходимое перед выполнением обновления фильтра

`update_min_a (double, default: π/6.0 radians)` - определяет вращательное движение, необходимое перед выполнением обновления фильтра

`resample_interval (int, default: 2)` - определяет количество обновлений фильтра, необходимых перед повторной выборкой

`transform_tolerance (double, default: 0.1 seconds)` - определяет максимально допустимую разницу в секундах между временем записи преобразования и временем его использования. в AMCL положение и ориентация робота оцениваются на основе данных датчиков и карты окружающей среды. предполагаемое положение и ориентация робота представлены преобразованием, которое представляет собой математическое представление положения и ориентации робота во фрейме карты. параметр transform_tolerance используется для указания того, как долго алгоритм AMCL будет продолжать использовать преобразование, прежде чем оно будет признано слишком старым и должно быть отброшено. например, если для параметра transform_tolerance установлено значение 0,1 секунды, алгоритм AMCL будет использовать только преобразования, которые были записаны в течение последних 0,1 секунды. если преобразование старше 0,1 секунды, оно будет отброшено, и алгоритм AMCL продолжит использовать последнее допустимое преобразование. это может помочь предотвратить использование алгоритмом устаревшей информации, что может привести к плохим результатам локализации. важно отметить, что для этого параметра следует установить значение, подходящее для конкретного приложения и конфигурации датчика, поскольку слишком низкое значение может привести к слишком частому удалению достоверной информации, а слишком высокое значение может привести к использованию устаревшей информации

`recovery_alpha_slow (double, default: 0.0 (disabled))` - определяет экспоненциальную скорость затухания для фильтра медленного среднего веса, используемого при принятии решения о том, когда восстанавливаться, добавляя случайные позы. Хорошим значением может быть 0,001

`recovery_alpha_fast (double, default: 0.0 (disabled))` - определяет экспоненциальную скорость затухания для фильтра быстрого среднего веса, используемого при принятии решения о том, когда восстанавливаться, добавляя случайные позы. Хорошим значением может быть 0.1

`initial_pose_x (double, default: 0.0 meters)` - определяет начальное значение позы (x), используемое для инициализации фильтра с распределением по Гауссу

`initial_pose_y (double, default: 0.0 meters)` - определяет начальное значение позы (y), используемое для инициализации фильтра с распределением по Гауссу

`initial_pose_a (double, default: 0.0 radians)` - определяет начальное значение положения (рыскание), используемое для инициализации фильтра с распределением по Гауссу

`initial_cov_xx (double, default: 0.5*0.5=0.25 meters)` - определяет начальную ковариацию позы (x*x), используемую для инициализации фильтра с распределением по Гауссу

`initial_cov_yy (double, default: 0.5*0.5=0.25 meters)` - определяет начальную ковариацию позы (y*y), используемую для инициализации фильтра с распределением по Гауссу

`initial_cov_aa (double, default: (π/12)*(π/12)=0.06854 radian)` - определяет начальную ковариацию позы (рыскание*рыскание), используемую для инициализации фильтра с распределением по Гауссу

`gui_publish_rate (double, default: -1.0 Hz)` - определяет максимальную частоту (Гц), с которой сканы и пути публикуются для визуализации, -1.0 для отключения

`save_pose_rate (double, default: 0.5 Hz)` - определяет максимальную частоту (Гц), с которой последняя оцененная позиция и ковариация сохраняются на сервере параметров в переменных ~initial_pose_* и ~initial_cov_*. эта сохраненная позиция будет использоваться при последующих запусках для инициализации фильтра. -1.0 для отключения.

`use_map_topic (bool, default: false)` - если установлено значение true, AMCL подпишется на раздел карты, а не будет выполнять вызов службы для получения своей карты

`first_map_only (bool, default: false)` - если установлено значение true, AMCL будет использовать только первую карту, на которую он подписался, вместо того, чтобы обновлять ее каждый раз при получении новой

`selective_resampling (bool, default: false)` - определяет, должен ли алгоритм AMCL использовать выборочную повторную выборку или нет. повторная выборка - это процесс, который используется в фильтре частиц, который является основным компонентом алгоритма AMCL. фильтр частиц использует набор частиц для представления возможных местоположений робота на карте. повторная выборка используется для обновления набора частиц на основе данных датчика с целью обеспечения того, чтобы частицы, соответствующие более вероятным позициям робота, имели более высокую вероятность быть выбранными. выборочная повторная выборка - это метод оптимизации, который повышает эффективность процесса повторной выборки за счет повторной выборки только тех частиц, которые вряд ли соответствуют истинному положению робота. путем повторной выборки только подмножества частиц выборочная повторная выборка может уменьшить количество частиц, которые необходимо повторно выбрать, что может повысить производительность алгоритма AMCL. если параметру selective_resampling присвоено значение true, алгоритм AMCL будет использовать выборочную повторную выборку. если для него установлено значение false, алгоритм AMCL не будет использовать выборочную повторную выборку. важно отметить, что использование выборочной повторной выборки может повысить производительность алгоритма AMCL, но это также увеличивает время вычислений. поэтому важно находить компромисс между временем вычисления и точностью при установке параметра selective_resampling

### параметры лазерной модели

`laser_min_range (double, default: -1.0)` - определяет минимальный диапазон сканирования, который следует учитывать; -1.0 приведет к использованию заявленной минимальной дальности действия лазера

`laser_max_range (double, default: -1.0)` - определяет максимальный диапазон сканирования, который следует учитывать; -1.0 приведет к использованиюзаявленной максимальной дальности действия лазера

`laser_max_beams (int, default: 30)` - определяет, сколько равномерно расположенных лучей в каждом сканировании следует использовать при обновлении фильтра

`laser_z_hit (double, default: 0.95)` - определяет ожидаемое измерение попадания (т.е. когда лазерный луч успешно обнаруживает препятствие). более высокое значение этого параметра увеличит вероятность попадания частицы, когда данные лазерного сканирования совпадут с ожидаемым измерением попадания

`laser_z_short (double, default: 0.1)` - определяет ожидаемое измерение для короткого считывания (т.е. когда лазерный луч обнаруживает препятствие до того, как он достигнет максимальной дальности). более высокое значение этого параметра увеличит вероятность обнаружения частицы, когда данные лазерного сканирования совпадут с ожидаемым измерением для короткого считывания

`laser_z_max (double, default: 0.05)` - определяет максимальную дальность действия лазерного датчика. более высокое значение этого параметра уменьшит вероятность обнаружения частицы, когда данные лазерного сканирования превысят этот диапазон

`laser_z_rand (double, default: 0.05)` - представляет вероятность случайного измерения (т.е. когда лазерный луч не обнаруживает препятствие).более высокое значение этого параметра увеличит вероятность обнаружения частицы, когда данные лазерного сканирования совпадут с ожидаемым измерением для случайного считывания

`laser_sigma_hit (double, default: 0.2 meters)` - представляет стандартное отклонение распределения Гаусса, используемого для моделирования шума при измерениях попадания. более высокое значение этого параметра увеличит диапазон возможных измерений, которые будут считаться попаданием

`laser_lambda_short (double, default: 0.1)` - определяет скорость затухания экспоненциального распределения, используемого для моделирования коротких показаний. более высокое значение этого параметра увеличит вероятность коротких показаний

`laser_likelihood_max_dist (double, default: 2.0 meters)` - этот параметр представляет максимальное расстояние, на котором модель лазерного датчика будет использоваться для вычисления вероятности обнаружения частицы. более высокое значение этого параметра увеличит диапазон, в котором будет использоваться модель датчика

---

`laser_model_type (string, default: "likelihood_field")` - относится к типу модели датчика, используемой для лазерного дальномера. модель датчика - это математическое представление характеристик датчика и того, как он взаимодействует с окружающей средой. пакет amcl поддерживает несколько различных моделей лазерных датчиков, а параметр "laser_model_type" позволяет вам выбрать, какую из них использовать. варианты таковы:

* "likelihood_field": эта модель использует поле правдоподобия для представления вероятности нахождения частицы в определенном месте на основе лазерных измерений

* "beam": в этой модели используется подход, основанный на луче, при котором каждый луч обрабатывается независимо

* "likelihood_field_prob": эта модель похожа на модель "likelihood_field", но в ней используется вероятностное представление вероятности

* "beam_model_prob": эта модель похожа на модель "beam", но в ней используется вероятностное представление вероятности

Выбор модели датчика будет зависеть от характеристик лазерного дальномера, окружающей среды и конкретных требований приложения

### параметры модели одометрии

`odom_model_type (string, default: "diff")` - относится к типу модели движения, используемой для одометрии. модель движения - это математическое представление того, как движется робот, и как на это движение влияют шум и другие факторы. пакет amcl поддерживает несколько различных моделей движения odometry, а параметр "odom_model_type" позволяет вам выбрать, какую из них использовать. варианты таковы:

• "diff": эта модель предназначена для роботов с дифференциальным приводом. Он предполагает, что движение робота состоит из прямой и угловой скоростей, и использует эти скорости для оценки положения и ориентации робота

• "omni": эта модель предназначена для всенаправленных роботов. Он использует поступательную и угловую скорости робота, а также его боковые скорости для оценки положения и ориентации робота

• "diff-corrected": Эта модель является расширением модели "diff" и использует одометрию колес и IMU для уменьшения дрейфа в одометрии.
Выбор модели движения будет зависеть от характеристик робота, окружающей среды и конкретных требований приложения

---

`odom_alpha1 (double, default: 0.2)` - определяет количество шума, которое добавляется к скорости вращения робота

`odom_alpha2 (double, default: 0.2)` - определяет количество шума, которое добавляется к скорости вращения робота

`odom_alpha3 (double, default: 0.2)` - определяет количество шума, которое добавляется к поступательному перемещению робота

`odom_alpha4 (double, default: 0.2)` - определяет уровнем шума, который добавляется к вращательному перемещению робота

`odom_alpha5 (double, default: 0.2)` - определяет количество шума, которое добавляется к поступательному ускорению робота

`odom_frame_id (string, default: "odom")` - определяет, какой фрейм использовать для одометрии

`base_frame_id (string, default: "base_link")` - определяет, какой фрейм использовать для основания робота

`global_frame_id (string, default: "map")` - определяет название системы координат, опубликованной системой локализации

`tf_broadcast (bool, default: true)` - относится к действию публикации предполагаемого положения и ориентации робота (pose) в виде сообщения "transform" в библиотеке преобразования ROS (tf). библиотека tf отвечает за поддержание связей между различными кадрами координат в системе, и она использует опубликованные преобразования для обновления положений различных кадров. параметр "tf_broadcast" - это логическое значение, которое определяет, будет ли узел amcl публиковать оценочную позу робота в библиотеке tf или нет. если установлено значение true, узел amcl опубликует оценочную позу, позволяя другим узлам использовать ее для обновления своих собственных кадров и выполнения других задач, таких как визуализация положения робота на карте. если установлено значение false, узел amcl не будет публиковать расчетную позу, и другие узлы не смогут получить к ней доступ. по умолчанию для параметра tf_broadcast установлено значение true, но можно установить для него значение false, если вы не хотите, чтобы amcl публиковал позу и использовал данные из других источников

## параметры slam_gmapping

[официальная документация](http://wiki.ros.org/gmapping)

`inverted_laser (string, default: "false")` - true если сканы формируются против часовой стрелки) или вверх ногами (false если сканы формируются по часовой стрелке)

`throttle_scans (int, default: 1)` - используется для управления скоростью, с которой лазерные сканы обрабатываются алгоритмом отображения. Он определяет количество сканирований, которые должны быть получены до повторного запуска алгоритма сопоставления. установка этого параметра на более высокое значение снизит скорость обработки алгоритма, что может быть полезно, если вычислительная мощность робота ограничена или если робот работает с высокой скоростью сканирования

`base_frame (string, default: "base_link")` - фрейм прикреплен к мобильной базе

`map_frame (string, default: "map")` - фрейм прикреплен к карте

`odom_frame (string, default: "odom")` - фрейм прикреплен к системе одометра

`map_update_interval (float, default: 5.0)` - определяет, сколько времени (в секундах) между обновлениями карты) уменьшение этого числа приводит к более частому обновлению сетки заполняемости за счет большей вычислительной нагрузки)

`maxUrange (float, default: 80.0)` - используется для установки максимального диапазона использования лазерного датчика. этот диапазон используется для исключения показаний лазера, которые бесполезны для картографирования, это может быть связано с шумом датчика или отражениями от близких препятствий. это значение задается в метрах, и показания, диапазон которых превышает это значение, игнорируются

`sigma (float, default: 0.05)` - управляет стандартным отклонением ядра Гаусса, используемого для сглаживания данных лазерного сканирования

`kernelSize (int, default: 1)` - определяет размер ядра, используемого в операции свертки. Ядро, также известное как матрица свертки или маска, представляет собой небольшую матрицу, которая используется для применения определенного эффекта или фильтра к изображению. ядро передается по изображению по одному пикселю за раз, и значение каждого пикселя в изображении умножается на соответствующее значение в ядре, и результаты суммируются. параметр kernelSize определяет размер ядра, которое может представлять собой квадратную матрицу с нечетным числом строк и столбцов, например матрицу 3x3 или 5x5. чем больше ядро, тем больше оно будет размывать изображение

---

`lstep (float, default: 0.05)` - определяет расстояние между последовательными лазерными сканированиями на карте. он используется для управления разрешением карты, при этом меньшее значение приводит к карте с более высоким разрешением, а большее значение приводит к карте с более низким разрешением

`astep (float, default: 0.05)` - определяет угол между последовательными лазерными сканированиями. он работает аналогично параметру линейного шага, управляя разрешением карты в угловом измерении

p.s. оба параметра должны быть установлены тщательно, потому что карта с высоким разрешением потребует больше вычислительной мощности и памяти, но карта с низким разрешением затруднит обнаружение небольших объектов

---

`iterations (int, default: 5)` - управляет количеством итераций для алгоритма сопоставления сканирования

`lsigma (float, default: 0.075)` - управляет стандартным отклонением распределения Гаусса, используемого в функции правдоподобия, которая используется для определения вероятности наблюдения лазерного сканирования с определенной позиции на карте. функция правдоподобия используется для сравнения данных лазерного сканирования с картой, а значение lsigma определяет, насколько данные лазерного сканирования могут отличаться от карты, прежде чем они будут считаться маловероятным совпадением. меньшее значение lsigma приведет к более строгому сравнению, а большее значение приведет к менее строгому сравнению. в lsigma важно установить правильное значение, чтобы получить хороший баланс между получением хорошего соответствия и избеганием ложных срабатываний

`ogain (float, default: 3.0)` - контролирует вес, придаваемый данным лазерного сканирования при обновлении карты. он используется для балансировки влияния данных лазерного сканирования на предыдущую информацию карты, при этом более высокое значение придает больший вес данным лазерного сканирования, а более низкое значение придает больший вес предыдущей информации карты. параметр ogain можно использовать для настройки компромисса между точностью карты и ее гладкостью. более высокое значение ogain увеличит влияние данных лазерного сканирования, что приведет к более точной, но менее гладкой карте. более низкое значение ogain уменьшит влияние данных лазерного сканирования, что приведет к менее точной, но более гладкой карте. важно найти баланс между точностью и плавностью отображения карты в зависимости от варианта использования, датчика и окружающей среды.

`lskip (int, default: 0)` - используется для управления скоростью, с которой лазерные сканы обрабатываются алгоритмом отображения. он определяет количество сканирований, которые будут пропущены до обработки следующего сканирования. установка этого параметра на более высокое значение приведет к снижению скорости обработки сканирований, что может быть полезно, если вычислительная мощность робота ограничена или если робот работает с высокой скоростью сканирования. этот параметр может использоваться для управления вычислительной нагрузкой алгоритма и для повышения надежности алгоритма в средах с высокой скоростью сканирования или высоким уровнем шума. важно отметить, что увеличение параметра lskip также приведет к уменьшению разрешения карты, что сделает ее менее точной и менее плавной. он должен быть сбалансирован с другими параметрами, такими как lstep, astep, lsigma и ogain

`minimumScore (float, default: 0.0)` - устанавливает пороговое значение для оценки вычисленных поз, которое используется для определения качества картографического решения. оценка - это показатель того, насколько хорошо текущая карта совпадает с новыми данными лазерного сканирования. его можно использовать для фильтрации плохих поз или снимков низкого качества. более высокое значение minimumScore приведет к более строгим критериям приемлемости для вычисленных поз, а более низкое значение приведет к менее строгим критериям приемлемости. это означает, что если для параметра minimumScore установлено высокое значение, будут приниматься только позы с очень высоким баллом, а если для него установлено низкое значение, будут приниматься даже позы с низким баллом. его можно использовать для фильтрации плохих поз или снимков низкого качества, но он также будет отфильтровывать хорошие позы. он должен быть установлен тщательно, чтобы гарантировать, что отображение является надежным и точным

---

следующие параметры, используемые в модели движения сканера сопоставления, и они управляют неопределенностью движения. параметры srr, srt, str и stt используются в модели движения алгоритма сопоставления сканирования. эти параметры контролируют неопределенность движения робота и используются для моделирования погрешности в измерениях одометрии. эти параметры задаются в метрах или радианах, и их следует корректировать в зависимости от конкретного варианта использования и погрешности системы одометрии робота. например, если система одометрии робота имеет высокую погрешность при вращении вокруг оси x, значение srr следует увеличить. аналогично, если система одометрии робота имеет высокую погрешность при перемещении вдоль осей x, y и z, значение stt следует увеличить. важно отметить, что увеличение значений этих параметров увеличит пространство поиска средства сопоставления сканирования, что приведет к более медленному сопоставлению сканирования, но также увеличит шансы найти правильное соответствие. в то время как уменьшение значений этих параметров приведет к уменьшению пространства поиска средства сопоставления сканирования, что приведет к более быстрому сопоставлению сканирования, но также уменьшит шансы найти правильное совпадение.

`srr (float, default: 0.1)` - управляет неопределенностью вращения вокруг оси x

`srt (float, default: 0.2)` - управляет неопределенностью вращения вокруг оси y

`str (float, default: 0.1)` - управляет неопределенностью вращения вокруг оси z

`stt (float, default: 0.2)` - управляет неопределенностью перемещения вдоль осей x, y и z

---

`linearUpdate (float, default: 1.0)` - минимальное расстояние (в метрах), на которое может переместиться робот, не обновив карту

`angularUpdate (float, default: 0.5)` - минимальное угол (в радианах), на которое может переместиться робот, не обновив карту

`temporalUpdate (float, default: -1.0)` - время, за которое карта обновится, даже если робот не совершал перемещения

`resampleThreshold (float, default: 0.5)` - используется для управления величиной повторной выборки, которая выполняется, когда поза робота неопределенна. этот параметр представляет собой пороговое значение для расстояния между предполагаемым положением робота и положением, определенным на карте. если расстояние превышает этот порог, карта будет повторно выбрана для лучшего согласования с предполагаемым положением робота. пороговое значение должно быть установлено на значение, соответствующее конкретным датчикам робота и возможностям локализации. более низкие значения приведут к более частой повторной выборке, что может повысить точность карты, но также увеличить вычислительные затраты. высокие значения приведут к менее частой повторной выборке, что может снизить вычислительные затраты, но также снизить точность карты

`particles (int, default: 30)` - управляет количеством частиц, используемых в алгоритме фильтрации частиц. алгоритм фильтрации частиц - это метод, используемый для оценки позы робота (положения и ориентации) на основе данных датчиков. каждая частица представляет возможное состояние робота, и алгоритм фильтрации частиц использует набор частиц для представления распределения вероятностей по возможным состояниям робота. чем больше частиц используется, тем точнее будет оцененная поза робота, однако большое количество частиц увеличит вычислительные затраты. меньшее количество частиц уменьшит вычислительные затраты, но также снизит точность предполагаемой позы робота. в общем, число частиц должно быть установлено достаточно высоким, чтобы гарантировать правильную выборку распределения вероятностей по возможным состояниям робота, но не настолько высоким, чтобы вычислительные затраты становились непомерно высокими. как правило, в большинстве приложений gmapping используются значения от 100 до 1000 частиц

---

следующие парметры используются для указания размера сетки карты и определения разрешения карты

`xmin (float, default: -100.0)` - начальный размер карты (в метрах) по оси x

`ymin (float, default: -100.0)` - начальный размер карты (в метрах) по оси у

`xmax (float, default: 100.0)` - начальный размер карты (в метрах) по оси x

`ymax (float, default: 100.0)` - начальный размер карты (в метрах) по оси у

---

`delta (float, default: 0.05)` - используется для управления степенью детализации создаваемой карты. он представляет размер ячеек в сетке карты в метрах. меньшее значение для дельты приведет к более подробной и точной карте, но также увеличит вычислительные затраты и использование памяти. большее значение для дельты приведет к менее подробной и менее точной карте, но также снизит вычислительные затраты и использование памяти. обычно он устанавливается на значение, соответствующее возможностям датчика робота и локализации, а также размеру отображаемой среды. стоит отметить, что значение дельты также влияет на разрешение карты, меньшая дельта создаст более подробную карту, но роботу потребуется больше данных с датчиков, чтобы охватить ту же область

---

следующие параметры используются для управления выборкой данных лазерного датчика в процессе отображения В системе ROS (Robot Operating System) параметр ll sample range используется для указания дальности действия лазерного сканера (также известного как LIDAR) при использовании пакета laser_scan_matcher. Этот пакет выполняет согласование сканирования, которое представляет собой метод, используемый для выравнивания двух лазерных сканирований путем сведения к минимуму разницы между ними. Параметр llsamplerange используется для указания диапазона показаний лазерного сканера, который будет использоваться в процессе сопоставления сцен

`llsamplerange (float, default: 0.01)` - для управления диапазоном данных линейного лазерного датчика

`llsamplestep (float, default: 0.01)` - для управления размером шага данных линейного лазерного датчика

`lasamplerange (float, default: 0.005)` - для управления диапазоном данных углового лазерного датчика

`lasamplestep (float, default: 0.005)` - для управления размером шага данных углового лазерного датчика

---

`transform_publish_period (float, default: 0.05)` - используется для управления частотой публикации преобразования карты. преобразование карты - это матрица преобразования, которая описывает взаимосвязь между фреймом карты и базовым фреймом робота. значение этого параметра задается в секундах, оно представляет период времени между последовательными публикациями преобразования карты. эта информация используется другими узлами в системе ROS для выравнивания карты с данными одометрии робота и датчиков. по умолчанию преобразование публикуется со скоростью данных датчика, если для этого параметра установлено значение больше 0, это ограничит скорость публикации преобразования. это может быть полезно для снижения вычислительных затрат и использования памяти, например, если робот движется с низкой скоростью, нет необходимости обновлять преобразование карты очень часто. важно отметить, что если период установлен слишком высоко, это может привести к отклонению карты от истинного положения робота и снижению точности карты

`occ_thresh (float, default: 0.25)` - пороговое значение, используемое для определения того, занята ячейка на карте или нет

`maxRange (float)` - используется для установки максимальной дальности действия лазерного датчика, используемого для картографирования. это значение также задается в метрах, и показания, диапазон которых превышает это значение, игнорируются

*** Таким образом, параметр "maxUrange" используется для исключения показаний лазера, которые бесполезны для отображения, поскольку они находятся слишком далеко от датчика или потому, что они являются отражениями, в то время как параметр "maxRange" используется для исключения показаний лазера, которые находятся за пределами максимального диапазона датчика, который следует использовать для отображения ***
