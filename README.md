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

Data complexity estimation is a relevant problem in data analysis. Existing methods often assume linear scaling of complexity with sample size, but this approach fails to account for the intrinsic structure of data lying on manifolds. To derive a measure of data complexity, we propose leveraging the properties of diffusion models, which can be used to recover the geometry of the data distribution. The novelty lies in abandoning the linear assumption and analyzing complexity based on manifold characteristics such as local dimension and curvature. The proposed method enables meaningful comparison of dataset complexity (e.g., MNIST vs. CIFAR-10), demonstrating, for instance, that duplicating points does not increase complexity. Furthermore, generative models already operate near its upper bound.

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
