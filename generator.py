import sys

def main():
    print("\n".join([div_n(i) for i in range(5)]))

def div_n(i):
    n = 2**(i+1)
    return  f"""\
operation div_{n}(A,B,Rem) {{
  pre_loop: do load2_(B,Rem,A) goto loop

  loop: if zero B then goto 0 else goto loop_1
  loop_1: do sub B {n-1} goto loop_2

  loop_2: if zero B then goto 0 else goto loop_3
  loop_3: do sub B 1 goto loop_4
  loop_4: do sub Rem {n} goto loop_5
  loop_5: do inc A goto loop
}}
"""

if __name__ == '__main__':
    main()