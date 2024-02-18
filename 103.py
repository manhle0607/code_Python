class student:
    def __init__(self, self_name, self_correct, self_submit):
        self.self_name = self_name
        self.self_correct = self_correct
        self.self_submit = self_submit

a = []

for t in range(int(input())):
    s = input()
    x,y = [int(i) for i in input().split()]
    a.append(student(s,x,y))
    
a.sort(key=lambda i: ((-1) * i.self_correct, i.self_submit, i.self_name))
for i in a:
    print('{} {} {}'.format(i.self_name, i.self_correct, i.self_submit))