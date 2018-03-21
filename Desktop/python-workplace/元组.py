#传说中的元组
zoo=('elephant','monkey','wolf')
print('The animals in the zoo are:',zoo)
newZoo=('girafee','penguin',zoo)
print('The animails in the new zoo are:',newZoo)
print('The animals bought form the old zoo are:',newZoo[2])
print('The last animal bought from the old zoo is:',newZoo[2][2]) 
#变量zoo指的是一个包含项目的元组，此时zoo和newZoo的len都是3
#此时在python里我们称[]为索引运算符
#zoo和newZoo其实可以不用打括号，但打了会比较明了
#特别说一句（懒得再写一个代码了ORZ）要指定只有一个元素的数组时，必须在元素后打个括号
