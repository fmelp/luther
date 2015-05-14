# luther

### [Movie data visualization with D3.js!](http://bl.ocks.org/anonymous/raw/e630ef973988fa15d538/)

##Analyzed data from 3,500 movies
  - data collection:
    - collected top 100 grossing movies from years 1980-2015
    - original data from BoxOfficeMojo
    - additional data from IMDB, The-Numbers, RottenTomatoes, Metacritic
    - Tools: Selenium, BeautifulSoup
  - data analysis:
    - cleaned data with python and pandas
    - linear regression analysis with Statsmodel, SciKit-Learn
    - visualization with Seaborn and Matplotlib
  - conclusions:
    - tried to predict which genres of movies would yield highest gross box office revenue to budget ratio
      - which movies would generate the highest investment return multiple
    - found that horror, family, and highly rated comedy movies generate highest Beta values for this metric
      - makes sense because these genres tend to be low budget, but have the potential to make a lot at the box office
