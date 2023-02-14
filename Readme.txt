Local Postgres run

    docker volume create postgres-volume
    docker run --name postgres-db -e POSTGRES_USER=user_short -e POSTGRES_PASSWORD=password_short_11 -e POSTGRES_DB=short_urls -p 5432:5432 -v pgdata:/var/lib/postgresql/data/ -d postgres