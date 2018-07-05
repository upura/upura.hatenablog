# W(1)を可視化
plt.style.use('fivethirtyeight')
# draw digit images
def draw_digit_w1(data, n, i, length):
    size = 28
    plt.subplot(math.ceil(length/15), 15, n)
    Z = data.reshape(size,size)   # convert from vector to 28x28 matrix
    Z = Z[::-1,:]                 # flip vertical
    plt.xlim(0,size)
    plt.ylim(0,size)
    plt.pcolor(Z)
    plt.title("%d"%i, size=9)
    plt.gray()
    plt.tick_params(labelbottom="off")
    plt.tick_params(labelleft="off")


plt.figure(figsize=(15,70))
cnt = 1
for i in range(len(l1_W[9])):
    draw_digit_w1(l1_W[9].data[i], cnt, i, len(l1_W[9].data[i]))
    cnt += 1
#    print str(i)
    
plt.show()