# Code

Source code for the paper on the data-complexity measure $C(X) = \log\det(I+K)$ based on score func and heat kernel.

## Layout

```
code/
├── kernels/                  # Общий пакет, используемый exp3 и exp4
│   ├── __init__.py
│   ├── berry_sauer.py        # L_eps^sym по матрице d^2 (Theorem 4.7)
│   ├── score_metric.py       # g(x) = (I + s s^T)^{-1}, d_g^2(X)
│   ├── heat.py               # discrete_heat_kernel, поточечная нормализация
│   └── complexity.py         # complexity, t_spectral, t_median
├── experiments/              # Jupyter notebooks с экспериментами
│   ├── exp1.ipynb            # Базовые свойства C(X) на S^2: аналитика, верх/нижние
│   │                         # границы, эксперимент D (рост C(N)), субаддитивность
│   │                         # и субмодулярность.
│   ├── exp2.ipynb            # Дискретный Лапласиан Berry–Sauer (Theorem 4.7) против
│   │                         # аналитики на S^2: спектр, калибровка c, C(t), C(N).
│   ├── exp3.ipynb            # Чувствительность C(X) к разделимости кластеров.
│   │                         # Гауссовская смесь в R^2, теоретический score,
│   │                         # Berry–Sauer на score-индуцированной метрике,
│   │                         # проверка блочно-диагональной асимптотики.
│   ├── exp4.ipynb            # Зашумленный тор с двумя кластерами в R^3, score из diffusion-модели,
│   │                         # сравнение евклидовой и score-индуцированной метрик.
│   └── exp5.ipynb            # (Two-Moons / MNIST / CIFAR-10), пока не реализовано.
│                             
├── requirements.txt
└── README.md
```

## Installation

```bash
cd code
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python -m ipykernel install --user --name iad-211 --display-name "Python (iad-211)"
```

## Usage

Запуск ноутбуков по очереди:

```bash
cd code
source .venv/bin/activate
jupyter notebook experiments/
```

Все сиды зафиксированы; графики и числовые результаты должны воспроизводиться.

Чтобы перезапустить все клетки:

```bash
jupyter nbconvert --to notebook --execute --inplace experiments/exp1.ipynb
jupyter nbconvert --to notebook --execute --inplace experiments/exp2.ipynb
jupyter nbconvert --to notebook --execute --inplace experiments/exp3.ipynb
jupyter nbconvert --to notebook --execute --inplace experiments/exp4.ipynb
```
