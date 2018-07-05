# W(2).Tを可視化
plt.style.use('fivethirtyeight')
# draw digit images

def draw_digit2(data, i, length):
    size = 28
    plt.subplot(math.ceil(length/15)+1, 15, i+1)
    Z = data.reshape(size,size)   # convert from vector to 28x28 matrix
    Z = Z[::-1,:]                 # flip vertical
    plt.xlim(0,27)
    plt.ylim(0,27)
    plt.pcolor(Z)
    plt.title("%d"%i, size=9)
    plt.gray()
    plt.tick_params(labelbottom="off")
    plt.tick_params(labelleft="off")

W_T = np.array(l2_W[9].data).T

plt.figure(figsize=(15,70))
for i in range(W_T.shape[0]):
    draw_digit2(W_T[i], i, W_T.shape[0])
    
plt.show()