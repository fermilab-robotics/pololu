import time
from machine import Pin
from pololu import POLOLU_36v4 as Pololu

def main():
    p = Pololu(DirPin=Pin(0), StepPin=Pin(1))
    
    print({p})
    while True:
        p.step_forward(100)
        time.sleep(5)
        p.step_backwards(101, delay=10)
        time.sleep(5)
            
    return

if __name__ == "__main__":
    main()