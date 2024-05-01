from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Charizard", "bulbasour"])
table.add_column("Type", ["Electric","Fire","Plant"])



print(table)
