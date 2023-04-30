import argparse

parsx = argparse.ArgumentParser(description='Calculadora')
parsx.add_argument('-o', '--operator', choices=['+', '-', '*', '/'],help='the operator to use')
parsx.add_argument('-n', '--first', type=int, help='the first number')
parsx.add_argument('-m', '--second', type=int, help='the second number')
args = parsx.parse_args()

if args.operator == '+':
    result = args.first + args.second

elif args.operator == '-':
    result = args.first - args.second

elif args.operator == '*':
    result = args.first * args.second

elif args.operator == '/':
    result = args.first / args.second
    
else:
    print('La operacion es invalida')
    exit()

print(f'{args.first} {args.operator} {args.second} = {result}')