# seriexn — Soma Parcial (Partial Summation)

**Python code for checking convergence of the "soma xn" series via partial sums.**

[![Python](https://img.shields.io/badge/Python-3.12-blue)]()
[![Status](https://img.shields.io/badge/Status-Research%2FExploration-informational)]()

---

## What it does

Computes the **partial sums** of the series Σ(1/xₙ) to numerically check whether the series converges or diverges.

- **Input:** number of terms (`tamanho`) and starting index (`indice`)
- **Computation:** for each term xₙ from `indice` to `tamanho`, computes 1/xₙ and accumulates the partial sum
- **Output:** list of partial sums → `lista.txt`

The partial sums are printed and saved, allowing direct numerical verification of convergence behavior.

## Files

| File | Description |
|---|---|
| `soma-parcial.py` | Main script — computes partial sums of Σ(1/xₙ), writes `lista.txt` |
| `soma-parcial.ipynb` | Jupyter notebook — exploratory version with notebook cells |
| `soma-parcial-v2.ipynb` | v2 notebook iteration |
| `soma-parcial-v3.ipynb` | v3 notebook iteration |
| `soma-parcial-v3-1.ipynb` | v3-1 notebook iteration (latest) |
| `lista.txt` | Output — accumulated partial-sum values |

## How to run

```bash
python soma-parcial.py
```

The script prompts for:
1. **Número de parcelas** (`tamanho`) — number of terms in the series
2. **Índice inicial** (`indice`) — starting index

Results are appended to `lista.txt`.

## Mathematical background

The "soma xn" series is the sequence of partial sums of 1/xₙ — a harmonic-type series. By computing partial sums numerically, this project verifies convergence behavior: the partial sums either stabilize (converge) or grow without bound (diverge).

## Version history

- **v1** (`soma-parcial.py`, `soma-parcial.ipynb`) — initial implementation
- **v2** (`soma-parcial-v2.ipynb`) — notebook refinement
- **v3** (`soma-parcial-v3.ipynb`) — structure improvement
- **v3-1** (`soma-parcial-v3-1.ipynb`, `soma-parcial-v3-1.py`) — final cleaned version

## Notes

- Exploratory / research project (Jupyter notebook workflow)
- Header adapted from the `inset/intset` repository
- Demonstrates numerical series analysis and convergence checking
