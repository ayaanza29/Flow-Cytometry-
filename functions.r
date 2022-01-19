#jpeg("user_plot.jpeg", quality = 75)
#plot(iris)
#dev.off()

library(ggplot2)

p <- ggplot(iris, aes(x=Sepal.Length, y=Sepal.Width)) + geom_point()
p
ggsave("temporary_images/user_plot.jpeg")