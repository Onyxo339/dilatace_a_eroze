image2d = [[4 - max(abs(i - 4), abs(j - 4)) for j in range(9)] for i in range(9)]

def md_2d(field):
    md = "| " + " | ".join(str(i) for i in field[0]) + " |\n"
    md += "|---" * len(field[0]) + "|\n"
    
    for row in field[1:]:
        md += "| " + " | ".join(str(cell) for cell in row) + " |\n"
    
    return md

markdown_table = md_2d(image2d)
print(markdown_table)