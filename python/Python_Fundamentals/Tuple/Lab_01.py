
# Slicing

the_best_team = ('Scorpion','Subzero','Liu Kang', 'Kitana', 'Kung Lao', 'Johnny Cage', 'Sonya Blade', 'Jax')
the_worst_team = ('Shao Kahn', 'Sindel','Shang Tsung', 'Mileena', 'Noob Saibot', 'Kano', 'Kintaro', 'Goro')

tuple_3 = the_best_team + the_worst_team

print(tuple_3)

print(tuple_3[0:3])
print(tuple_3[5:9])
print(tuple_3[5])
print(tuple_3[::2])
print(tuple_3[-2])
print(tuple_3[::-2])
print(tuple_3[3::-2])

tuple_4 = ('Sarıyer', ('Suadiye', 'Erenköy'), ('Yeniköy', 'Bebek', ('Etiler', 'Ulus')))

print(tuple_4[0])
print(tuple_4[1][0])
print(tuple_4[2][2][1])

