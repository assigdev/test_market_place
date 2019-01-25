# Test MarketPlace

### RUN

run commands :
    
    git clone https://github.com/assigdev/WW91IGRvbid0IGZpbmQgdGhpcyEh.git
    docker-compose up -d
    docker-compose exec backend python manage.py migrate
    docker-compose exec backend python manage.py cities_light
    docker-compose exec backend python manage.py createsuperuser
    
    # optional
    docker-compose exec backend python manage.py add_random_ads
    
goto [http://127.0.0.1:8000](http://127.0.0.1:8000)

