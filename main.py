# Ивановская 9г
# Статический класс «Калькулятор площадей» с методами вычисления площади треугольника по трем сторонам, площади прямоугольника, площади круга, 
# которая принимает π и радиус. Декоратор, который функцию от 2 аргументов, превращает в функцию от 1 аргумента, 
# автоматически подставляя вместо первого pi из математического модуля. Декорировать метод нахождения площади круга.
from area_calculator import AreaCalculator

def display_main_menu():
    print("\nВыберите способ ввода данных:")
    print("1. Ввод данных из файла (inp.txt)")
    print("2. Ввод данных из консоли")
    print("3. Выход")

def calc_menu():
    print("\nМеню калькулятора площадей:")
    print("1. Вычислить площадь треугольника")
    print("2. Вычислить площадь прямоугольника")
    print("3. Вычислить площадь круга")

def input_data_from_file():
    with open('inp.txt', 'r') as file:
        line = file.readline().strip()
        data = line.split(' ')
        if len(data) == 3:
            a, b, c = map(float, data[0:3])
            area = AreaCalculator.triangle_area(a, b, c)
            return {"type": "треугольник", "area": area}
        elif len(data) == 2:
            length, width = map(float, data[0:2])
            area = AreaCalculator.rectangle_area(length, width)
            return {"type": "прямоугольник", "area": area}
        elif len(data) == 1:
            radius = float(data[0])
            area = AreaCalculator.circle_area(radius)
            return {"type": "круг", "area": area}
    
def input_data_from_console(shape):
    if shape == '1': #треугольник
        a = float(input("Введите длину стороны a: "))
        b = float(input("Введите длину стороны b: "))
        c = float(input("Введите длину стороны c: "))
        area = AreaCalculator.triangle_area(a, b, c)
        return {"type": "треугольник", "area": area}
    
    elif shape == '2': #прямоугольник
        length = float(input("Введите длину прямоугольника: "))
        width = float(input("Введите ширину прямоугольника: "))
        area = AreaCalculator.rectangle_area(length, width)
        return {"type": "прямоугольник", "area": area}
    
    elif shape == '3': #круг
        radius = float(input("Введите радиус круга: "))
        area = AreaCalculator.circle_area(radius)
        return {"type": "круг", "area": area}

def output_results(result):
    if result is None:
        print("Нет результатов для вывода.")
        return
    
    output_choice = input("Куда вывести результат? (1 - на консоль, 2 - в файл): ")
    if output_choice == '1':
        print(f"Фигура: {result['type']}; Площадь: {result['area']:.2f}")
    elif output_choice == '2':
        with open('out.txt', 'w', encoding='utf-8') as out_file:
            out_file.writeprint(f"Фигура: {result['type']}; Площадь: {result['area']:.2f}")
        print("Данные загружены в файл 'out.txt'.")
    else:
        print("Неверный ввод. Результат не был выведен.")

choice = 0
        
while choice!='4':
    display_main_menu()
    choice = input("-> ")

    if choice == '1':
            result = input_data_from_file()
            output_results(result)
                
    elif choice == '2':
        while True:
            calc_menu()
            shape = input("-> ")
            if shape in ['1', '2', '3']:
                result = input_data_from_console(shape)
                output_results(result)
                break
            else:
                print("Неверный ввод. Пожалуйста, попробуйте снова.")
    elif choice == '3':
        print("Выход из программы.")
        break
    
    else:
        print("Неверный ввод. Пожалуйста, попробуйте снова.")