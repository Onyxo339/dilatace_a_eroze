# dilatace_a_eroze_md

- Generace md tabulky ze zadaného vstupu

## Kód_na_md_tabulku
- Vytvořil jsem funkci, která má zadaný field.
- Dále jsem udělala, že vezmu první řádek změním každý element na string a spojím je s " | ".
- Jako další jsem přidal "|---" podle počtu sloupců pro vytvoření kompletní tabulky.
```
    md = "| " + " | ".join(str(i) for i in field[0]) + " |" + "\n"
    md += "|---" * len(field) + "|" + "\n"
```

| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 |
| 0 | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 0 |
| 0 | 1 | 2 | 3 | 3 | 3 | 2 | 1 | 0 |
| 0 | 1 | 2 | 3 | 4 | 3 | 2 | 1 | 0 |
| 0 | 1 | 2 | 3 | 3 | 3 | 2 | 1 | 0 |
| 0 | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 0 |
| 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
