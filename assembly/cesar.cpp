#include &lt;iostream&gt;
using namespace std;
int main()
{
    char mass[10];
    for (int i = 0; i &lt; 10; i++)
        {
        cin &gt;&gt; mass[i];
        }
    _asm
    {
    mov eax, 0; индекс элемента массива

    start :
        cmp eax, 10
            je finish
            ADD byte ptr[mass + eax], 3; здесь указывается сдвиг

            CMP byte ptr[mass + eax], 90; если выход за границу алфавита
            вправо
            JLE A1
            sub byte ptr[mass + eax], 26
            JMP A2

            A1 :
        CMP byte ptr[mass + eax], 65; если выход за границу алфавита влево
            JGE A2
            add byte ptr[mass + eax], 26
            
            A2: INC eax; увеличиваем индекс на 1
            jmp start; возвращаемся в начало цикла
        finish :
    }
    for (int i = 0; i &lt; 10; i++)
    cout &lt;&lt; mass[i];
}