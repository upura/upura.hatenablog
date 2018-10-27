library(ChannelAttribution)
library(reshape2)
library(ggplot2)
data(PathData)

path <- c(
  "柏木 > 岩波",
  "森脇 > 興梠 > 宇賀神 > 槙野 > 柏木 > 宇賀神 > 青木 > 武藤",
  "阿部 > 青木 > ナバウト > 武藤"
)

total_conversions <- rep(1, length(path))

Data <- data.frame(
  path = path,
  total_conversions = total_conversions
)

#ヒューリスティックモデルを推定
H = heuristic_models(Data, 'path', 'total_conversions')

#マルコフ連鎖モデルを推定
M = markov_model(Data, 'path', 'total_conversions', out_more = TRUE)

#合計コンバージョンをプロット
R = merge(H, M$result, by='channel_name')

g <- ggplot(R, aes(x = channel_name, y = total_conversions))
g <- g + geom_bar(stat = "identity") + theme_gray (base_family = "HiraKakuPro-W3") + labs(title="マルコフ連鎖モデル", x="", y="貢献度")

plot(g)

# マルコフ連鎖モデルの掘り下げ

############## visualizations ##############
# transition matrix heatmap for "real" data
df_plot_trans <- M$transition_matrix

cols <- c("#e7f0fa", "#c9e2f6", "#95cbee", "#0099dc", "#4ab04a", "#ffd73e", "#eec73a",
          "#e29421", "#e29421", "#f05336", "#ce472e")
t <- max(df_plot_trans$transition_probability)

ggplot(df_plot_trans, aes(y = channel_from, x = channel_to, fill = transition_probability)) +
  theme_minimal() +
  geom_tile(colour = "white", width = .9, height = .9) +
  scale_fill_gradientn(colours = cols, limits = c(0, t),
                       breaks = seq(0, t, by = t/4),
                       labels = c("0", round(t/4*1, 2), round(t/4*2, 2), round(t/4*3, 2), round(t/4*4, 2)),
                       guide = guide_colourbar(ticks = T, nbin = 50, barheight = .5, label = T, barwidth = 10)) +
  geom_text(aes(label = round(transition_probability, 2)), fontface = "bold", size = 4) +
  theme(legend.position = 'bottom',
        legend.direction = "horizontal",
        panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        plot.title = element_text(size = 20, face = "bold", vjust = 2, color = 'black', lineheight = 0.8),
        axis.title.x = element_text(size = 24, face = "bold"),
        axis.title.y = element_text(size = 24, face = "bold"),
        axis.text.y = element_text(size = 8, face = "bold", color = 'black'),
        axis.text.x = element_text(size = 8, angle = 90, hjust = 0.5, vjust = 0.5, face = "plain"),
        text = element_text(family = "HiraKakuPro-W3")) +
  ggtitle("Transition matrix heatmap")

# 取り除いた時の影響
## https://www.lunametrics.com/blog/2016/06/30/marketing-channel-attribution-markov-models-r/
g <- ggplot(M$removal_effects, aes(x = channel_name, y = removal_effects))
g <- g + geom_bar(stat = "identity") + theme_gray (base_family = "HiraKakuPro-W3") + labs(title="Removal Effects", x="", y="Removal Effects")
plot(g)
