# 入力と出力を可視化
plt.style.use('fivethirtyeight')

plt.figure(figsize=(15,25))

num = 100
cnt = 0
ans_list  = []
pred_list = []
for idx in np.random.permutation(N_test)[:num]:
    xxx = x_test[idx].astype(np.float32)
    h1 = F.dropout(F.relu(model.l1(Variable(xxx.reshape(1,784)))),  train=False)
    y  = model.l2(h1)
    cnt+=1
    ans_list.append(x_test[idx])
    pred_list.append(y)

cnt = 0
for i in range(int(num/10)):
    for j in range (10):
        img_no = i*10+j
        pos = (2*i)*10+j
        draw_digit_ae(ans_list[img_no],  pos+1, 20, 10, "ans")
        
    for j in range (10):
        img_no = i*10+j
        pos = (2*i+1)*10+j
        draw_digit_ae(pred_list[i*10+j].data, pos+1, 20, 10, "pred")
    
plt.show