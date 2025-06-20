def print_head(text_head, width=44):
    """Imprime el encabezado de cada menú"""
    
    left = int((width-len(text_head))/2)
    right = width - 2 - len(text_head) - left
    print("┌" + "─" * (width-2) + "┐")
    print("│" + " " * left + text_head + " " * right + "│")
    print("└" + "─" * (width-2) + "┘")


print_head("")


print("─"*60)


options = {
    "hola": "hola",
    "color":"verde"
}
option_list = list(options.items())

print(option_list)