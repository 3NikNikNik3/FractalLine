# FractalLine 
### Python 3.11

## О мини-проекте

С его помощью можно сделать и посмотреть состоящий из линий фрактал.

Можно посмотреть фрактал в окне с анимацией перехода или сделать картинку или видео

## Примеры

https://github.com/3NikNikNik3/FractalLine/assets/161970751/d80c84fc-cb24-4305-b868-78e329b1f671

```main.py setting/90ang.json 500 500 video example/ex1.mp4 6 1 60```

![image](example/ex2.png)

```main.py setting/max.json 400 400 window 0.5```

![image](example/ex3.png)

```main.py setting/spiral.json 400 400 window 0.5```

## Об алгоритме построения

Изначально есть прямая. В каждую итерацию каждая прямая делится на несколько новых, и их концы перемещяются по правилу:

1) поворачиваем угол ходьбы (изначально как у прямой)
2) идём на часть длины изначальной прямой

## О настройках

Формат файла настроек - json, они хранятся в setting (не обязательно)

В ```setting/min.json``` показаны минимальные параметры, а в ```setting/max.json``` то же самое, но со всеми параметрами. В них можно ознакомится со структурой

Список всех параметров:

- ```start``` и ```end``` - начальное положение прямой (0.0 - 1.0)
- ```alg``` - алгоритм построения новых прямых, список объектов для каждой новой линии
- ```alg/ang``` - угол поворота направления движения в углах
- ```alg/len``` - длина прохода (в длине изначальной прямой)
- ```r``` - ширина прямой отрисовки
- ```color``` - цвет прямой (фон - \[255, 255, 255\])
- ```auto_end``` - когда делятся прямые, добавить ли точку в конец прямой (закреплённую)
- ```end_len``` - длина последней прямой (в доле от изначальной прямой) (используется при ```auto_end``` = true) (нужен для анимации)

## Как запустить

Через консоль (Linux, Window)

Чтобы узнать как, введите ```main.py help``` ._.

## Пару примеров

В setting находятся различные настройки, попробуйте :-)

В example/example.png красивое)

```main.py setting/max.json 400 400 window 1```

```main.py setting/min.json 400 400 window 0.1```

```main.py setting/what2.json 400 400 screenshot 10 res.png```
