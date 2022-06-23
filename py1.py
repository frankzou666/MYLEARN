import numpy as np
from keras.models import Sequential
from keras.layers import Dense

def main():
     #产生随机数seed
     np.random.seed(2018)
     #构建1000*3,500*3两个矩䧃
     taindata = np.random.random((1000,3))
     testdata = np.random.random((500,3))
     validata = np.random.random((500, 3))
     #构建1000*1矩阵，且数字是0-1之间
     tainlabel = np.random.randint(2,size=(1000,1))
     valilabel = np.random.randint(2, size=(500, 1))
     #新建模型对像
     model = Sequential()
     #第一层是5个neural
     model.add(Dense(20,input_dim=3,activation='relu'))
     #第二个是4个neural
     model.add(Dense(5000, activation='relu'))
     model.add(Dense(5000, activation='relu'))
     model.add(Dense(5000, activation='relu'))
     model.add(Dense(5000, activation='relu'))
     model.add(Dense(10, activation='relu'))
     #产生sigmoid
     model.add(Dense(1, activation='sigmoid'))
     #编译
     model.compile(loss='binary_crossentropy',optimizer='Adam',metrics=['accuracy'])
     #训练数据
     model.fit(taindata,tainlabel,epochs=10,batch_size=128,validation_data=(validata,valilabel))
     #预测
     model.save('keras.model')
     prediction = model.predict(testdata)
     print(prediction[:10])


     #print(tainlabel)

if __name__ == '__main__':
    main()