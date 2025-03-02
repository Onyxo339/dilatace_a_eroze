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
- Vytvářim funkci pro dilataci, kde na vstupu je image2d.
```
def dil(image2d):
```
- Vytvořim novou matici pod jménem new_image, abych ukládal updatované hodnoty.
```
new_image = [[0] * width for _ in range(height)]
```
- Dále použiju for loop pro projetí jak sloupců tak řádků.
- If statementy zjištují zda je nalevo, napravo, nahoře nebo dole hodnota.
- Pokud ano tak zjistím jaké je na pozici číslo a uložím ho.
- Nakonec vracím největší hodnotu co jsem našel
```
for i in range(height):
        for j in range(width):
            neighbors = [image2d[i][j]]
            if i > 0: 
                neighbors.append(image2d[i-1][j]) 
            if i < height-1: 
                neighbors.append(image2d[i+1][j])  
            if j > 0: 
                neighbors.append(image2d[i][j-1])  
            if j < width-1: 
                neighbors.append(image2d[i][j+1])  

            new_image[i][j] = max(neighbors)

return new_image
```
- Dále dělám udělám celý proces znovu jen vrátím nejmenší hodnotu.
```
def er(image2d):
    height = len(image2d)
    width = len(image2d)
    new_image = [[0] * width for _ in range(height)]

    for i in range(height):
        for j in range(width):
            neighbors = [image2d[i][j]]
            if i > 0: 
                neighbors.append(image2d[i-1][j])  
            if i < height-1: 
                neighbors.append(image2d[i+1][j])  
            if j > 0: 
                neighbors.append(image2d[i][j-1]) 
            if j < width-1: 
                neighbors.append(image2d[i][j+1])  

            new_image[i][j] = min(neighbors)  

    return new_image
```
- Jako poslední vytvořím 3 for loopy pro zobrayení originálního pole, po dilataci a po erozi
```
print("Original:")
for row in image2d:
    print(row)

print("Dilatace:")
dilated = dil(image2d)
for row in dilated:
    print(row)

print("Eroze:")
eroded = er(image2d)
for row in eroded:
    print(row)
```
