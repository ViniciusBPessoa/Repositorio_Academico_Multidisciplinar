getwd()

setwd("C:/Users/Pichau/Desktop/Faculdade/Projects/Repositorio_Academico_Multidisciplinar/Computacao_Dados/projeto")

alternativas_separadas <- read.csv('alternativas_separadas.csv')
tudo_junto <- read.csv('tudo_junto.csv')


library(stringr)
library(tm)

preprocess_text <- function(text) {
  text <- tolower(text)
  
  text <- str_remove_all(text, "[[:punct:]]")
  
  tokens <- unlist(str_split(text, "\\s+"))
  
  stop_words <- stopwords("pt")
  tokens <- tokens[!tokens %in% stop_words]
  
  stemmer <- function(word) SnowballC::wordStem(word, language = "portuguese")
  tokens <- sapply(tokens, stemmer)
  
  termos_importantes <- c(
    "literatura", "gramática", "redação", "interpretação", "semântica",
    "figuras", "coesão", "coerência", "gêneros", "sintaxe", "morfologia",
    "poesia", "história", "geografia", "sociologia", "filosofia", "política",
    "economia", "cultura", "revolução", "cidadania", "constituição", "guerra",
    "democracia", "direitos", "biologia", "física", "química", "célula",
    "genética", "evolução", "fotossíntese", "termoquímica", "tabela", "periodica",
    "eletricidade", "força", "energia", "função", "álgebra", "geometria",
    "probabilidade", "estatística", "cálculo", "triângulo", "progressão", "vetor", "polinômio"
  )
  
  tokens <- tokens[nchar(tokens) > 2 | tokens %in% termos_importantes]
  
  text <- paste(tokens, collapse = " ")
  return(text)
}

alternativas_separadas <- read.csv("alternativas_separadas.csv", stringsAsFactors = FALSE)
tudo_junto <- read.csv("tudo_junto.csv", stringsAsFactors = FALSE)

for (col in colnames(alternativas_separadas)[2:(ncol(alternativas_separadas) - 1)]) {
  alternativas_separadas[[col]] <- sapply(alternativas_separadas[[col]], preprocess_text)
}

write.csv(alternativas_separadas, "alternativas_separadas_pp.csv", row.names = FALSE)

tudo_junto$Enunciado_Alternativas <- sapply(tudo_junto$Enunciado_Alternativas, preprocess_text)

write.csv(tudo_junto, "tudo_junto_pp.csv", row.names = FALSE)

alternativas_separadas <- read.csv('alternativas_separadas.csv')
tudo_junto <- read.csv('tudo_junto.csv')
alternativas_separadas_pp <- read.csv('alternativas_separadas_pp.csv')
tudo_junto_pp <- read.csv('tudo_junto_pp.csv')

# -------------------------------------------------------------------------

if (!require(dplyr)) install.packages("dplyr")
library(dplyr)

# Passo 1
mapa_personalizado <- c(
  "Linguagens" = 0,
  "Ciências Humanas" = 1,
  "Ciências da Natureza" = 2,
  "Matemática" = 3
)

# Passo 2
alternativas_separadas$Area_de_Conhecimento <- recode(alternativas_separadas$Area_de_Conhecimento, !!!mapa_personalizado)
tudo_junto$Area_de_Conhecimento <- recode(tudo_junto$Area_de_Conhecimento, !!!mapa_personalizado)
alternativas_separadas_pp$Area_de_Conhecimento <- recode(alternativas_separadas_pp$Area_de_Conhecimento, !!!mapa_personalizado)
tudo_junto_pp$Area_de_Conhecimento <- recode(tudo_junto_pp$Area_de_Conhecimento, !!!mapa_personalizado)

#------------------------------------------------------------------------
if (!require(caret)) install.packages("caret")
library(caret)

set.seed(1) 
indices <- createDataPartition(tudo_junto_pp$Area_de_Conhecimento, p = 0.8, list = FALSE)

X_train <- tudo_junto_pp$Enunciado_Alternativas[indices]
y_train <- tudo_junto_pp$Area_de_Conhecimento[indices]

X_test <- tudo_junto_pp$Enunciado_Alternativas[-indices]
y_test <- tudo_junto_pp$Area_de_Conhecimento[-indices]

#-------------------------------------------------------------------------
if (!require(tm)) install.packages("tm")
if (!require(SnowballC)) install.packages("SnowballC")

library(tm)
library(SnowballC)

corpus_train <- Corpus(VectorSource(X_train))

tdm_train <- TermDocumentMatrix(corpus_train, control = list(
  weighting = weightTfIdf,
  bounds = list(global = c(1, 5000))
))

X_train_tfidf <- as.matrix(tdm_train)

X_train_tfidf <- as.matrix(X_train_tfidf)

corpus_test <- Corpus(VectorSource(X_test))

tdm_test <- TermDocumentMatrix(corpus_test, control = list(
  weighting = weightTfIdf,
  dictionary = Terms(tdm_train)
))

X_test_tfidf <- as.matrix(tdm_test)

X_test_tfidf <- as.matrix(X_test_tfidf)

X_test_tfidf <- t(X_test_tfidf)
X_train_tfidf <- t(X_train_tfidf)

# ------------------------------------------------------------------------
if (!require(keras)) install.packages("keras")
library(keras)

create_deep_model <- function(input_dim, output_dim, dense_layers) {
  model <- keras_model_sequential()
  
  model <- model %>%
    layer_dense(units = dense_layers[1], activation = 'relu', input_shape = c(input_dim))
  
  for (neurons in dense_layers[2:length(dense_layers)]) {
    model <- model %>%
      layer_dense(units = neurons, activation = 'relu')
  }
  
  model <- model %>%
    layer_dense(units = output_dim, activation = 'softmax')
  
  model <- model %>% compile(
    optimizer = 'adam',
    loss = 'categorical_crossentropy',
    metrics = c('accuracy')
  )
  
  return(model)
}

input_dim <- ncol(X_train_tfidf)  
output_dim <- length(unique(y_train)) 
dense_layers <- c(128, 64, 32)

model <- create_deep_model(input_dim, output_dim, dense_layers)

# ---------------------------------------------------------------------------------------

summary(model)


y_train_cat <- to_categorical(y_train, num_classes = output_dim)
y_test_cat <- to_categorical(y_test, num_classes = output_dim)

history <- model %>% fit(
  X_train_tfidf, y_train_cat,  
  epochs = 200,                 
  batch_size = 32,             
  validation_data = list(X_test_tfidf, y_test_cat),  
  verbose = 1
)


save_model_hdf5(model, "modelo_treinado.h5")

plot(history)

entrada_exemplo <- X_test_tfidf[28, , drop = FALSE]
classe_verdadeira <- y_test[28]

previsao <- model %>% predict(entrada_exemplo)

classe_predita <- which.max(previsao) - 1

cat("Classe predita:", classe_predita, "\n")
cat("Classe verdadeira:", classe_verdadeira, "\n")

