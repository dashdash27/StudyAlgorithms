#include <iostream>
using namespace std;
double top, rezq;
int main()
{
    //вводим значение s
    double s, no_round, round, frac, two_round, two_frac, ou, power, result=0;
    cout << "s = ";
    cin >> s;
    double n = 1, one = 1;
    _asm {

        fld n; помещаем единичку в самый низ стека
        mov eax, 0

        ;цикл
        cy: cmp eax, 500
            je go
            ; 1 -- - ищем степень двойки(это логарифм умноженный на s)
            fst n
            fld s;
            fld n;
            fyl2x; теперь в стеке : [n, (cтепень двойки)]

            ; 2 -- - разделяем эту степень двойки на дробную и целую часть
            fst no_round; заносим в память неокругленное
            frndint; округлили
            fst round; заносим в память округленное
            fstp ou; теперь в стеке : [n]
            fld no_round
            fsub round
            fst frac; заносим в память дробную часть
            fstp ou; в стеке снова только n

            ; 3 -- - возводим двойку в целую степень
            fld round; добавляем целую часть степени в стек
            fld one; добавляем единичку в стек
            fscale; теперь в стеке[n, round, 2 ^ round]
            fst two_round
            fstp ou
            fstp ou; теперь в стеке только n

            ; 4 -- - возводим двойку в дробную степень
            fld frac; добавляем в стек дробную часть
            f2xm1; возвели в степень
            fadd one; добавляем потерянную единичку
            fst two_frac
            fstp ou

            ; 5 -- - умножаем two_frac на two_round
            fld two_frac
            fmul two_round
            fst power; это и есть двойка в той страшной степени
            fstp ou

            ; 6 -- - единицу делим на результат пункта 5
            fld one
            fdiv power
            fadd result
            fst result; теперь все прибавили к результату
            fstp ou
            fadd one; прибавили к n единичку
            
            add eax, 1
            jmp cy
        go:

    }
    cout << result << endl;
}