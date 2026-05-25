# Lead-Lag Forecasting (LLF) on Social Platforms

Official repository for the paper *Benchmark Datasets for Lead-Lag Forecasting on Social Platforms*.

**Data portal**: [lead-lag-forecasting.github.io](https://lead-lag-forecasting.github.io/)

## Abstract

Social and collaborative platforms emit multivariate time-series traces in which early interactions — such as views, likes, or downloads — are followed, sometimes months or years later, by higher-impact outcomes like citations, sales, or reviews. We formalize this setting as **Lead-Lag Forecasting (LLF)**: given an early usage channel (the *lead*), predict a correlated but temporally shifted outcome channel (the *lag*). We present two high-volume benchmark datasets — **ArXiv** (accesses → citations, 2.3M papers) and **GitHub** (pushes/stars → forks, 3M repositories) — and benchmark parametric and non-parametric baselines for regression.

## Repository Structure

This repository is organized into two submodules:

```
├── ellf/          # Parametric baselines (MLP, LSTM, Transformer)
├── Time-MoE/      # Time-MoE foundation model embedding extraction + KNN ablation
└── figures/        # Paper figure generation scripts
```

| Submodule | Description | Repository |
|---|---|---|
| **ellf** | Trains MLP, LSTM, and Transformer baselines on LLF datasets with W&B experiment tracking | [kimzemian/LLF-Training](https://github.com/kimzemian/LLF-Training) |
| **Time-MoE** | Extracts embeddings from a pretrained Time-MoE model and evaluates via KNN ablation | [kimzemian/Time-MoE-LLF](https://github.com/kimzemian/Time-MoE-LLF) |

## Datasets

| Dataset | Lead signal | Lag signal | Scale |
|---|---|---|---|
| ArXiv | Accesses | Citations | 2.3M papers |
| GitHub | Pushes / Stars | Forks | 3M repositories |

Datasets are available for download at the [data portal](https://lead-lag-forecasting.github.io/).

## Getting Started

```bash
git clone --recurse-submodules https://github.com/kimzemian/LLF.git
cd LLF
```

See each submodule's README for setup and usage instructions:
- [`ellf/README.md`](ellf/README.md) — Baseline model training
- [`Time-MoE/README.md`](Time-MoE/README.md) — Embedding extraction and KNN evaluation

## Citation

```bibtex
@article{kazemian2025benchmark,
  title={Benchmark Datasets for Lead-Lag Forecasting on Social Platforms},
  author={Kazemian, Kimia and Liu, Zhenzhen and Yang, Yangfanyu and Luo, Katie Z and Gu, Shuhan and Du, Audrey and Yang, Xinyu and Jansons, Jack and Weinberger, Kilian Q and Thickstun, John and Yin, Yian and Dean, Sarah},
  journal={arXiv preprint arXiv:2511.03877},
  year={2025}
}
```
