def get_adj_matrix(clients):
    pass

clients = [
            ["Yalitza Aparicio", "Julio Torres"],
            ["Julio Torres", "Fred Armisen"],
            ["Bowen Yang", "Julio Torres"],
            ["Bowen Yang", "Margaret Cho"],
            ["Margaret Cho", "Ali Wong"],
            ["Ali Wong", "Fred Armisen"],
            ["Ali Wong", "Bowen Yang"]]

id_map, adj_matrix = get_adj_matrix(clients)
print(id_map)
print(adj_matrix)
