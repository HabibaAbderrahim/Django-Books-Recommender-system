# Books-Recommender-system
Le site WeBook est un site de visualization des livres de divertissement de type science fiction, computer, Horror implémenté par le Framework écrit en Python Django <br>
Ce site permettra de réaliser les opérations suivantes :<br>
-Gérer l’authentification d’utilisateurs :<br>
Register<br>
Login<br>
Logout<br>
-Rechercher Un livre dans la barre de recherche<br>
- naviguer les divers livre selon Catalogue de livre<br>
-naviguer les divers livre selon la langue de livre<br>
-Consulter les livres similaire par catégorie liée au livre choisie<br>
-Recommandation de Top 3 premiers livre similaire au livre sélectionné selon son contenus .<br>

<h2>Outil :</h2><br>
Visual studio Code , XAMPP ,phpmyadmin to handel Myqsl <br>

<h3>Access Admin Aria : </h3> http://localhost:8000/admin/<br>
<h3>Noter bien :</h3> j'ai mappé des tables dans la base test Mysql en Models via les etapes suivantes:<br>

<h3>1-Changement de setting.py :</h3><br>

# Database properties<br>
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases<br>
----------------------------------------------------------------------------------<br>
DATABASES = {<br>
    'default': {<br>
       
       'ENGINE': 'django.db.backends.mysql',<br>
'NAME': 'test',<br>
'USER': 'root',<br>
'PASSWORD': '',<br>
'HOST': 'localhost',<br>
'PORT': '3306',<br>
'OPTIONS': {<br>
'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"<br>
}
    },<br>
   
    
}
-----------------------------------------------------------------------------------------<br>
<h3>2-Migration de la base Msql :</h3><br>
cmd: python manage.py makemigrations<br>
<h3>3-d’une base de données sql a un model Django :</h3><br>
cmd : python manage.py inspectdb > models.py<br>
------------------------------------------------------------------------------------------<br>
NB : via ce lien vous trouvez le code de recommandation contenat Top 3 book similaires <br>
(l'idée est simple j'ai traité un algorithme de recommandation de top 3 books similaire par la suite je l'ai stocké les resultat dans une base nomé Top (par la suite j'ai 
appliqué l'ORM comme noté ci dessus).<br>
<h2>lien :</h2> https://github.com/HabibaAbderrahim/recomandation-system-python
