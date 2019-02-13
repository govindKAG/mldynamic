
def get_args():
    l = []
    with open('sample-args.txt','r') as f:
        for i in f:
            l.append(i.strip().split(':'))
    print(l)
