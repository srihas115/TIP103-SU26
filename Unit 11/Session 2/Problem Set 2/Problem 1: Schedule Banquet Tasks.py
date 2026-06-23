def prepare_banquet(tasks, prerequisites):
    pass

tasks_1 = ["set_table", "prepare_dessert"]
prerequisites_1 = [["prepare_dessert", "set_table"]]

tasks_2 = ["stock_pantry", "main_course", "decorations", "serve_food"]
prerequisites_2 = [["main_course", "stock_pantry"], ["decorations", "stock_pantry"], ["serve_food", "main_course"], ["serve_food", "decorations"]]

tasks_3 = ["only_task"]
prerequisites_3 = []

print(prepare_banquet(tasks_1, prerequisites_1))
print(prepare_banquet(tasks_2, prerequisites_2))
print(prepare_banquet(tasks_3, prerequisites_3))
