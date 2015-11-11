from arrow import *

arr1 = Arrow('red')
arr1.draw()
print ('')
arr1.flip()
print ('')
arr1.draw()

print('')
print ('--------------------')
print('Testing red_flip: ')
red_list = [Arrow('red') for i in range(10)]

red_list[6] = Arrow('white')
red_list[1] = Arrow('white')
red_list[3] = Arrow('white')

print_arrow_list(red_list)
print ('')
red_flip(red_list)
print('')
print_arrow_list(red_list)
print('')

print ('--------------------------')


print ('Testing blue_flip: ')

red_list[2] = Arrow('blue')
red_list[0] = Arrow('blue')

print_arrow_list(red_list)
print('')
blue_flip(red_list, red_list[0])
print('')
print_arrow_list(red_list)

print('')
print('--------------------------')

print ('Random list:')
rand1 = generate_rand_list(9)
print ('Using colored flip on the second arrow:')
print_arrow_list(rand1)
print('')
colored_flip(rand1, rand1[1])
print_arrow_list(rand1)


print('')
print('-------------')
print('testing random puzzle generation')

disordered1 = generate_disordered_list(9)
print_arrow_list(disordered1)
