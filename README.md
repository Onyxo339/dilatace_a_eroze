# dilatace_a_eroze

- Generace md tabulky ze zadaného vstupu
- Změna čísla podle okolních čísel

## Kód_na_md_tabulku
- Vytvořil jsem funkci, která má zadaný field.
```
def md_2d(field):
```
- Dále jsem udělala, že vezmu první řádek změním každý element na string a spojím je s " | ".
- Jako další jsem přidal "|---" podle počtu sloupců pro vytvoření kompletní tabulky.
```
    md = "| " + " | ".join(str(i) for i in field[0]) + " |" + "\n"
    md += "|---" * len(field) + "|" + "\n"
```
- Dále projíždím řádky 2d pole, měním na string a spojuji s " | ".
```
for row in field[1:]:
        md += "| " + " | ".join(str(cell) for cell in row) + " |" + "\n"
```
- Jako poslední dávám na vstup funkce předpřipravení list image2d a vypisuji ho.
```
markdown_table = md_2d(image2d)
print(markdown_table)
```
Finální output:

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

## Kód_na_implementaci_operací
- 
