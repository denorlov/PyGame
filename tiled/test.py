# level1_map = [
# [340,344,344],
# [261,158,-1],
# [225,225,225],
# [261,-1,-1],
# [261,-1,-1]
# ]

# for r in range(len(level1_map)):
#     row = level1_map[r]
#     print()
#     for c in range(len(row)):
#         print(level1_map[r][c], end=",")

# for (row_idx, row) in enumerate(level1_map):
#     print()
#     for (col_idx, cell) in enumerate(row):
#         print(row_idx, col_idx, cell, end=";    ")

item_code = 158
tile_row = item_code // 20
tile_col = item_code % 20
print(tile_row, tile_col)