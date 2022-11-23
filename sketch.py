# from sketchpy import library as lib
# obj=lib.ironman_ascii()
# obj.draw()

x, y, z = 0, 1, 0

# if x == 1 or y == 1 or z == 1:
#     print('passed')
# else:
#     print("failed")

# if 1 in (x, y, z):
#     print('passed')
# else:
#     print("failed")


# These only test for truthiness:
# if x or y or z:
#     print('passed')

if any((x, y, z)):
    print('passed')