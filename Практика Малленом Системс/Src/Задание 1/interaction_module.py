import program_module

print('Программа для форматирования изображения')
print('Выберите действие:')

choice = input('Введите 1 - если хотите изменить размер изображения или 2 - если хотите повернуть изображение:')
image_path = input('Введите путь к изображению:')

if choice == '1':
    width = int(input('Введите новое значение ширины:'))
    height = int(input('Введите новое значение высоты:'))
    new_name = input('Введите новое имя для изображения')
    result_path = program_module.resize_image(image_path, width, height, new_name)
    print(f'Изображение сохранено на рабочем столе: {result_path}')

elif choice == '2':
    angle = int(input('Введите угол поворота:'))
    new_name = input('Введите новое имя для изображения')
    result_path = program_module.rotate_image(image_path, angle, new_name)
    print(f'Изображение сохранено на рабочем столе: {result_path}')

else:
    print('Неверный выбор')
