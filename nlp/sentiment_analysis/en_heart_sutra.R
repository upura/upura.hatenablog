# https://www.holymtn.com/homepage/tea-ware/references-tea-asian-teapot/buddhist-heart-sutra/
# https://www.slideshare.net/langstat/r-75299421

library("SentimentAnalysis")

documents <- c(
  "When Avalokitesvara Bodhisattva is practising the profound Prajna-paramita.", 
  "He sees and illuminates to the emptiness of the five skandhas", 
  "Thus attains deliverance from all suffering.", 
  "Sariputra, matter is not different from emptiness",
  "Emptiness is not different from matter.",
  "Matter is emptiness and emptiness is matter.",
  "So too are sensation, recognition, volition and consciousness.",
  "Sariputra, the emptiness character of all dharmas, neither arises nor ceases, is neither pure nor impure, and neither increases nor decreases.",
  "Therefore, in emptiness: there is no matter, no sensation, recognition, volition or consciousness, no eye, ear, nose, tongue, body, or mind, no sight, sound, scent, taste, tangibles, or dharma, no field of the eye up to no field of mental consciousness, no suffering, no cause of suffering, no ending of suffering, and no path, no wisdom and also no attainment.",
  "Because there is nothing obtainable.",
  "Bodhisattvas through the reliance on Prajna-paramita have no attachment and hindrance in their minds.",
  "Because there is no more attachment and hindrance.",
  "There is no more fear.",
  "Far away from erroneous views and wishful-thinking, Ultimately : The Final Nirvana.",
  "Therefore, realize that Prajna-paramita is the great wondrous mantra, the great radiant mantra, the unsurpassed mantra, and the unequalled mantra.",
  "It can eradicate all suffering, and It is genuine and not false.",
  "Therefore, utter the Prajna-paramita mantra.",
  "Chant: Gate Gate Paragate Parasamgate Bodhisvaha!"
)

# Analyze sentiment
sentiment <- analyzeSentiment(documents)

# Extract dictionary-based sentiment according to the QDAP dictionary
sentiment$SentimentQDAP

# Rate of negative/neutral/positive
table(convertToDirection(sentiment$SentimentGI))

# Plot
plot(sentiment$SentimentQDAP, type="l") 
