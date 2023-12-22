# flattened = []
# def flatten_list(lst):
#     for item in lst:
#         if isinstance(item, list):
#             flatten_list(item)
#         else:
#             flattened.append(item) #  solution via recursive (not mine)
#
# for elem in list_of_lists_2:
#     if isinstance(elem, list):
#         flatten_list(elem)
#     else:
#         flattened.append(elem)
# print(flattened)