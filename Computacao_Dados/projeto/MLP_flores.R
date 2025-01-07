library(keras)
library(datasets)

data(iris)

X <- iris[, 1:4]
y <- as.numeric(iris$Species) - 1


X <- scale(X)

set.seed(123)
indices <- sample(1:nrow(X), size = 0.8 * nrow(X))
X_train <- X[indices, ]
y_train <- y[indices]
X_test <- X[-indices, ]
y_test <- y[-indices]

model <- keras_model_sequential() %>%
  layer_dense(units = 64, activation = 'relu', input_shape = c(4)) %>%
  layer_dense(units = 32, activation = 'relu') %>%
  layer_dense(units = 3, activation = 'softmax')

model %>%
  compile(
    loss = 'sparse_categorical_crossentropy',
    optimizer = 'adam',
    metrics = c('accuracy')
  )

history <- model %>%
  fit(
    X_train, y_train,
    epochs = 50,
    batch_size = 8,
    validation_data = list(X_test, y_test)
  )

score <- model %>% evaluate(X_test, y_test)
cat('Loss:', score$loss, '\n')
cat('Accuracy:', score$accuracy, '\n')

predictions <- model %>% predict(X_test)
predicted_classes <- apply(predictions, 1, which.max) - 1

table(predicted_classes, y_test)
