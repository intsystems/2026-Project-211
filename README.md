# Data Complexity via Data Geometry Using Generative Models

<!-- Change `kisnikser/m1p-template` to `intsystems/your-repository`-->
[![License](https://badgen.net/github/license/kisnikser/m1p-template?color=green)](https://github.com/kisnikser/m1p-template/blob/main/LICENSE)
[![GitHub Contributors](https://img.shields.io/github/contributors/kisnikser/m1p-template)](https://github.com/kisnikser/m1p-template/graphs/contributors)
[![GitHub Issues](https://img.shields.io/github/issues-closed/kisnikser/m1p-template.svg?color=0088ff)](https://github.com/kisnikser/m1p-template/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr-closed/kisnikser/m1p-template.svg?color=7f29d6)](https://github.com/kisnikser/m1p-template/pulls)

<table>
    <tr>
        <td align="left"> <b> Author </b> </td>
        <td> Kirill Zolotarev </td>
    </tr>
    <tr>
        <td align="left"> <b> Consultant </b> </td>
        <td> Danila Chernousov </td>
    </tr>
    <tr>
        <td align="left"> <b> Advisor </b> </td>
        <td> Andrey Grabovoy, PhD </td>
    </tr>
</table>

## Assets

- [LinkReview](LINKREVIEW.md)
- [Code](code)
- [Paper](paper/main.pdf)
- [Slides](slides/main.pdf)

## Abstract

Оценка сложности данных — актуальная проблема анализа данных. Существующие методы часто предполагают линейное масштабирование сложности с размером выборки, но этот подход не учитывает внутреннюю структуру данных, лежащих на многообразиях. Для того, чтобы найти меру сложности данных предлагается использовать свойства диффузионных моделей, с помощью которых можно восстановить геометрию распределения. Новизна заключается в отказе от линейного предположения и анализе сложности на основе таких характеристик многообразия, как локальная размерность и кривизна. Метод позволяет корректно сравнивать сложность датасетов (например, MNIST и CIFAR-10), показывая, например, что дублирование точек не увеличивает сложность. А генеративные модели уже работают вблизи её верхней границы.

## Citation

If you find our work helpful, please cite us.
```BibTeX
@article{citekey,
    title={Title},
    author={Name Surname, Name Surname (consultant), Name Surname (advisor)},
    year={2025}
}
```

## Licence

Our project is MIT licensed. See [LICENSE](LICENSE) for details.
