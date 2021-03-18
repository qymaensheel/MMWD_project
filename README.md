# MMWD_covid_project

Zagadnienie dotyczy rozwiązania problemu dowozu żywienia do osób, które są na kwarantannie domowej. Każda restauracja dysponuje listą domów, które może obsłużyć, a także 
ilością dostępnych posiłków. Ilość mieszkańców każdego domostwa determinuje zapotrzebowanie na posiłki oraz jest obsługiwane przez jedną firmę/może być obsługiwane przez 
wiele firm. Dodatkowym parametrem jest odległość domów od restauracji. Chcemy zminimalizować sumę odległości między restauracjami a obsługiwanymi przez nie mieszkaniami 
biorąc pod uwagę możliwości produkcyjne lokalów gastronomicznych.
Projekt realizowany w 3 osobowym zespole: Balibna Molerus, Tomasz Wojakowski, Bartosz Nieroda.

**Dane wejściowe:**

Lista restauracji z informacjami:
  - możliwy zasięg dowozu 
  - ilości dziennie produkowanych porcji posiłków

Lista domów z informacjami:
  - lokalizacja
  - zapotrzebowanie na posiłki (porcje) 

**Założenia:**

  - dom otrzymuję całe zapotrzebowanie od jednej restauracji lub może przyjąć dzielone porcję od kilku.
  - przepustowość restauracji dziennej jest stała
  - zapotrzebowanie dzienne domów jest stałe
  - zakładamy, że po każdym dostarczeniu do odbiorcy dostawca wraca do lokalu po kolejne porcje
  - między mieszkaniem a restauracją jest jedna trasa 


**Model matematyczny:**

Parametry:
  - R - zbiór restauracji serwujących posiłki
  - M - zbiór mieszkań z osobami na kwarantannie
  - Di,j - droga dzieląca restauracje i mieszkania
  - Pi - zapotrzebowanie porcji posiłków dla każdego mieszkania na kwarantannie
  - Ji  - ilość możliwych do dostarczenia porcji posiłków przez restaurację

Funkcja celu

![image](https://user-images.githubusercontent.com/49729749/111630480-b2691a80-87f2-11eb-82cd-6f33e918f1c7.png)


