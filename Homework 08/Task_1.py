def fd(f,*arg):
   try: f(*arg)
   except SystemExit:
     print("ошибка, вызвана функцией sys.exit при выходе из программы")
   except KeyboardInterrupt:
     print("ошибка  вызвана из-за прерывании программы пользователем (обычно сочетанием клавиш Ctrl+C)")
   except GeneratorExit:
     print("ошибка вызвына из-за вызова метода close объекта generator")
   except StopIteration:
     print("ошибка вызвана встроенной функцией next, в итераторе больше нет элементов")
   except ArithmeticError:
     print("арифметическая ошибка")
   except AssertionError:
     print("выражение в функции assert ложно")
   except AttributeError:
     print("объект не имеет данного атрибута (значения или метода)")
   except BufferError:
     print("операция, связанная с буфером, не может быть выполнена")
   except EOFError:
     print("функция наткнулась на конец файла и не смогла прочитать то, что хотела")
   except ImportError:
     print("не удалось импортирование модуля или его атрибута")
   except LookupError:
     print("некорректный индекс или ключ")
   except MemoryError:
     print("недостаточно памяти")
   except OSError:
     print("ошибка, связанная с системой")
   except ReferenceError:
     print("попытка доступа к атрибуту со слабой ссылкой")
   except RuntimeError:
     print("исключение не попадает ни под одну из других категорий")
   except NotImplementedError:
     print("абстрактные методы класса требуют переопределения в дочерних классах")
   except SyntaxError:
     print("синтаксическая ошибка")
   except TypeError:
     print("операция применена к объекту несоответствующего типа")
   except ValueError:
     print("функция получает аргумент правильного типа, но некорректного значения")
   except UnicodeError:
     print("ошибка, связанная с кодированием / раскодированием unicode в строках")


def f1(t,e):
   return e/t

fd(f1,0,1)

