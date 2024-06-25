class New:
    def __getitem__(self, index):
        if len(self.val1) > len(self.val2):
            for i in range(len(self.val1)):
                self.val2.append(0)
        else:
            self.val1.append(0)
        return self.val1[index] + self.val2[index]

    def __str__(self):
        return str(self.val1) + "; " + str(self.val2)


A = New()
A.val1 = [0, 1, 2]
A.val2 = [0, 1, 2, 1]
print(A)
print(A[3])