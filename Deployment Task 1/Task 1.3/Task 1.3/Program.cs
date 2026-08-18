using System.Runtime.InteropServices;

class Program
{
    const int VK_LBUTTON = 0x01;

    [DllImport("user32.dll")]
    static extern short GetAsyncKeyState(int vKey);

    static void Main()
    {
        Console.WriteLine("Listening for left clicks. Ctrl+C to quit.");

        bool wasDown = false;
        while (true)
        {
            bool isDown = (GetAsyncKeyState(VK_LBUTTON) & 0x8000) != 0;

            if (isDown && !wasDown)
                Console.WriteLine("Left click pressed");

            wasDown = isDown;
            Thread.Sleep(10);
        }
    }
}